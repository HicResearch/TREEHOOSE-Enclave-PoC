'''
Original code from :
https://www.kaggle.com/donkeys/preprocessing-images-to-normalize-colors-and-sizes
'''
import math
import matplotlib.pyplot as plt
from collections.abc import Iterable
import pydicom
import numpy as np

def show_img(img_path, colormap = None, extra_brightness=0):
    ds = pydicom.dcmread(img_path)
    shape = ds.pixel_array.shape
    target = 255

    # Convert to float to avoid overflow or underflow losses.
    image_2d = ds.pixel_array.astype(float)
    img_data = image_2d
    print(f"data min: {img_data.min()}, max: {img_data.max()}")
    print(f'window center: {ds.WindowCenter}') #, rescale intercept: {ds.RescaleIntercept})
    multival = isinstance(ds.WindowCenter, Iterable)
    if multival:
        scale_center = -ds.WindowCenter[0]
    else:
        scale_center = -ds.WindowCenter
    intercept = scale_center+extra_brightness
    #intercept = scale_center + ds.RescaleIntercept + extra_brightness
    print(f"final intercept: {intercept}")
    image_2d += intercept
    print(f"after applying intercept, min: {image_2d.min()}, max: {image_2d.max()}")

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    print(f"after scaling to 0-255, min: {image_2d_scaled.min()}, max: {image_2d_scaled.max()}")

    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    #plt.figure(figsize=(12,8))
    #plt.imshow(image_2d_scaled, cmap=colormap)
    a1 = plt.subplot(2, 2, 1)
    plt.imshow(image_2d_scaled, cmap="gray")


    plt.show()
    return image_2d_scaled

#show_img(f'{DATA_DIR}/train/ID00011637202177653955184/1.dcm', colormap=plt.cm.bone) <-image 0 below
#show_img(f'{DATA_DIR}/train/ID00128637202219474716089/1.dcm', colormap=plt.cm.bone) #image 1
#show_img(files[0], colormap=plt.cm.bone) #image 2