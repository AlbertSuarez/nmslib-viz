# Parameters
VIEW_DIMENSIONS: int = 3
NUMBER_POINTS: int = 1000

# Argument helper
HELP_NMSLIB_INDEX_FILE_PATH = 'String pointing to the NMSLIB file path. ' \
                              'There has to be the additional .dat file for the index, the one that is created when ' \
                              'uses the `save_data=True` option in the saveIndex() function. For example: ' \
                              '`index.nmslib` and `index.nmslib.dat` need to exist but only `index.nmslib` has to be ' \
                              'provided as this parameter.'
HELP_NUMBER_POINTS = 'Number of points as a maximum to plot from the NMSLIB index data, where has to be 1 at least. ' \
                     f'Default value: {NUMBER_POINTS}.'

# Error messages
ERROR_FILE_NOT_EXISTS = 'File path provided do not point to an NMSLIB index. ' \
                        'Remember for visualizing an NMSLIB index, data from the index had to be saved when saving ' \
                        'the index using the `save_data=True` option in the saveIndex() function.'
ERROR_NUMBER_POINTS = 'Number of points has to be at least 1.'
