import numpy as np
import pickle
import os
from random import choice


class Classifier:
    """ Classifier that is used throughout the rest of the 
        Pattern recognition and machine learning course

        Later on more prediction methods will be implemented here
    """

    def __init__(self):
        self.Xtr = []
        self.ytr = []

    def train(self, X, y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        # At this point the classifier simply remembers all the training data
        # No actual learning just yet
        self.Xtr = X
        self.ytr = y

    def cifar10_classifier_random(self, X):
        """ Returns randomly chosen label. This is considered to be the 'worst'
            possible classifier. 
        """
        return choice(self.ytr)

    def cifar10_classifier_1nn(self, X):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]

        print(num_test)
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)

        # loop over all test rows
        for i in range(num_test):
            print(i)
            # find the nearest training image to the i'th test image
            # using the euklidean distance
            distances = np.sum(np.power(self.Xtr - X[i, :], 2), axis=1)
            min_index = np.argmin(distances)
            Ypred[i] = self.ytr[min_index]
        return Ypred

    def class_acc(self, pred, gt):
        """ Evaluates classification accuracy. """
        return np.mean(pred == gt)


def load_CIFAR_batch(filename):
    """ load single batch of cifar """
    with open(filename, 'rb') as f:
        datadict = pickle.load(filename, encoding='latin1')
        X = datadict['data']
        Y = datadict['labels']
        X = X.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
        Y = np.array(Y)
        return X, Y


def load_CIFAR10(ROOT, batch_no=6):
    """ load all of cifar """
    xs = []
    ys = []
    for b in range(1, batch_no):
        f = os.path.join(ROOT, 'data_batch_%d' % (b, ))
        X, Y = load_CIFAR_batch(f)
        xs.append(X)
        ys.append(Y)
    Xtr = np.concatenate(xs)
    Ytr = np.concatenate(ys)
    del X, Y
    Xte, Yte = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))
    return Xtr, Ytr, Xte, Yte


Xtr, Ytr, Xte, Yte = load_CIFAR10('C:\\Users\\Joonas\\Desktop\\cifar-10-batches-py', 2)
# flatten out all images to be one-dimensional
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)  # Xtr_rows becomes 50000 x 3072
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)  # Xte_rows becomes 10000 x 3072

nn = Classifier()  # create a Nearest Neighbor classifier class
nn.train(Xtr_rows, Ytr)  # train the classifier on the training images and labels
Yte_predict = nn.cifar10_classifier_1nn(Xte_rows[0:10])  # predict labels on the test images
# and now print the classification accuracy, which is the average number
# of examples that are correctly predicted (i.e. label matches)

print(f'Accuracy: {nn.class_acc(Yte_predict, Yte[0:10])}')
