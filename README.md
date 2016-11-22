Python wrapper for the [Leanplum API](https://www.leanplum.com/dashboard#/4510371447570432/help/setup/api).

Implemented methods:
- start
- stop
- setUserAttributes
- track
- multi
- sendMessage

TODO (prod):
- advance
- pauseState
- resumeState
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
make
```

## Run tests

### Unit tests
`make test`

### Integration tests
1. Create a leanplum app if you haven't done so yet.
2. Create `.env` in the project root. (This is gitignored.)
3. Add your app id and keys, and a message id in the following format:
```
export LEANPLUM_APP_ID="your app id here"
export LEANPLUM_PRODUCTION_CLIENT_KEY="your production key here"
export LEANPLUM_DEVELOPMENT_CLIENT_KEY="your development key here"
export LEANPLUM_TEST_MESSAGE_ID="a test message id from leanplum"
```

Now you can run:
`make integration`

### Running all tests
`make testall`
