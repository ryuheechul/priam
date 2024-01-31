# if you run this file in the same directory,
# it will fail with `ImportError: attempted relative import with no known parent package`
# you can circumvent this by stepping outside like `cd .. && python -m python.andromeda`
from .milky_way.__main__ import identity as galaxy_identity

print(__file__)


def identity():
    return "the Andromeda galaxy"


if __name__ == "__main__":
    print(f"I'm {identity()} that is close to {galaxy_identity()}")
