venv:
	virtualenv -p python3 .venv
	. .venv/bin/activate && \
	pip install -r requirements.txt

test:
	. venv/bin/activate && \
	coverage run --source=mocking/ -m unittest discover -s mocking/ && \
	coverage report -m

run:
	. venv/bin/activate && \
	cd mocking && \
	python test_mocked.py