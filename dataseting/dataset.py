"""Different datasets structures are defined here."""


class Dataset(object):
    """A brief framework of each dataset"""

    def __init__(self, dataset_size):
        """Basic variables in dataset class"""
        self.dataset_size = dataset_size
        self._data = list()
        self._label = list()
        self.data_prop = dict()
        self.valid_data_prop = list()
        self._batch_index = 0

    def concatence(self):
        """Method used to concatence two datasets."""
        pass

    @property
    def data(self):
        """Data in dataset."""
        pass

    def get_data_prop(self):
        """Get some extra data static information for further analyse."""
        pass

    @property
    def label(self):
        """Labels in dataset."""
        pass

    def batches_generator(self, batch_size, cut_tail=False):
        """A generator produce small batches in one epoch."""
        if not self.data or not self.label:
            raise ValueError('Data or label has not set in this dataset.')

        if not isinstance(batch_size, int):
            raise ValueError('batch_size should be an int.')

        if batch_size > self.dataset_size:
            raise ValueError('Batch size should be less than dataset size.')

        _flag = True

        while _flag:
            if batch_size + self._batch_index < self.dataset_size:
                _start = self._batch_index
                _end = batch_size + self._batch_index
                self._batch_index = self._batch_index + batch_size
            elif batch_size + self._batch_index == self.dataset_size:
                _start = self._batch_index
                _end = None
                self._batch_index = 0
            else:
                if cut_tail is True:
                    return
                else:
                    _start = self._batch_index
                    _end = None
                _flag = False

            yield self.data[_start: _end], self.label[_start: _end]

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
        if not isinstance(data, list):
            raise ValueError('data should be a list.')

        if not len(data) == self.dataset_size:
            raise ValueError('Data list length not equals to dataset_size.')

        for i in range(self.dataset_size):
            if not isinstance(data[i], list):
                raise ValueError('The image in data at index {}'
                                 'is not a list.'.format(i))
            inst_mapping = list(map(lambda x: isinstance(x, (float, int)),
                                    data[i]))

            if False in inst_mapping:
                raise ValueError('There is a pixcel in {}th image and indexed '
                                 '{} is not an instance of int or float.'
                                 .format(i, inst_mapping.index(False)))

        self._data = data
        if self.label:
            self.get_data_prop()

    @property
    def label(self):
        """Label reader in ImgClassifyDataset."""
        return self._label

    @label.setter
    def label(self, label):
        """Label setter in ImgClassifyDataset."""
        if not isinstance(label, list):
            raise ValueError('label should be a list.')

        if not len(label) == self.dataset_size:
            raise ValueError('Label list length not equals to dataset_size.')

        self._label = label
        if self.data:
            self.get_data_prop()

    def get_data_prop(self):
        """Get extra properties for each image"""
        if not self._data:
            raise ValueError('Data in this set is not set yet.')

        if not self._label:
            raise ValueError('Label in this et is not set yet.')

        _uni_labels = list(set(self.label))
        _count = dict((l, 0) for l in _uni_labels)
        cls_count = list()

        for i in self.label:
            _count[self.label[i]] = _count[self.label[i]] + 1
            cls_count.append(_count[self.label[i]])

        self.valid_data_prop.append('count_by_class')
        self.data_prop['count_by_class'] = cls_count
