# download and install conda environment
# setup:
# 	conda create -n core.3.7 python=3.7
# 	conda activate core.3.7
#   conda update
# 	python -m virtualenv ~/.venv

VMROOT=.venv
VMNAME=$(VMROOT)/default-wks
PACKAGE_NAME=keebler-studio

CONDA_ENV=base.vm.v3_9
PYTHON_VERSION=3.9


.PHONY: clean

git_configure:
	git init


vm:
	python -m venv ~/$(VMNAME)
	. ~/$(VMNAME)/bin/activate
	echo "~/$(VMNAME)/bin/activate" >> ~/.bashrc
	echo "~/$(VMNAME)/bin/activate" >> ~/.zshrc

conda_install:
	conda create -n $(CONDA_ENV) python=$(PYTHON_VERSION) && 				\
	source $$(conda info --base)/etc/profile.d/conda.sh && 					\
	conda activate $(CONDA_ENV)												\
	conda update

install:
# pre-commmit to git hooks on execution of 'git commit'
	pip install -U pip pip-tools setuptools wheel &&						\
	pip install -r env/requirements.txt && 									\
	pre-commit install && 													\
	pre-commit autoupdate
# pip install -e ".[${VMNAME}]" --no-cache-dir

clean:
	find . -type f -name "*.DS_Store" -ls -delete
	pip uninstall $(PACKAGE_NAME)
# pip uninstall $(basename $(find . -name '*.egg-info') .egg-info)
#rm -r $(find . -name '*.egg-info')
	rm -rf ~/$(VMNAME)

build:
	python setup.py build

test:
	pip install -r  env/requirements_test.txt
	python -m pytest -vvv  --cov=keebler tests

# 	python -m pytest -vvv  --cov=keebler examples tests
# 	python -m pytest -ravv --cov=keebler examples tests

quality:
	black --check *.py
	isort --check-only *.py

style:
	black   *.py
	isort   *.py
	flake8  --statistics *.py

lint:
	pylint *.py

setup: vm install
all: install quality style lint #test
