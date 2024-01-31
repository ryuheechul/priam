# earth
We are testing siblings only in this package directory.

run `cat ./__main__.py ./moon.py ./iss.py` to see the contents as there is specifics on each file what it tries to (relatively) import and that's what makes it work or not work


| run       | `__main__.py` | `moon.py` | `iss.py` |
| --------- | ------------- | --------- | -------- |
| as script | x             | o         | o        |
| as module | x             | o         | o        |

as script: `python x.py`
as module: `python -m x`

e.g. in case as module:
- `python -m __main__`
  - and this doesn't work, anyone knows how to invoke this?
- `python -m moon`
- `python -m iss`
