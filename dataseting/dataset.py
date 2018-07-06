#!/usr/bin/env python3
"""Different datasets structures are defined here."""


class Dataset(object):
    """A brief framework of each dataset"""

    def __init__(self):
        """Basic variables in dataset class"""
        self.dataset_size = int()
        self.data = list()
        self.labels = list()

    def concatence(self):
        """Method used to concatence two datasets."""
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
