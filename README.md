# NMSLIB-viz

[![HitCount](http://hits.dwyl.io/AlbertSuarez/nmslib-viz.svg)](http://hits.dwyl.io/AlbertSuarez/nmslib-viz)
[![PyPI version](https://badge.fury.io/py/nmslib-viz.svg)](https://pypi.org/project/nmslib-viz/)
![Python application](https://github.com/AlbertSuarez/searchly/workflows/Python%20application/badge.svg)
![Python package](https://github.com/AlbertSuarez/nmslib-viz/workflows/Python%20package/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/nmslib-viz.svg)](https://GitHub.com/AlbertSuarez/nmslib-viz/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/nmslib-viz.svg)](https://GitHub.com/AlbertSuarez/nmslib-viz/network/)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/nmslib-viz.svg)](https://GitHub.com/AlbertSuarez/nmslib-viz/graphs/contributors/)

📊 NMSLIB visualization tool

## Installation

Install client via pip. Ideally, `nmslib-viz` is well supported for Python >= 3.7.

```bash
pip3 install nmslib-viz --no-binary nmslib
```

> The `--no-binary` option is important for a better CPU performance.

## Usage

Just run it like this:

```bash
nmslib-viz INDEX_FILE_PATH [--number_points NUMBER_POINTS]
```

Arguments:

- `INDEX_FILE_PATH`: String pointing to the NMSLIB file path. There has to be the additional .dat file for the index, the one that is created when uses the `save_data=True` option in the saveIndex() function. For example: `index.nmslib` and `index.nmslib.dat` need to exist but only `index.nmslib` has to be provided as this parameter.
- `NUMBER_POINTS`: (optional) Number of points as a maximum to plot from the NMSLIB index data, where has to be 1 at least. Default value: 1000.

## Result

![Example](https://raw.githubusercontent.com/AlbertSuarez/nmslib-viz/master/docs/images/example.png)

> **Note**: this example is a representation of the [SearchLy](https://github.com/AlbertSuarez/searchly) index.

## Development

### Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

### Installation

1. Setup virtual environment

2. Install dependencies

  ```bash
  pip3 install -r requirements.lock
  ```

3. Install locally

  ```bash
  pip3 install . --no-binary nmslib
  ```
  

## Contributing

Suggestions, improvements, and enhancements are always welcome! If you have any issues, please do raise one in the Issues section. If you have an improvement, do file an issue to discuss the suggestion before creating a PR.

All ideas – no matter how outrageous – welcome!

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

Apache-2.0 © nmslib-viz
