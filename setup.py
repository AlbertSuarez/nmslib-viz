import setuptools


with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='nmslib-viz',
    version='0.1',
    author='AlbertSuarez',
    author_email='alsumo95@gmail.com',
    description='NMSLIB visualization tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlbertSuarez/nmslib-viz',
    license='Apache-2.0',
    packages=['nmslib_viz'],
    install_requires=[
        'tqdm==4.43.0',
        'nmslib==2.0.5',
        'networkx==2.4',
        'matplotlib==3.1.3'
    ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    keywords='nmslib visualization graph',
    scripts=['bin/nmslib-viz']
 )
