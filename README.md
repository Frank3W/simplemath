# Simple Math
This repo presents and demos techniques for building a `python` package. To install this demonstration package, download and run at the root folder
```bash
pip install .
```

### `pip install .` vs `python setup.py install`
To install a `python` package from the source, `pip` command is
```bash
pip install <path_to_package>
```
where `<path_to_package>` folder contains the source code and setup files: `setup.cfg` and `setup.py`. It will invoke the `setuptool` library to build the package, which is reflected in `pyproject.toml`.

Alternative command to build a package from the source is `python install setup.py`. But `pip install` is a better solution since `pip` is better at managing and resolving package dependence.

### `setup.py` and `setup.cfg`.
`setuptools` is in the transition from `setup.py` to `setup.cfg` where `setup.cfg` will contain static setup but `setup.py` will contain dynamic setup. Even when all setup contents are static, it is still useful to have `setup.py` there to enable `pip install -e` to launch develop mode as below

```python
import setuptools
setuptools.setup()
```

### install_requires vs requirement.txt
`install_requires` is an option in `setup.cfg` to specify the dependent packages. Those dependent packages will be installed if not existent in the environment when installing package. `requirements.txt` is a text file to keep all dependent packages and to be able installed by command
```bash
pip install -r requirements.txt
```
But the packages in `requirements.txt` won't be automatically installed when run install package command like
```bash
pip install .
```

A good practice for the use of these two places to track package dependence is:
- use `requirements.txt` to record exact version when package developed,
- use `install_requires` to record compatible versions like `>=1.1.2` for package users;

see an example at [requirements.txt](requirements.txt) and [setup.cfg](setup.cfg).

In a data science pipeline, to enable reproducibility, it is critical to have `requirements.txt` track the exact version of all dependence.

### package data
If a package requires data to come with, this can be specified at `setup.cfg` as
- In [options] section, `include_package_data = True`
- In [options.package_data] section, declare location of the data files relative to the root folder that contains `setup.cfg`

see [setup.cfg](setup.cfg) for an example. To load the data to the package code, the package `pkg_resources` distributed with `setuptools` plays a role; see [print_numbers.py](simplemath/print_numbers.py) for an example.


### entry point
`setuptools` provides entry point mechanism to wrap function in the package into standalone CLI command in the installation process. One package can have multiple entry points, i.e., installation generates multiple CLI commands. The entry points can be defined at `setup.cfg`; see [setup.cfg](setup.cfg) for an example.

- The CLI commands generated will only exist in the environment where the package is installed.

- Entry point points to a specific function in the package. `hello = simplemath.hello:hello` is essentially equivalent to:
```python
import sys
from simplemath.hello import hello
if __name__ == '__main__':
    sys.exit(hello())
```

- If the function takes parameters from `sys.args`, then corresponding CLI command created will follow; see [hello.py](simplemath/hello.py) for an simple implemented by `click`.


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

This package has the feature of `__main__.py` implemented and invoked after installation as
```bash
python -m simplemath
```

### package test
Package requires test module to ensure that all code pass quality standards. In package installation, testing component is not mandatory. But it is a good (in fact, must-have) practice to get installed package tested in different environments before distribution. This process contains two logic parts that can fulfilled by two commonly used `python` tools:

- `tox` - automatically create specified isolated environments, install required dependence and launch testing commands.
- `pytest` - execute testing cases implemented in its framework.

`tox` tool can be installed by running `pip install tox`. After the installation, command `tox` is supposed to run at the folder where it contains setup file (`setup.cfg`and/or `setup.py`) and `tox.ini`. The file `tox.ini` provides the configuration for `tox` execution. The command to invoke testing is also specified in `tox.ini` file; see [tox.ini](tox.ini) for an example.

In `tox.ini`, the dependency for running test can be provided. Note that the dependency given by `install_requires` in setup file will be automatically installed by `tox` into isolated testing environments as well.