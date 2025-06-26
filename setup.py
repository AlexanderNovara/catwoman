from __future__ import print_function
import setuptools
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import numpy as np
import os
import shutil
import tempfile


class CustomBuildExt(build_ext):
    def build_extensions(self):
        ce = self.compiler
        if ce.compiler_type == "unix":
            if self.compiler_has_openmp():
                for e in self.extensions:
                    e.extra_compile_args += ["-fopenmp", "-std=c99"]
                    e.libraries += ["gomp"]
            else:
                for e in self.extensions:
                    e.extra_compile_args += ["-std=c99"]
        super().build_extensions()

    def compiler_has_openmp(self):
        """Check if the compiler supports OpenMP"""
        test_code = "#include <omp.h>\nint main() { omp_get_num_threads(); return 0; }"
        return self.try_compile(test_code, extra_postargs=["-fopenmp"])

    def try_compile(self, code, extra_postargs=None):
        """Attempt to compile a test program"""
        tmp_dir = tempfile.mkdtemp(prefix="tmp-setuptools")
        file_name = os.path.join(tmp_dir, "test.c")
        with open(file_name, "w") as file:
            file.write(code)
        try:
            self.compiler.compile(
                [file_name], output_dir=tmp_dir, extra_postargs=extra_postargs
            )
            return True
        except setuptools.distutils.errors.CompileError:
            return False
        finally:
            shutil.rmtree(tmp_dir)

extensions = [
    Extension("catwoman._nonlinear_ld", ["c_src/_nonlinear_ld.c"]),
    Extension("catwoman._quadratic_ld", ["c_src/_quadratic_ld.c"]),
    Extension("catwoman._logarithmic_ld", ["c_src/_logarithmic_ld.c"]),
    Extension("catwoman._exponential_ld", ["c_src/_exponential_ld.c"]),
    Extension("catwoman._custom_ld", ["c_src/_custom_ld.c"]),
    Extension("catwoman._power2_ld", ["c_src/_power2_ld.c"]),
    Extension("catwoman._rsky", ["c_src/_rsky.c"]),
    Extension("catwoman._eclipse", ["c_src/_eclipse.c"]),
]

setup(	name='catwoman',
	version="1.0.14",
	author='Kathryn Jones',
	author_email = 'kathryndjones@hotmail.co.uk',
	url = 'https://github.com/KathrynJones1/catwoman',
	packages =['catwoman'],
	license = 'GNU GPLv3',
	description ='Transit modelling package for asymmetric light curves',
	long_description=open('README.rst').read(),
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Programming Language :: Python'
		],
	include_dirs = [np.get_include()],
    install_requires=["numpy"],
    setup_requires=["wheel"],
    extras_require={
        "matplotlib": ["matplotlib"],
    },
    ext_modules=extensions,
    cmdclass={"build_ext": CustomBuildExt},
)
