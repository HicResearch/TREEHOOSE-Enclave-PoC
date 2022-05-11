# USAGE
# python index_images.py --model output/autoencoder.h5 --index output/index.pickle

# import the necessary packages
from tensorflow.keras.models import Model
import os
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model
from helper.load_custome_data import load_images_from_folder
from helper.load_custome_data import load_images_from_folderNII
from helper.hyperparameters import height, width
import numpy as np
import argparse
import pickle

#path = '/home/azureuser/PycharmProjects/WP3/'

path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/'
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=True,
	help="path to trained autoencoder")
ap.add_argument("-i", "--index", type=str, required=True,
	help="path to output features index file")
args = vars(ap.parse_args())

# load the MNIST dataset
print("[INFO] loading training split...")
#trainX = load_images_from_folder('Med/', shuffle=False, width = width, height = height)

subfolders = [ f.path for f in os.scandir(path+'MRISeq/') if f.is_dir() ]
image_data = []
filenames = []
for folder in subfolders :

	image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width = width, height = height)
	if 'DTI' in folder:
		image_data1 = image_data1[:600]
		filenames1 = filenames1[:600]
	image_data.append(image_data1) #[*image_data, *image_data1] #image_data + image_data1
	filenames.append(filenames1)

image_data = [item for sublist in image_data for item in sublist]
filenames = [item for sublist in filenames for item in sublist]
image_data = np.array(image_data)
trainX = image_data

# add a channel dimension to every image in the training split, then
# scale the pixel intensities to the range [0, 1]
# trainX = np.expand_dims(trainX, axis=-1)
trainX = trainX.astype("float32") / 255.0

#new_model = load_model(args["model"])

# load our autoencoder from disk
print("[INFO] loading autoencoder model...")
'''json_file = open(args["model"], 'r')
loaded_model_json = json_file.read()
json_file.close()
autoencoder = model_from_json(loaded_model_json)'''
autoencoder = load_model(args["model"])

# create the encoder model which consists of *just* the encoder
# portion of the autoencoder
encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)

# quantify the contents of our input images using the encoder
print("[INFO] encoding images...")
features = encoder.predict(trainX)
print(features.shape)

# construct a dictionary that maps the index of the training
# image to its corresponding latent-space representation
indexes = list(range(0, trainX.shape[0]))


data = {"indexes": indexes, "features": features, "images": trainX, "filenames": filenames}

# write the data dictionary to disk
print("[INFO] saving index...")
f = open(args["index"], "wb")
f.write(pickle.dumps(data))
f.close()