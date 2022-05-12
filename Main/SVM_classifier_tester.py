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


from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
import numpy as np

import argparse
import pickle
import cv2
import os
import csv


project_path = 'C:/Users/cgao001/OneDrive - University of Dundee/HIC research/3 hic/TreeHoose-enclave/WP3_SMI-main/'

path = 'C:/Users/cgao001/OneDrive - University of Dundee/HIC research/3 hic/TreeHoose-enclave/Data/'



ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=False, default = project_path+'output/autoencoderMRI.h5',
	help="path to trained autoencoder")
ap.add_argument("-s", "--SVM", type=str, required=False, default = project_path+'output/MRI_Sequence_SVMClassifier.pkl',
	help="path to SVM index file")
'''ap.add_argument("-s", "--sample", type=int, default=10,
	help="# of testing queries to perform")'''
args = vars(ap.parse_args())
args = vars(ap.parse_args())
# load the dataset
print("[INFO] loading dataset...")
#path = '/home/azureuser/PycharmProjects/WP3/'




# get features

clf1 = pickle.load(open(args["SVM"], 'rb'))

subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
image_data = []
filenames = []
labels_names = []
labels = []
for folder in subfolders :

	image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width = width, height = height)
	image_data.append(image_data1) #[*image_data, *image_data1] #image_data + image_data1
	filenames.append(filenames1)
	labels_names.append([folder[len(path):]] * len(image_data1))
	labels.append(folder[len(path):])

# make the labels into classes  y
labels_names = [item for sublist in labels_names for item in sublist]
y_dense =labels_names
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




autoencoder = load_model(args["model"])

encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)

# quantify the contents of our input testing images using the encoder
print("[INFO] encoding testing images...")
features_train = encoder.predict(image_data)


#now train the classifier
# TRAIN SVM LEARNING ALGORITHM
#clf = SVC(kernel='linear')
#clf = clf.fit(features_train, y_train)





indexes = list(range(0, image_data.shape[0]))


predictions = clf1.predict(features_train)
acc = accuracy_score(y_dense, predictions)
print(acc)
#acc = accuracy_score(y_test, predictions)
data = { "predictions": predictions, "filenames": filenames}
print(predictions)
print(filenames)




'''with open(path+'MRI_Sequence_Results.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x

    w = csv.writer(f)
    w.writerow(data.keys())
    w.writerow(data.values())'''
field_names = ['index', 'predictions', 'filenames']
with open(project_path+'output/MRI_Sequence_Results.txt', 'w') as csvfile:
	'''writer = csv.writer(csvfile, fieldnames = field_names)
	writer.writeheader()
	writer.writerow(data.keys())
	writer.writerow(data.values())'''
    #writer.writerows(data)
	for key, values in zip(predictions,filenames):

		csvfile.write(key + ',' + values + '\n')
		#csvfile.write(f"{key},{','.join(values)}\n")
'''predictions = clf1.predict(features_test)
acc = accuracy_score(y_test, predictions)
print(acc)'''
# PLOT EVERYTHING
'''plt.scatter(X1[:,0], X1[:,1], color='r')
plt.scatter(X2[:,0], X2[:,1], color='b')
plt.scatter(X3[:,0], X3[:,1], color='y')
plt.contourf(xx,yy,Z,cmap=plt.cm.coolwarm, alpha=0.8)
plt.title("SVM With Linear Kernel and Three Labels (0, 1, 2)")
plt.show()'''