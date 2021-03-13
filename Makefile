PYTHON_BIN = /usr/bin/python3.9
VIRTUALENV = /Calc

all : $(VIRTUALENV)

# Configure virtualenv for this project.
$(VIRTUALENV) :
	 -p $(PYTHON_BIN) $(VIRTUALENV)
	source $(VIRTUALENV)/bin/activate

# Install editor tooling.
.PHONY: tooling
tooling : $(VIRTUALENV)
	/usr/bin/pip3.9 install --user jedi
	/usr/bin/pip3.9 install --user epc
	/usr/bin/pip3.9 install --user flake8
	/usr/bin/pip3.9 install --user black
	/usr/bin/pip3.9 install --user autopep8
	/usr/bin/pip3.9 install --user yapf
