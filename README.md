# keebler-studio
Template starter pack for new projects

## Installation
Install Libraries and Dependencies
```sh
# installs the library in 'edit' mode for development into prior installed environment
# show be installed as: `{*-template}` in listing the packages (pip list | less ) as mentioned in setup.py
cd '{*-template}'
rm -r $(find . -name '*.egg-info')
pip uninstall <package_name>
pip install -e .
pip install -e .[all]
pip install -e .[data]
```
