# Simple Math
This repo presents and demos how to build a `python` package to distribute and share with others via package installation. The key elements for creating an installable `python` package are covered. The good practices regarding those elements are discussed as well.

This repo contains the source code of an installable `simplemath` package for demonstration purpose. This package can be installed by running the `pip` command at the root folder
```bash
pip install .
```

### setup files
To make a package installable, it requires the existence of a combination of files from `setup.py`, `setpu.cfg` and `pyproject.toml` at the root folder of the repo. Those files provide the configuration for package installation.

The following are two alternative minimal combinations required for installation:
- `setup.py`
- `setup.cfg` and `pyproject.toml`

Installation will invoke package `setuptools` for the execution to build. In the latest version of `setuptools`, it is recommended to have all these 3 files for the separate purposes
- `pyproject.toml` makes system build tools explicit; see [pyproject.toml](pyproject.toml) that is sufficient for most projects.
- `setup.cfg` contains static configuration and provides default values for setup entries.
- `setup.py` contains dynamic setup configuration that can be based on user inputs or local environments.

As mentioned above, file `setup.py` is not mandatory. It is not required if all setup configuration is static. But even in this case, it is still a good practice to have this file `setup.py` with simple contents as:

```python
import setuptools
setuptools.setup()
```

More importantly, the package installation in development mode requires the existence of the file `setup.py`. This mode is quite useful in code development phase, although not required in package installation.

### `pip install .` vs `python setup.py install`
To install a `python` package from the source, the `pip` command is
```bash
pip install <path_to_package>
```
where `<path_to_package>` folder contains the source code and required setup files as shown above. The development mode can be launched with option `-e` as `pip install -e <path_to_package>`.

Alternative command to build a package from the source is `python install setup.py`. But `pip install` is a better solution since `pip` is a standard tool to manage and resolve package dependence.


### install_requires vs requirement.txt
`install_requires` is an option in `setup.cfg` to specify the dependent packages. Those dependent packages will be installed if not existent in the environment when installing package. `requirements.txt` is a text file to keep a track of all dependent packages and to be able installed by `pip` command
```bash
pip install -r requirements.txt
```

Note that the packages in `requirements.txt` won't be automatically installed when running `pip` installation

A good practice around the use of these two places to track package dependence is:
- use `requirements.txt` to record exact version when package developed,
- use `install_requires` to record compatible versions like `>=1.1.2` for package users;

see an example at [requirements.txt](requirements.txt) and [setup.cfg](setup.cfg).

In a data science pipeline, to enable reproducibility, it is critical to have `requirements.txt` to track the exact version of all dependence.

### package data
If a package requires data to come with, this can be specified at `setup.cfg` as
- In [options] section, `include_package_data = True`
- In [options.package_data] section, declare location of the data files relative to the root folder that contains `setup.cfg`

see [setup.cfg](setup.cfg) for an example. To load the data to the package code, the package `pkg_resources` distributed with `setuptools` plays a role; see [print_numbers.py](simplemath/print_numbers.py) for an example.


### entry point
`setuptools` provides entry point mechanism to wrap function in the package into standalone CLI command in the installation process. One package can have multiple entry points, i.e., installation creates multiple CLI commands. The entry points can be defined at `setup.cfg`; see [setup.cfg](setup.cfg) for an example.

- The CLI commands generated will only exist in the environment where the package is installed.

- Entry point points to a specific function in the package. `hello = simplemath.hello:hello` is essentially equivalent to:
```python
import sys
from simplemath.hello import hello
if __name__ == '__main__':
    sys.exit(hello())
```

- If the function takes parameters from `sys.args`, then corresponding CLI command created will follow; see [hello.py](simplemath/hello.py) for an simple implemented by package `click`.


### \_\_main\_\_ file
To be able to run a command like
```bash
python -m <packagename>
```
it requires `__main__.py` file to exist. The scripts in the file will be executed when running command above. This mechanism is like a `python` module having lines like
```python
if __name__ == '__main__':
    # script block
```
The script block will be executed by `python -m <python_module>`. The file `__main__.py` is like the version for a package.

This package has the feature of `__main__.py` implemented and it can be invoked after installation by
```bash
python -m simplemath
```

### package test
Package requires test module to ensure that all code pass quality standards. In package installation, testing component is not mandatory. But it is a good (in fact, must-have) practice to get installed package tested in different environments before distribution. This process contains two logic parts that can fulfilled by two commonly used `python` tools:

- `tox` - automatically create specified isolated environments, install required dependence and launch testing commands.
- `pytest` - execute testing cases implemented in its framework.

`tox` tool can be installed by running `pip install tox`. After the installation, command `tox` is supposed to run at the folder where it contains setup files and `tox.ini`. The file `tox.ini` provides the configuration for `tox` execution. The command to invoke testing is also specified in `tox.ini` file; see [tox.ini](tox.ini) for an example.

In `tox.ini`, the dependency for running test can be provided. Note that the dependency given by `install_requires` in setup file will be automatically installed by `tox` into isolated testing environments as well.