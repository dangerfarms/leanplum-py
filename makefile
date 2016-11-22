install:
	@pyvenv venv
	@venv/bin/pip install -r requirements.dev.txt
	@echo "#!/bin/bash" > .git/hooks/pre-commit
	@echo "make testall" >> .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit

testall: test integration

venv:
	@venv/bin/activate

test: venv
	@venv/bin/unit2

integration: venv
	@. ./.env && venv/bin/unit2 discover --pattern 'integration*.py'

