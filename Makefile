all:
	black -l 79 src/*
	flake8 src/jarvis.py src/main.py src/parameters.py
	python3 src/main.py
