""" FROM PYdicOm
==========================================================
Load CT slices and plot axial, sagittal and coronal images
==========================================================
This example illustrates loading multiple files, sorting them by slice
location, building a 3D image and reslicing it in different planes.
.. usage:
   reslice.py <glob>
   where <glob> refers to a set of DICOM image files.
   Example: python reslice.py "*.dcm". The quotes are needed to protect
   the glob from your system and leave it for the script.
.. note:
   Uses numpy and matplotlib.
   Tested using series 2 from here
   http://www.pcir.org/researchers/54879843_20060101.html
"""

import pydicom
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import os
from Normalise_slices import show_img

# load the DICOM files
files = []
path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/DICOM/ffa0037427_sorted/ffa0037427/20100517/anonymous'
subjects_folders = [f.path for f in os.scandir(path) if f.is_dir() ]
slice_size = 512

#print('glob: {}'.format(sys.argv[1]))
for folder in subjects_folders :
    files =[]
    for fname in os.listdir(folder):
        print("loading: {}".format(fname))
        #dicom_image = show_img(folder+'/'+fname)
        files.append(pydicom.dcmread(folder+'/'+fname))


    print("file count: {}".format(len(files)))

    # skip files with no SliceLocation (eg scout views)
    slices = []
    skipcount = 0
    for f in files:
        if hasattr(f, 'SliceLocation'):
            slices.append(f)
        else:
            skipcount = skipcount + 1

    print("skipped, no SliceLocation: {}".format(skipcount))

    # ensure they are in the correct order
    slices = sorted(slices, key=lambda s: s.SliceLocation)

    # pixel aspects, assuming all slices are the same
    ps = slices[0].PixelSpacing
    ss = slices[0].SliceThickness
    ax_aspect = ps[1]/ps[0]
    sag_aspect = ps[1]/ss
    cor_aspect = ss/ps[0]

    # create 3D array
    img_shape = list(slices[0].pixel_array.shape)
    img_shape.append(len(slices))
    img3d = np.zeros(img_shape)

    # fill 3D array with the images from the files
    for i, s in enumerate(slices):
        img2d = s.pixel_array
        #img2d = np.resize(img2d, (slice_size,slice_size))
        img3d[:, :, i] = img2d


    # plot 3 orthogonal slices
    a1 = plt.subplot(2, 2, 1)
    plt.imshow(img3d[:, :, img_shape[2]//2],cmap="gray") #, origin="lower")
    a1.set_aspect(ax_aspect)


    '''a2 = plt.subplot(2, 2, 2)

    plt.imshow(img3d[:, img_shape[1] // 2, :], cmap="gray")  # , origin="lower")
    a2.set_aspect(sag_aspect)'''
    plt.axis('off')
    #save midlsice axial
    plt.savefig((os.path.join(path, fname + '.jpeg')), bbox_inches='tight')

    '''a3 = plt.subplot(2, 2, 3)
    plt.imshow(img3d[img_shape[0]//2, :, :],cmap="gray")#, origin="lower")
    a3.set_aspect(cor_aspect)'''

    #plt.show()