all: debug

clean:
	rm -f .coverage
	find . -name \*.pyc -delete

test: clean
	python -m unittest discover -v -t . -s test

debug:
	dev_appserver.py --host 0.0.0.0 .

deploy:
	make test && appcfg.py update --oauth2 .

lint:
	flake8 .

coverage: clean
	coverage run -m unittest discover -f -t . -s test 2> /dev/null
	coverage report -m

.PHONY: clean test debug deploy lint coverage
