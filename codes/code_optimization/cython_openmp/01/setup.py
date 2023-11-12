from distutils.core import setup 
from distutils.extension import Extension 
# from Cython.Build import cythonize
from Cython.Distutils import build_ext
ext_module = Extension(
    "numthreads",
    ["useopenmp.pyx"],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp']
)

setup(
    name = 'OpenMP app',
    cmdclass = {"build_ext" : build_ext},
    ext_modules = [ext_module],
)

