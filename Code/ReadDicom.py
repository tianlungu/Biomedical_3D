# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pydicom as dicom
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import csv


# %%
folder_path1 = "/GTL/jupyter/ReadDICOM/Data/before/"
png_folder_path1 = "/GTL/jupyter/ReadDICOM/Data/before_picture/"
resize_folder_path1="/GTL/jupyter/ReadDICOM/Data/before_resize_picture/"
folder_path2 = "/GTL/jupyter/ReadDICOM/Data/after/"
png_folder_path2 = "/GTL/jupyter/ReadDICOM/Data/after_picture/"
resize_folder_path2="/GTL/jupyter/ReadDICOM/Data/after_resize_picture/"


# %%
def read_dicom(folder_path,png_folder_path):
    images_path = os.listdir(folder_path)
    for n, image in enumerate(images_path):
        if os.path.splitext(image)[-1] == ".dcm":
            ds = dicom.read_file(os.path.join(folder_path, image))
            pixel_array_numpy = ds.pixel_array
            pixel_array_numpy.astype(np.int16)
            image = image.replace('.dcm', '.png')
            outputImg = Image.fromarray(pixel_array_numpy)
            outputImg.convert('L')
            outputImg.save(os.path.join(png_folder_path, image))
            if n % 50 == 0:
                print('{} image converted'.format(n))


# %%
def read_dicom(folder_path,png_folder_path):
    images_path = os.listdir(folder_path)
    for n, image in enumerate(images_path):
        ds = dicom.read_file(os.path.join(folder_path, image))
        pixel_array_numpy = ds.pixel_array/255
        # pixel_array_numpy.astype('uint8')
        image = image.replace('.dcm', '.png')
        cv2.imwrite(os.path.join(png_folder_path, image),pixel_array_numpy)
        if n % 50 == 0:
            print('{} image converted'.format(n))


# %%
def img_resize(png_folder_path,resize_folder_path):
    images_path=os.listdir(png_folder_path)
    for n,image in enumerate(images_path):
        src = cv2.imread(os.path.join(png_folder_path, image), cv2.IMREAD_UNCHANGED)
        width = int(512)
        height = int(512)
        dsize = (width, height)
        output = cv2.resize(src, dsize)
        cv2.imwrite(os.path.join(resize_folder_path, image),output) 


# %%
scan_dicom=read_dicom(folder_path1,png_folder_path1)
img_resize(png_folder_path1,resize_folder_path1)



