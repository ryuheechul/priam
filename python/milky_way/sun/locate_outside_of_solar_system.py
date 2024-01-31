from ..black_hole import identity as black_hole_identity
from ..alpha_centauri_b.__main__ import identity as another_star_identity

print(__file__)

if __name__ == "__main__":
    print(
        f"I'm locating {black_hole_identity()} and {another_star_identity()} from our solar system"
    )
