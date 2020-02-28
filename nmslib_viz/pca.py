import numpy as np

from sklearn.decomposition import PCA

from nmslib_viz.config import VIEW_DIMENSIONS


def reduce(data_set):
    """
    Reduce data set dimensionality to the use set up on the configuration.
    :param data_set: Numpy array representing the data set.
    :return: Data set dimensionality reduce to the desired dimensions.
    """
    try:
        print(f'info: reducing features from {data_set.shape[1]} to {VIEW_DIMENSIONS} dimensions...')
        pca_instance = PCA(n_components=VIEW_DIMENSIONS, svd_solver='full')
        # If number of samples is lower than dimensionality
        samples_amount: int = data_set.shape[0]
        if samples_amount < VIEW_DIMENSIONS:
            new_data_set = np.empty((VIEW_DIMENSIONS, data_set.shape[1]), dtype=data_set.dtype)
            new_data_set[:samples_amount] = data_set
            new_data_set[samples_amount:] = data_set[np.random.choice(range(samples_amount),
                                                                      size=VIEW_DIMENSIONS - samples_amount)]
            pca_instance.fit(new_data_set)
        else:
            pca_instance.fit(data_set)
        # Reducing dimensions
        features = pca_instance.transform(data_set)
        return features
    except Exception as e:
        print(f'error: Data set could not be dimensionality reduced to {VIEW_DIMENSIONS}: [{e}]')
        return None
