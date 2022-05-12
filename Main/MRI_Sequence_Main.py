#### main interface for running classifier to classify MRI sequence types into (T1, T2, PD, MRA, DTI)
## The script first calls an autoencoder to extract features from mRI images (mid-slice)
## SVM is used to classify sequence type
## Author : Esma Mansouri-Benssassi February 2022
## script is run as follow through the command line
# python MRI_Sequence_Main.py --model output/autoencoder.h5 --vis output/recon_vis.png --plot output/plot.png
# import the necessary packages
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from helper.load_custome_data import load_images_from_folder
from helper.load_custome_data import load_images_from_folderNII
from helper.hyperparameters import height, width
import imutils
#from imutils import  build_montage

from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from operator import itemgetter
from tkinter_UI import show_images
#from CBIR_GUI import show_images
import numpy as np
import argparse
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-m", "--model", type=str, required=True,
	help="path to trained autoencoder")

ap.add_argument("-s", "--svm", type=str, required=True,
	help="path to trained svm model")

ap.add_argument("-d", "--datasource", type=str, required=True,
	help="path to data to be classified")


ap.add_argument("-r", "--result", type=str, required=True,
	help="path to results file ")
args = vars(ap.parse_args())


# now get data for classification
path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/'
subfolders = [ f.path for f in os.scandir(path+'MRISeq/') if f.is_dir() ]
image_data = []
filenames = []
labels_names =[]
labels=[]
for folder in subfolders :

	if 'T1' in folder:
		image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width=width, height=height)
		if 'DTI' in folder:
			image_data1 = image_data1[:600]
			filenames1 = filenames1[:600]
		image_data.append(image_data1)  # [*image_data, *image_data1] #image_data + image_data1
		filenames.append(filenames1)
		labels_names.append([folder[len(path + 'MRISeq/IXI-'):]] * len(image_data1))
		labels.append(folder[len(path + 'MRISeq/'):])

# Load the autoencdoer for features extraction
autoencoder = load_model(args["model"])
index = pickle.loads(open(args["index"], "rb").read())


encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)


# extract feature for all chosen images
print("[INFO] encoding testing images...")
features = encoder.predict(data)

# now load the MRI sequence classifier and classify the chosen images
path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/'

clf1 = pickle.load(open(args['SVM'], 'rb'))# path+'MRI_Sequence_SVMClassifer.pkl', 'rb'))

#now save results in a table containing image file name and classification label )


