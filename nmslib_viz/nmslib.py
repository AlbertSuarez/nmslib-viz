import nmslib
import numpy as np

from nmslib_viz.config import ERROR_FILE_NOT_EXISTS


def load_index(file_path: str):
    """
    Load an NMSLIB index with the data included given their file path.
    :param file_path: File path pointing to the NMSLIB index.
    :return: NMSLIB index instance.
    """
    try:
        index_instance = nmslib.init()
        index_instance.loadIndex(file_path, load_data=True)
        return index_instance
    except Exception as e:
        print(f'error: {ERROR_FILE_NOT_EXISTS} - {e}')
        return None


def build_data_set(index_instance):
    """
    Build a Numpy array with all the points inside the given index instance.
    :param index_instance: NMSLIB index instance.
    :return: Numpy array with all the points representing the data set.
    """
    data_set: list = list()
    nodes_amount: int = nmslib.getDataPointQty(index_instance)
    print(f'info: {nodes_amount} nodes found.')
    for idx in range(nodes_amount):
        try:
            data_set.append(nmslib.getDataPoint(index_instance, idx))
        except Exception as e:
            print(f'warn: Node number {idx} could not be obtained: [{e}]')
    return np.array(data_set)
