.. :changelog:
1.0.14 (19-12-22)
~~~~~~~~~~~~~~~~~~~
-updated version number to match pypi distributions.

1.0.13 (28-10-22)
~~~~~~~~~~~~~~~~~~~
-fixed installation bug (issue #15).

1.0.12 (24-08-20)
~~~~~~~~~~~~~~~~~~~
-fixed a bug with the phi angle being corrected for orbital motion
-fixed a bug when, due to orbital motion, phi increases above 90 degrees or below -90 degrees

1.0.10 + 1.0.11 (12-08-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
-made sure numpy>=1.16.2 is installed when installing catwoman

1.0.9 (10-08-20)
~~~~~~~~~~~~~~~~~
-actually removed unused files (see below)

1.0.8 (10-08-20)
~~~~~~~~~~~~~~~~~
-removed unused files from directory so they aren't include in installation

1.0.7 (29-06-20)
~~~~~~~~~~~~~~~~~
-fixed a bug with installing catwoman straight from source archive, involved removing unused python files from import

1.0.6 (27-06-20)
2.5.3 (2025-05-05)
~~~~~~~~~~~~~~~~~~
- update CI to latest stable python versions
- update numpy version to 2.0 in C extensions

2.5.2 (2025-10-01)
~~~~~~~~~~~~~~~~~~
- renamed I variable in common.h to avoid duplication with linux macros

2.5.1 (2024-16-04)
~~~~~~~~~~~~~~~~~~
- created new tests for `transitmodels.py`

2.5.0 (2024-16-04)
~~~~~~~~~~~~~~~~~~
- updated `setup.py` file with setuptools instead of distutils.

2.4.9 (2022-29-05)
~~~~~~~~~~~~~~~~~~
- require oldest-supported-numpy in pyproject.toml

2.4.8 (2021-24-05)
~~~~~~~~~~~~~~~~~~
- fix bug in setup.py for python 3.8 install, add support for inverse transits

2.4.7 (2020-10-06)
~~~~~~~~~~~~~~~~~~
- specify numpy as a build dependency, ensure times are contiguous, remove extraneous calculations for zero eccentricity orbits

2.4.6 (2017-11-25)
~~~~~~~~~~~~~~~~~~
- fixed setup.py file so catwoman specifies and downloads dependencies automatically when pip installed in a new environment

