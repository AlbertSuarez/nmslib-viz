import os


def exists(file_path: str):
    """
    Checks if the NMSLIB file exists and was saved with the data included.
    :param file_path: File path pointing to the NMSLIB index.
    :return: True if both nmslib index and their data exists, False otherwise.
    """
    index_exists: bool = os.path.isfile(file_path)
    index_data_exists: bool = os.path.isfile(f'{file_path}.dat')
    return index_exists and index_data_exists
