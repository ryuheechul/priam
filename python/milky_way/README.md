# milky way
We are testing siblings and children of sibling and parent in this package directory.


run `cat ./__main__.py ...` to see the contents there is specifics on each file what it tries to (relatively) import and that's what makes it work or not work


| run       | `andromeda.py` | `milky_way/alpha_centaury_b/__main__.py` | `milky_way/sun/mars.py` | `milky_way/sun/earth/__main__.py` |
| --------- | -------------- | ---------------------------------------- | ----------------------- | --------------------------------- |
| as script | x              | x                                        | o                       | x                                 |
| as module | x              | o                                        | o                       | o                                 |

as script: `python x.py`
as module: `python -m x`

e.g. in case as module:
- `python -m andromeda.py`
- `python -m milky_way.alpha_centaury_b`
- `python -m milky_way.sun.mars`
- `python -m milky_way.sun.earth`
