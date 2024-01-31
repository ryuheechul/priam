# python
_This is to demonstrate that importing siblings (and its children) in the root directory is a bad idea._
_Assuming we are pretending this directory is the top directory of your repo/proejct._




We are testing siblings and children of sibling in this package directory.


run `cat ./__main__.py ...` to see the contents there is specifics on each file what it tries to (relatively) import and that's what makes it work or not work


| run       | `__main__.py` | `black_hole.py` | `sun/earth/moon.py` | `alpha_centauri_b/alpha_centauri_bb.py` | `alpha_centauri_b/__main__.py` |
| --------- | ------------- | --------------- | ------------------- | --------------------------------------- | ------------------------------ |
| as script | o             | o               | o                   | o                                       | x                              |
| as module | x             | o               | o                   | o                                       | o                              |

as script: `python x.py`
as module: `python -m x`

e.g. in case as module:
- `python -m __main__`
  - and this doesn't work, anyone knows how to invoke this?
- `python -m black_hole`
- `python -m sun.earth.moon`
- `python -m alpha_centauri_b.alpha_centauri_bb`
- `python -m alpha_centauri_b`
