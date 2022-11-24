![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)

# default_struct
Default structure for python project

To initialize a new Project you need to modify:
1) .github/workflows/tests.yml -> Select the list of supported OS and python versions (default = ubuntu-latest, windows-latest, python=3.8 to 3.11)
2) docs/source/conf.py -> Doc MetaData
3) src -> subfolder name
4) requirements.txt -> list user requirements
5) requirements_dev.txt -> list dev requirements
6) setup.cfg -> Metadata, options, options.package_data
7) setup.py -> minimal python version check
8) tox -> list of python versions
