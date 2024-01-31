from .alpha_centauri_bb import identity as exoplanet_identity

print(__file__)


def identity():
    return "Alpha Centauri B"


if __name__ == "__main__":
    print(f"I'm {identity()} with {exoplanet_identity()}")
