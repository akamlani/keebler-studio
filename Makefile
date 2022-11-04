# download and install conda environment
# setup:
# 	conda create -n core.3.7 python=3.7
# 	conda activate core.3.7
# 	python -m virtualenv ~/.venv

VMROOT=.venv
VMNAME=$(VMROOT)/scratch-wks
PACKAGE_NAME=keebler-studio

.PHONY: clean

git_configure:
	git init

vm:
	python -m venv ~/$(VMNAME)
	echo "source ~/$(VMNAME)/bin/activate" >> ~/.bashrc

install:
# pre-commmit to git hooks on execution of 'git commit'
	pip install -U  pip setuptools wheel &&		\
	pip install -r  env/requirements.txt &&		\
	pre-commit install

clean:
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
