# USAGE
# python train_autoencoder.py --model output/autoencoder.h5 --vis output/recon_vis.png --plot output/plot.png


# set the matplotlib backend so figures can be saved in the background
#--model /home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/output/autoencoderMRI.json --vis /home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/output/vis.png --plot /home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/output/plot.png
import tensorflow as tf
import matplotlib
import os
import pickle
matplotlib.use("Agg")


# import the necessary packages
from sklearn.model_selection import train_test_split
from helper.convautoencoderMRI import ConvAutoencoder
from helper.load_custome_data import load_images_from_folder
from helper.load_custome_data import load_images_from_folderNII
from helper.hyperparameters import height, width
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

def visualize_predictions(decoded, gt, samples=10):
	# initialize our list of output images
	outputs = None

	# loop over our number of output samples
	for i in range(0, samples):
		# grab the original image and reconstructed image
		original = (gt[i] * 255).astype("uint8")
		recon = (decoded[i] * 255).astype("uint8")

		# stack the original and reconstructed image side-by-side
		output = np.hstack([original, recon])

		# if the outputs array is empty, initialize it as the current
		# side-by-side image display
		if outputs is None:
			outputs = output

		# otherwise, vertically stack the outputs
		else:
			outputs = np.vstack([outputs, output])

	# return the output images
	return outputs

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
project_path = '/Users/esmamansouri/PycharmProjects/WP3_SMI/'

path = '/Users/esmamansouri/Downloads/archive/'
ap.add_argument("-m", "--model", type=str, required=False, default = project_path+'autoencoderBodyParts.h5',
	help="path to output trained autoencoder")
ap.add_argument("-v", "--vis", type=str,  default = '/output/recon_visBP.png',
	help="path to output reconstruction visualization file")
ap.add_argument("-p", "--plot", type=str,  default = '/output/plotBP.png',
	help="path to output plot file")

# initialize the number of epochs to train for, initial learning rate,
# and batch size
EPOCHS = 25
INIT_LR = 1e-3
BS = 20#20


# load the  dataset
print("[INFO] loading dataset...")
subfolders = [ f.path for f in os.scandir(path+'archive/') if f.is_dir() ]
image_data = []
labels_names = []
labels = []
for folder in subfolders :

	print(folder)

	image_data1, filenames = load_images_from_folder(folder, shuffle=True, width = width, height = height)
	if 'DTI' in folder or 'MRA' in folder or 'PD' in folder:
			image_data1 = image_data1[:530]
			filenames = filenames[:530]
	image_data.append(image_data1) #[*image_data, *image_data1] #image_data + image_data1
	labels_names.append([folder[len(path + 'archive'):]] * len(image_data1))
	labels.append(folder[len(path + 'archive/'):])

labels_names = [item for sublist in labels_names for item in sublist]

y_dense =labels_names


image_data = [item for sublist in image_data for item in sublist]
image_data = np.array(image_data)
#x_train,x_test=train_test_split(image_data,test_size=0.20)
x_train, x_test, y_train, y_test = train_test_split(image_data, y_dense, test_size=0.10) #, stratify = y_dense)
trainX = x_train #image_data[100:]
testX = x_test #image_data[:100]

# add a channel dimension to every image in the dataset, then scale
# the pixel intensities to the range [0, 1]
#trainX = np.expand_dims(trainX, axis=-1)
#testX = np.expand_dims(testX, axis=-1)
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

# construct our convolutional autoencoder
print("[INFO] building autoencoder...")
autoencoder = ConvAutoencoder.build(width, height, depth=3, latentDim=250) #100)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
autoencoder.compile(loss="mse", optimizer=opt ) #opt) #mse

autoencoder.summary()

# train the convolutional autoencoder
H = autoencoder.fit(
	trainX, trainX,
	validation_data=(testX, testX),
	epochs=EPOCHS,
	batch_size=BS)

# use the convolutional autoencoder to make predictions on the
# testing images, construct the visualization, and then save it
# to disk
print("[INFO] making predictions...")
decoded = autoencoder.predict(testX)
vis = visualize_predictions(decoded, testX)
cv2.imwrite(args["vis"], vis)

# construct a plot that plots and saves the training history
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig(args["plot"])

# serialize the autoencoder model to disk
print("[INFO] saving autoencoder...")
name = args["model"]
model_json = autoencoder.to_json()


with open(name, "w") as json_file:
    json_file.write(model_json)
#with open(name, 'wb') as file:
#    pickle.dump(autoencoder, file)
#tf.keras.models.save_model(autoencoder, name)
 #,protocol=None, fix_imports=True)
#autoencoder.save(args["model"]) #, save_format="tf")
