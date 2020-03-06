from nmslib_viz import file_manager, nmslib, pca, plot
from nmslib_viz.config import ERROR_FILE_NOT_EXISTS, ERROR_NUMBER_POINTS, NUMBER_POINTS


def view(nmslib_index_file_path: str, number_points: int = NUMBER_POINTS):
    """
    Main function for visualizing an NMSLIB index given its file path.
    :param nmslib_index_file_path: File path pointing to a NMSLIB index.
    :param number_points: Number of points as a maximum to plot from the NMSLIB index data.
    :return: Index being visualized.
    """
    try:
        # Check if the file exists
        file_exists: bool = file_manager.exists(nmslib_index_file_path)
        if not file_exists:
            print(f'error: {ERROR_FILE_NOT_EXISTS}')
            return
        # Check number of points
        if number_points <= 0:
            print(f'error: {ERROR_NUMBER_POINTS}')
            return
        # Load index
        print('info: Loading index...')
        index_instance = nmslib.load_index(nmslib_index_file_path)
        if file_exists is None:
            return
        # Build data set
        print('info: Building data set...')
        data_set = nmslib.build_data_set(index_instance)
        # PCA fit-transform
        print('info: PCA fit-transforming...')
        data_set = pca.reduce(data_set)
        if data_set is None:
            return
        # Plot
        print('info: Plotting data...')
        plot.show(data_set, number_points)
    except Exception as e:
        print(f'error: Unexpected error occurred: [{e}]')
    finally:
        print('info: Done!')
