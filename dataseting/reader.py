#!/usr/bin/env python3
"""Dataset reading functions."""
import gzip
import struct
import array

import dataset


def from_mnist_like(img_file, label_file, img_magic=2051, label_magic=2049):
    """Load dataset from mnist like .gz file.

    Parameters
    ----------
    img_file : str
        filepath to the .gz file with image.
    label_file : str
        filepath to the .gz file with labels.
    img_magic : int, default=2051
        magic number of image .gz file.
    label_magic : int, default=2049
        magic number of labels .gz file.

    Returns
    -------
    dataset : ImgClassifyDataset
        An instance of ImgClassifyDataset that contains
        dataset information.
    """
    with gzip.open(img_file, 'rb') as i_file:
        i_magic, i_nums, rows, cols = struct.unpack('>IIII', i_file.read(16))

        if i_magic is not img_magic:
            raise ValueError('Magic number of image data not match,'
                             'expect {} but got {}.'.format(img_magic,
                                                            i_magic))

        imgs = array.array('B', i_file.read())
        images = list()
        for i in range(i_nums):
            images.append(imgs[i * rows * cols: (i + 1) * rows * cols])

    with gzip.open(label_file, 'rb') as l_file:
        l_magic, l_nums = struct.unpack('>II', l_file.read(8))

        if l_magic is not label_magic:
            raise ValueError('Magic number of label data not match,'
                             'expect {} but got {}.'.format(label_magic,
                                                            l_magic))
        labels = list(array.array('B', l_file.read()))

    if not i_nums == l_nums:
        pass

    dst = dataset.ImgClassifyDataset()
    dst.dataset_size = i_nums
    dst.data = images
    dst.labels = labels

    return dst
