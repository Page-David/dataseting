"""Dataset writing functions"""
import os

from . import dataset


def to_pngs(dst, folder_path, format_list, saver):
    """Write dataset to png images with given Dataset
    instance.

    Parameters
    ----------
    dst : Dataset
        An dataset that has images as its data attr.
    folder_path : str
        A directory that saves dataset.
    format_list : list
        A list that provides information on format filename
    saver : callable
        A function takes two arguments (path, image_in_1D_list)
        you can write that with your favoriate image process
        package (e.g., OpenCV, Pillow, matplotlib).
    """
    if not isinstance(dst, dataset.Dataset):
        raise TypeError('dst is not an Dataset type, but expected.')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if not os.path.isdir(folder_path):
        raise ValueError('Path {} exists but is not a directory'
                         .format(folder_path))

    if not isinstance(format_list, list):
        raise ValueError('Type of format_list shoud be list.')

    for k, item in enumerate(format_list):
        if not isinstance(item, (str, list)):
            raise ValueError('Format information in format_list should'
                             'either be str or list.')

        if isinstance(item, list):
            if not len(item) == dst.dataset_size:
                raise ValueError('List in format_list not match'
                                 'the dataset size.')
            try:
                format_list[k] = list(map(str, format_list[k]))
            except Exception:
                raise ValueError('Failed to convert element in list'
                                 'to str.')

    if not callable(saver):
        raise ValueError('saver should be a callable object.')

    for i in range(dst.dataset_size):
        _s = str()
        for key in format_list:
            if isinstance(key, str):
                _s = _s + key
            if isinstance(key, list):
                _s = _s + key[i]
        _s = _s + '.png'
        _s = os.path.join(folder_path, _s)

        saver(_s, dst.data[i])
