# Python Relative Imports Aha Moments

## Why Relative Imports in Python Is Relatively Not So Straight Foward?

Have you encountered these errors while you are trying to import other python file?
```
# this
ImportError: attempted relative import with no known parent package
# or
ImportError: attempted relative import beyond top-level package
```

Have you been trying to understand why relative import that just doesn't seem to work (by reading something like below)?

- https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
- (and there are tons more when you google)

Have you messed with `sys.path.append` as you stumbled upon as a suggestion?

Why doesn't it just work? That's the answer that I was looking for and as I got some aha moment of how to make these work,
I've setup multiple different scenarios under [python](./python) directory and its children.

Reading `README.md` files in each directory should give you some idea on what's going on and feel free to run them to help you get oriented.

Yes, you are welcome.

Also for the sake of complexity, I will compare what happens when you try to do the same thing in nodejs and deno (stay tuned).

## Modules and Packages

I should also write a bit about running python files in different mode `python x.py` vs `python -m x`

- isn't `python -m` is for existing or installed module like `python -m pip` not for my source code?
  - that's what we will talk about
- what is a module
- what is a package
- what is site packages

## Off Topic
also not impressed with current status of packaging
- https://chriswarrick.com/blog/2023/01/15/how-to-improve-python-packaging/
- https://github.com/mitsuhiko/rye/discussions/6
