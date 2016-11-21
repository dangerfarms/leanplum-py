# Develop

```python
pyvenv venv
. venv/bin/activate
pip install -r requirements.dev.txt
echo 'unit2' >> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Run tests
```
# (In venv)
unit2
```
