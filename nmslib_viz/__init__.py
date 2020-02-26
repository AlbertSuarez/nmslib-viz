from nmslib_viz import file_manager, nmslib
from nmslib_viz.config import VISUALIZE_MAXIMUM_NODES, ERROR_FILE_NOT_EXISTS


def view(nmslib_index_file_path: str, maximum_nodes: int = VISUALIZE_MAXIMUM_NODES):
    # Check if the file exists
    file_exists: bool = file_manager.exists(nmslib_index_file_path)
    if not file_exists:
        print(f'error: {ERROR_FILE_NOT_EXISTS}')
        return
    # Load index
    print('Loading index...')
    index_instance = nmslib.load_index(nmslib_index_file_path)
    if file_exists is None:
        return
    # Build graph
    print('Building graph...')
