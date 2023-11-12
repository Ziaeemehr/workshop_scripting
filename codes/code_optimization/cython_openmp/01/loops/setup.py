from distutils.core import setup
# from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext

# setup(name="fastloop", ext_modules=cythonize('fastloop.pyx'),)

ext_modules=[ Extension("fastloop",
              ["fastloop.pyx"],
              libraries=["m"],
              extra_compile_args = ["-ffast-math"])]

setup(
  name = "fastloop",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules)