PYTHON_INTERPRETER = python3.11
PYTHON = . ./.venv/bin/activate && $(PYTHON_INTERPRETER)
PROJECT_NAME = aoc

.PHONY: venv clean

venv: requirements.txt
	$(PYTHON_INTERPRETER) -m venv ./.venv --clear --prompt $(PROJECT_NAME)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m ipykernel install --user --name $(PROJECT_NAME)

clean:
	rm -rf ./.venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete