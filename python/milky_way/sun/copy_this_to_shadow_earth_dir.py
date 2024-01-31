# copy this file to `moon.py`
# try `python -m earth` and `python -m earth.moon`
# now you see that this file shadows `earth/` package

print(__file__)


def identity():
    return "wannabe earth"


if __name__ == "__main__":
    print(f"I'm {identity()}")
