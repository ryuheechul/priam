# yup, you can't do just `from .earth import ...`, lol
from .earth.__main__ import identity as earth_identity

# but you can do this with mars since marse.py is a module not a package
from .mars import identity as mars_identity
random things

print(__file__)

random things

def identity():
    return "the Sun"


if __name__ == "__main__":
    print(f"I'm {identity()} with {earth_identity()} and {mars_identity()}")
