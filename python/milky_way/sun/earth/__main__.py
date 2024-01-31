from .iss import identity as iss_identity
from .moon import identity as moon_identity


print(__file__)


def identity():
    return "the Earth"


if __name__ == "__main__":
    msg = f"I'm {identity()} with {moon_identity()} and {iss_identity()}"
    print(msg)
