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
from tkinter_UI import show_images
#from CBIR_GUI import show_images
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
import numpy as np

import argparse
import pickle
import cv2
import os



ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=True,
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
path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/'
#image_data = load_images_from_folder('dataset/', shuffle=False, width = width, height = height)
#subfolders = [ f.path for f in os.scandir(path+'MRISeq/') if f.is_dir() ]
image_data = []
filenames = []



clf1 = pickle.load(open(path+'MRI_Sequence_SVMClassifer1.sav', 'rb'))

subfolders = [ f.path for f in os.scandir(path+'test/') if f.is_dir() ]
image_data = []
filenames = []
labels_names = []
labels = []
for folder in subfolders :

	image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width = width, height = height)
	image_data.append(image_data1) #[*image_data, *image_data1] #image_data + image_data1
	filenames.append(filenames1)
	labels_names.append([folder[len(path+'test/'):]] * len(image_data1))
	labels.append(folder[len(path+'test/'):])

# make the labels into classes  y
labels_names = [item for sublist in labels_names for item in sublist]

#y_dense = lb.fit_transform(labels_names)  #fit_transform

#y_dense = LabelBinarizer.fit(labels_names)

image_data = [item for sublist in image_data for item in sublist]
filenames = [item for sublist in filenames for item in sublist]
image_data = np.array(image_data)


# add a channel dimension to every image in the dataset, then scale
# the pixel intensities to the range [0, 1]
# trainX = np.expand_dims(trainX, axis=-1)
# testX = np.expand_dims(testX, axis=-1)
image_data = image_data.astype("float32") / 255.0



print("[INFO] loading autoencoder and index...")
json_file = open(args["model"], 'r')
loaded_model_json = json_file.read()
json_file.close()
autoencoder = model_from_json(loaded_model_json)


# create the encoder model which consists of *just* the encoder
# portion of the autoencoder
encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)

# quantify the contents of our input testing images using the encoder
print("[INFO] encoding testing images...")



# quantify the contents of our input testing images using the encoder
print("[INFO] encoding testing images...")
features_train = encoder.predict(image_data)


#now train the classifier
# TRAIN SVM LEARNING ALGORITHM
#clf = SVC(kernel='linear')
#clf = clf.fit(features_train, y_train)








predictions = clf1.predict(features_train)
#acc = accuracy_score(y_test, predictions)

print(predictions)


'''plt.scatter(X1[:,0], X1[:,1], color='r')
plt.scatter(X2[:,0], X2[:,1], color='b')
plt.scatter(X3[:,0], X3[:,1], color='y')
plt.contourf(xx,yy,Z,cmap=plt.cm.coolwarm, alpha=0.8)
plt.title("SVM With Linear Kernel and Three Labels (0, 1, 2)")
plt.show()'''