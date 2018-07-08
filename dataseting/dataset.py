#!/usr/bin/env python3
"""Different datasets structures are defined here."""


class Dataset(object):
    """A brief framework of each dataset"""

    def __init__(self, dataset_size):
        """Basic variables in dataset class"""
        self.dataset_size = dataset_size
        self._data = list()
        self._label = list()

    def concatence(self):
        """Method used to concatence two datasets."""
        pass

    @property
    def data(self):
        """Data in dataset."""
        pass

    @property
    def label(self):
        """Labels in dataset."""
        pass

    def transform_data(self):
        """Method used to transform dataset data
        with given function.
        """
        pass

    def transform_labels(self):
        """Method used to transform dataset labels
        with given function.
        """
        pass


class ImgClassifyDataset(Dataset):
    """This dataset structure type is suitbale for problems
    that classify images into different types. For example, mnist
    dataset, coil-20 dataset, etc.
    """

    def __init__(self, *args, **kwargs):
        Dataset.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Data reader in ImgClassifyDataset."""
        return self._data

    @data.setter
    def data(self, data):
        """Data setter in ImgClassifyDataset."""
        if not len(data) == self.dataset_size:
            raise ValueError('Data list length not equals to dataset_size.')

        if not isinstance(data, list):
            raise ValueError('data should be a list.')

        for i in range(self.dataset_size):
            if not isinstance(self.data[i], list):
                raise ValueError('The image in data at index {}'
                                 'is not a list.'.format(i))
            inst_mapping = list(map(lambda x: isinstance(x, (float, int))))

            if False in inst_mapping:
                raise ValueError('There is a pixcel in {}th image and indexed'
                                 '{} is not an instance of int or float.'
                                 .format(i, inst_mapping.index(False)))

        self._data = data

    @property
    def label(self):
        """Label reader in ImgClassifyDataset."""
        return self._label

    @label.setter
    def label(self):
        """Label setter in ImgClassifyDataset."""
