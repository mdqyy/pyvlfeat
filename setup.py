from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy as np
import dependencies

# cython_modules = ["pyvlfeat/"]
cython_modules = []

setup(name='pyvlfeat',
      version='0.2',
      description='Cython wrapper of the VLFeat toolkit',
      author='Patrick Snape',
      author_email='p.snape@imperial.ac.uk',
      include_dirs=[np.get_include()],
      ext_modules=cythonize(cython_modules, nthreads=2,
                            quiet=True, language='c++'),
      packages=find_packages(),
      install_requires=dependencies.requirements,
      extras_require=dependencies.optionals,
      dependency_links=dependencies.repositories
)
