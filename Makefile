build:
	python setup.py build

sdist:
	python setup.py sdist

publish:
	python setup.py sdist
	twine upload dist/*

publishtest:
	python setup.py sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

test:
	pytest

rst:
	pandoc --from=markdown --to=rst --output=README.rst README.md

clean:
	if [ -d 'dist' ]; then \
		rm -r dist; \
	fi

	if [ -d 'build' ]; then \
		rm -r build; \
	fi
