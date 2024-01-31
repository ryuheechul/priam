# sun

We are testing siblings and children of sibling and parent in this package directory.


run `cat ./__main__.py ...` to see the contents there is specifics on each file what it tries to (relatively) import and that's what makes it work or not work

| run       | `__main__.py` | `locate_..._system.py` | `mars.py` | `earth/moon.py` | `earth/__main__.py` |
| --------- | ------------- | ---------------------- | --------- | --------------- | ------------------- |
| as script | x             | x                      | o         | o               | x                   |
| as module | x             | x                      | o         | o               | o                   |

as script: `python x.py`
as module: `python -m x`

e.g. in case as module:
- `python -m __main__`
  - and this doesn't work, anyone knows how to invoke this?
- `python -m locate_..._system`
- `python -m mars`
- `python -m earth.moon`
- `python -m earth`
