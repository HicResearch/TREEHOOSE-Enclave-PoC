#

# This script is used to train SVM classifier for MRI sequence type identificaiton
# import the necessary packages
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from helper.load_custome_data import load_images_from_folder
from helper.load_custome_data import load_images_from_folderNII
from helper.hyperparameters import height, width

#from imutils import build_montages
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from operator import itemgetter

#from CBIR_GUI import show_images
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
import numpy as np

import argparse
import pickle
import cv2
import os

project_path = '/Users/esmamansouri/PycharmProjects/WP3_SMI/'
path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/' #'/home/ubuntu/studies/Pictures/Esma-User-Folder/'
path = '/Users/esmamansouri/DUNDEE/Dundee/WP3/Autoencoder-image-search-master/MRISeq/IXI/'

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=False, default = project_path+'output/autoencoderMRI.h5',
	help="path to trained autoencoder")
'''ap.add_argument("-i", "--index", type=str, required=True,
	help="path to features index file")
ap.add_argument("-s", "--sample", type=int, default=10,
	help="# of testing queries to perform")
args = vars(ap.parse_args())'''
args = vars(ap.parse_args())
# load the dataset
print("[INFO] loading dataset...")
#path = '/home/azureuser/PycharmProjects/WP3/'

project_path = '/Users/esmamansouri/PycharmProjects/WP3_SMI/'

path = '/Users/esmamansouri/DUNDEE/Dundee/WP3/Autoencoder-image-search-master/MRISeq/IXI/'
#image_data = load_images_from_folder('dataset/', shuffle=False, width = width, height = height)
subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
image_data = []
filenames = []



# get features
subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
image_data = []
filenames = []
labels_names = []
labels = []
for folder in subfolders :

	image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width = width, height = height)
	if 'DTI' in folder:
		image_data1 = image_data1[:540]
		filenames1 = filenames1[:540]
	image_data.append(image_data1) #[*image_data, *image_data1] #image_data + image_data1
	filenames.append(filenames1)
	labels_names.append([folder[len(path):]] * len(image_data1))
	labels.append(folder[len(path):])


# make the labels into classes  y
labels_names = [item for sublist in labels_names for item in sublist]
lb = LabelBinarizer()
y_dense =labels_names
#y_dense = lb.fit_transform(labels_names)  #fit_transform

#y_dense = LabelBinarizer.fit(labels_names)

image_data = [item for sublist in image_data for item in sublist]
filenames = [item for sublist in filenames for item in sublist]
image_data = np.array(image_data)
#x_train,x_test=train_test_split(image_data,test_size=0.40)
X_train, X_test, y_train, y_test = train_test_split(image_data, y_dense, test_size=0.20, stratify = y_dense) #, random_state=42)
trainX =  X_train # x_train
testX = X_test#[100:]

# add a channel dimension to every image in the dataset, then scale
# the pixel intensities to the range [0, 1]
# trainX = np.expand_dims(trainX, axis=-1)
# testX = np.expand_dims(testX, axis=-1)
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

# load the autoencoder model and index from disk
print("[INFO] loading autoencoder and index...")
'''json_file = open(args["model"], 'r')
loaded_model_json = json_file.read()
json_file.close()
autoencoder = model_from_json(loaded_model_json)'''
autoencoder = load_model(args["model"])

# create the encoder model which consists of *just* the encoder
# portion of the autoencoder
encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)

# quantify the contents of our input testing images using the encoder
print("[INFO] encoding testing images...")
features_train = encoder.predict(trainX)
features_test = encoder.predict(testX)

#now train the classifier
# TRAIN SVM LEARNING ALGORITHM
clf = SVC(kernel='rbf') #'linear')
clf = clf.fit(features_train, y_train)
predictions = clf.predict(features_test)
acc = accuracy_score(y_test, predictions) #, normalize=False)
#print(predictions)
#print(y_test)
print(acc)

with open(project_path+'/output/MRI_Sequence_SVMClassifer.pkl', 'wb') as f:
    pickle.dump(clf, f)
# create decision boundary plot
'''xx, yy = np.meshgrid(
    np.arange(-10, 10, 0.2),
    np.arange(-10, 10, 0.2))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)'''
