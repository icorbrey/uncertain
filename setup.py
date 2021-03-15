"""Sets up the `uncertain` module."""

from pathlib import Path
from setuptools import setup

here = Path(__file__).parent
readme = (here/'README.md').read_text()

setup(
    name='uncertain',
    version='1.0.0',
    description='Mathematically uncertain values for scientific applications.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/icorbrey/uncertain',
    author='Isaac Corbrey',
    author_email='icorbrey@gmail.com',
    license='MIT',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.7'],
    packages=['uncertain']
)
