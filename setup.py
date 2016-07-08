# Build OGDF with shared setting and -fPIC flag
# http://www.ogdf.net

# Linux Arch

import os

from distutils.core import setup, Extension

from Cython.Distutils import build_ext

home = os.environ.get("HOME", "")

print("setup2.py", home)

module1 = Extension('ogdf',
                    include_dirs = ['{}/packages/ogdf/include'.format(home)],
                    libraries = ['OGDF', 'COIN'],
                    library_dirs = ['{}/packages/ogdf'.format(home)],
                    sources = ['main.cpp'],
                    #extra_objects = ["libOGDF.so", "libCOIN.so"],
                    extra_compile_args = ["-fPIC", "-shared"],
                    language = "c++")

setup(
    name = 'python-OGDF',
    version = '0.1',
    description = 'This is a demo package',
    cmdclass = {"build_ext": build_ext},
    ext_modules = [module1]
)
