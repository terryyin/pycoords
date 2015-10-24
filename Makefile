.PHONY: all tests pep8 pylint deps test-deps publish

all: extensive pylint
extensive: tests pep8

tests:
	nosetests tests

pep8:
	pep8 --exclude=mock.py pycoords_lib tests

pylint:
	pylint --rcfile pylintrc pycoords_lib

deps:
	pip install -r dev_requirements.txt

publish:
	python setup.py sdist upload

