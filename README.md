# Simple Math
This package presents and demos techniques for building a `Python` package.

### `pip install .` vs `python setup.py install`
To install a `Python` package from the source, run
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