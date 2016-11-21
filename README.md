Python wrapper for the [Leanplum API](https://www.leanplum.com/dashboard#/4510371447570432/help/setup/api).

Implemented methods:
- start
- stop

TODO (prod, highest priority):
- setUserAttributes
- track
- multi
- sendMessage
- advance
- pauseState
- resumeState

TODO (prod):
- setDeviceAttributes
- getVars
- heartbeat
- pauseSession
- resumeSession
- setTrafficSourceInfo
- downloadFile

TODO (dev):
- registerDevice
- multi (import mode)
- getMultiResults
- setVars
- uploadFile

TODO: Data export methods

TODO: Content read-only methods
 
TODO: Handle limit and other errors

# Develop

```python
pyvenv venv
. venv/bin/activate
pip install -r requirements.dev.txt
echo '#!/bin/bash
. venv/bin/activate
unit2' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Run tests
```
# (In venv)
unit2
```
