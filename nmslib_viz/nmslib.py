import nmslib

from nmslib_viz.config import NMSLIB_METRIC, NMSLIB_METHOD, NMSLIB_QUERY_TIME_EF_SEARCH, ERROR_FILE_NOT_EXISTS


def load_index(file_path: str):
    try:
        index_instance = nmslib.init(space=NMSLIB_METRIC, method=NMSLIB_METHOD)
        index_instance.loadIndex(file_path)
        index_instance.setQueryTimeParams(params={'efSearch': NMSLIB_QUERY_TIME_EF_SEARCH})
        return index_instance
    except Exception as e:
        print(f'error: {ERROR_FILE_NOT_EXISTS} - {e}')
        return None
