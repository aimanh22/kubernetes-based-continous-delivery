setup:
	python3 -m venv ~/.my-flask-app
	source ~/.my-flask-app/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_app.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile 
	pylint --disable=R,C app.py

all: install lint test
