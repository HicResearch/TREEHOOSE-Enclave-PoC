import matplotlib.pyplot as plt
import cv2 as cv2
import os
import numpy as np
import nibabel as nib
import pydicom
from PIL import Image
nib.openers.Opener.default_compresslevel = 9


def show_slices(slices, folder, filename):

    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        #axes[i].imshow(slice.T, cmap="gray", origin="lower")
        axes.imshow(slice.T, cmap="gray", origin="lower")
    plt.axis('off')
    plt.savefig((os.path.join(folder, filename+'.jpeg')),bbox_inches='tight')
    plt.close()
    plt.show()

def load_images_from_folder(folder, width, height, shuffle=False):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        if 'nii' not in filename:
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                fname = os.path.join(folder,filename)
                img = cv2.resize(img, (width, height))
                images.append(img)
                filenames.append(fname)
    images = np.array(images)
    if shuffle:
    	np.random.shuffle(images)
    return images, filenames


def load_images_from_folderNII(folder, width, height, shuffle=True):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        print(filename)
        if 'jpeg' in filename or 'MRA' in folder  : #or 'PD' in folder or 'T2' in folder or 'jpeg' in filename:

            #do nothin
            t = 0
        else:

            img = nib.load(os.path.join(folder, filename))

            if img is not None:
                img_data = img.get_fdata()
                '''number_frames = img_data.shape
                ms0 = (number_frames[0]) / 2
                ms1 = (number_frames[1]) / 2
                ms2 = (number_frames[2]) / 2
                slice_0 = img_data[int(ms0), :, :]
                slice_1 = img_data[:, int(ms1), :]
                slice_2 = img_data[:, :, int(ms2)]
                slice_2 = img_data[:, :, int(ms2)]
                show_slices([slice_2], folder,filename[:-7])'''

                #cv2.imwrite(os.path.join(folder, 'TEST0.jpeg'), slice_0)
                #cv2.imwrite(os.path.join(folder, 'TEST1.jpeg'), slice_1)
                #cv2.imwrite(os.path.join(folder, 'TEST2.jpeg'), slice_2)

                number_frames = img_data.shape
                midslicenumber = (number_frames[1]) / 2
                midslice = img_data[:,int(midslicenumber),:]
                ###midslice = img_data[int(midslicenumber), :, :]
                #midslice = img_data[:,:,int(midslicenumber)]
                h, w = midslice.shape





                #cArray1 = cv2.CreateMat(h, w, cv2.CV_32FC3)
                #cArray2 = cv2.fromarray(midslice)

                #midslice= np.uint8(midslice)

                #midslice = cv2.cvtColor(midslice, cv2.COLOR_BGR2RGB)



                #image = cv2.resize(midslice, (width, height))
                ### only use when all images are extracted midlisce midslice = cv2.imread(os.path.join(folder, filename))
                midslice = cv2.resize(midslice, (width, height))

                show_slices([midslice], folder, filename[:-7])

                #cv2.imwrite(os.path.join(folder, filename[:-7]) + '.png', midslice)
                #image = cv2.resize(midslice, (width, height))
                #midslice = image #midsliece = np.resize(midsliece, (width, height,3))
                fname = os.path.join(folder, filename)
                print(fname)#img = cv2.resize(img, (width, height))
                images.append(midslice) #img)
                filenames.append(fname)
    images = np.array(images)
    if shuffle:
    	np.random.shuffle(images)
    return images, filenames



def load_images_from_folderDICOM(folder, width, height, shuffle=True):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        print(filename)
        if 'jpeg' in filename or 'MRA' in folder  : #or 'PD' in folder or 'T2' in folder or 'jpeg' in filename:

            #do nothin
            t = 0
        else:

            img = nib.load(os.path.join(folder, filename))

            if img is not None:
                img_data = img.get_fdata()
                '''number_frames = img_data.shape
                ms0 = (number_frames[0]) / 2
                ms1 = (number_frames[1]) / 2
                ms2 = (number_frames[2]) / 2
                slice_0 = img_data[int(ms0), :, :]
                slice_1 = img_data[:, int(ms1), :]
                slice_2 = img_data[:, :, int(ms2)]
                slice_2 = img_data[:, :, int(ms2)]
                show_slices([slice_2], folder,filename[:-7])'''

                #cv2.imwrite(os.path.join(folder, 'TEST0.jpeg'), slice_0)
                #cv2.imwrite(os.path.join(folder, 'TEST1.jpeg'), slice_1)
                #cv2.imwrite(os.path.join(folder, 'TEST2.jpeg'), slice_2)

                number_frames = img_data.shape
                midslicenumber = (number_frames[1]) / 2
                midslice = img_data[:,int(midslicenumber),:]
                ###midslice = img_data[int(midslicenumber), :, :]
                #midslice = img_data[:,:,int(midslicenumber)]
                h, w = midslice.shape



                show_slices([midslice], folder, filename[:-7])

                #cArray1 = cv2.CreateMat(h, w, cv2.CV_32FC3)
                #cArray2 = cv2.fromarray(midslice)

                #midslice= np.uint8(midslice)

                #midslice = cv2.cvtColor(midslice, cv2.COLOR_BGR2RGB)



                #image = cv2.resize(midslice, (width, height))
                ### only use when all images are extracted midlisce midslice = cv2.imread(os.path.join(folder, filename))
                midslice = cv2.resize(midslice, (width, height))
                #cv2.imwrite(os.path.join(folder, filename[:-7]) + '.png', midslice)
                #image = cv2.resize(midslice, (width, height))
                #midslice = image #midsliece = np.resize(midsliece, (width, height,3))
                fname = os.path.join(folder, filename)
                print(fname)#img = cv2.resize(img, (width, height))
                images.append(midslice) #img)
                filenames.append(fname)
    images = np.array(images)
    if shuffle:
    	np.random.shuffle(images)
    return images, filenames
