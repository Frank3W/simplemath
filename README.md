# Simple Math
This package presents techniques for building a `Python` package.

To install a `Python` package from the source, run
```bash
pip install <path_to_package>
```
where `<path_to_package>` folder contains the source code and setup files: `setup.cfg` and `setup.py`. It will invoke the `setuptool` library to build the package, which is reflected in `pyproject.toml`.

- Alternative command to build a package from the source is `python install setup.py`. But `pip install` is a better solution since `pip` is better at managing and resolving package dependence.

- `setuptool` is in the transition from `setup.py` to `setup.cfg` where `setup.cfg` will contain static setup but `setup.py` will contain dynamic setup. Even when all setup contents are static, it is still useful to have `setup.py` there to enable `pip install -e` to launch develop mode as below

  ```python
  import setuptools
  setuptools.setup()
  ```


- To be able to run a command like
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
