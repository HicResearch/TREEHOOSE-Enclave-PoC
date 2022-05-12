# USAGE
# python search.py --model output/autoencoder.h5 --index output/index.pickle 

# import the necessary packages
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from helper.load_custome_data import load_images_from_folder
from helper.load_custome_data import load_images_from_folderNII
from helper.hyperparameters import height, width
#from imutils import build_montages
from operator import itemgetter
from CBIR_GUINII import show_images
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import argparse
import pickle
import cv2
import os
import nibabel as nib

def show_slices(slices, folder):

	""" Function to display row of image slices """
	fig, axes = plt.subplots(1, len(slices))
	for i, slice in enumerate(slices):
		#axes[i].imshow(slice.T, cmap="gray", origin="lower")
		img_shape= slice.shape
		img = Image.fromarray(slice, 'RGB')
		np.array(slice).reshape(img_shape[0], img_shape[1], 3)
		axes.imshow(slice.T, cmap="gray", origin="lower")
		#axes.plot(slice.T, cmap="gray", origin="lower")
	    #plt.plot(slice.T) #, cmap="gray", origin="lower")
	plt.savefig((os.path.join(folder, 'TESTs.jpeg')))
	plt.close()

def euclidean(a, b):
	# compute and return the euclidean distance between two vectors
	return np.linalg.norm(a - b)

def perform_search(queryFeatures, index, maxResults=64):
	# initialize our list of results
	results = []

	# loop over our index
	for i in range(0, len(index["features"])):
		# compute the euclidean distance between our query features
		# and the features for the current image in our index, then
		# update our results list with a 2-tuple consisting of the
		# computed distance and the index of the image
		d = euclidean(queryFeatures, index["features"][i])
		results.append((d, i))

	# sort the results and grab the top ones
	results = sorted(results) #[:maxResults]
	print(np.array(results).shape)

	# return the list of results
	return results

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=True,
	help="path to trained autoencoder")
ap.add_argument("-i", "--index", type=str, required=True,
	help="path to features index file")
ap.add_argument("-s", "--sample", type=int, default=10,
	help="# of testing queries to perform")
args = vars(ap.parse_args())

# load the dataset
print("[INFO] loading dataset...")
path = '/home/azureuser/PycharmProjects/WP3/'
#image_data = load_images_from_folder('dataset/', shuffle=False, width = width, height = height)
subfolders = [ f.path for f in os.scandir(path+'MRISeq/IXItest/') if f.is_dir() ]
image_data = []
for folder in subfolders :

	image_data1, filenames = load_images_from_folder(folder, shuffle=True, width = width, height = height)
	image_data.append(image_data1) #[*image_data, *image_data1] #image_data + image_data1

image_data = [item for sublist in image_data for item in sublist]
image_data = np.array(image_data)

x_train,x_test = train_test_split(image_data,test_size=0.3, shuffle = True)


trainX =  image_data
testX = image_data#[100:]

# add a channel dimension to every image in the dataset, then scale
# the pixel intensities to the range [0, 1]
# trainX = np.expand_dims(trainX, axis=-1)
# testX = np.expand_dims(testX, axis=-1)
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

# load the autoencoder model and index from disk
print("[INFO] loading autoencoder and index...")
autoencoder = load_model(args["model"])
index = pickle.loads(open(args["index"], "rb").read())

# create the encoder model which consists of *just* the encoder
# portion of the autoencoder
encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)

# quantify the contents of our input testing images using the encoder
print("[INFO] encoding testing images...")
features = encoder.predict(testX)

# randomly sample a set of testing query image indexes
queryIdxs = list(range(0, testX.shape[0]))
queryIdxs = np.random.choice(queryIdxs, size=args["sample"],
	replace=False)
# loop over the testing indexes
for i in queryIdxs:
	# take the features for the current image, find all similar
	# images in our dataset, and then initialize our list of result
	# images
	queryFeatures = features[i]
	results = perform_search(queryFeatures, index) #, maxResults=40)
	images = []
	images_names = []
	resmax = max(results, key=itemgetter(1))[0]
	resmin = min(results, key=itemgetter(1))[0]
	threshold = (resmax + resmin) / 2
	# loop over the results
	my_list = []
	with open(path + 'results' + str(i) + '.txt', 'w') as f:
		for (d, j) in results:
			# grab the result image, convert it back to the range
			# [0, 255], and then update the images list

			if d <= threshold:
				names = index["filenames"]
				names = [item for sublist in names for item in sublist]
				#names = np.array(names)
				name = names[j]
				#img = cv2.imread(name)
				img = nib.load(name)

				if img is not None:
					img_data = img.get_fdata()
					number_frames = img_data.shape
					ms0 = (number_frames[0]) / 2
					ms1 = (number_frames[1]) / 2
					ms2 = (number_frames[2]) / 2
					slice_0 = img_data[int(ms0), :, :]
					slice_1 = img_data[:, int(ms1), :]
					slice_2 = img_data[:, :, int(ms2)]
					img = Image.fromarray(slice_2, 'RGB')
					#show_slices([slice_2], 'MRI/')
					image = img.resize((width, height))

					#img = cv2.imread(path+'MRI/TESTs.jpeg')

				images_names.append(name)


				f.write('query' + str(name) + 'score ' + str(d) + '\n')

				#image = cv2.resize(img, (width, height))

				#image = (trainX[j] * 255).astype("uint8")
				image = np.dstack([image])
				images.append(image)
	f.close()
	# display the query image
	query = (testX[i] * 255).astype("uint8")
	show_images(images_names, query)
	'''
	cv2.imshow("Query", query)
	print(np.array(images).shape)
	# build a montage from the results and display it
	montage = build_montages(images, (40, 40), (20, 40))[0]
	cv2.imshow("Results", montage)
	cv2.waitKey(0)'''