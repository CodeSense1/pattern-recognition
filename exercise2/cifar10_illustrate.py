import pickle
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from time import sleep


def printRandomImageFromBatch(batch, labels):
    index = np.random.randint(0,high=999)
    pic1 = batch["data"][index]
    imgArray = np.reshape(pic1, (3,32,32))
    imgArray = np.transpose(imgArray, (1,2,0))

    # img = Image.fromarray(imgArray)
    num = batch["labels"][index]
    l = labels[num]
    plt.figure(1)
    plt.clf()
    plt.imshow(imgArray)
    plt.title(f"Image {index} label={l} num={num}")
    plt.show()

# Define your datasource here
# Note that this is the path to folder,
# individual batches are processed later
BASEPATH = "cifar-10-batches-py/"

# From CIFAR-10 documentation
def unpickle(file):
    path = BASEPATH + file
    with open(path, 'rb') as fo:
        d = pickle.load(fo, encoding="latin1")
    return d


batch = unpickle("data_batch_1")
labelNames = unpickle("batches.meta")["label_names"]


# Dict keys:
# b'batch_label'
# b'labels'
# b'data'
# b'filenames'

# Prints random image
printRandomImageFromBatch(batch, labelNames)
