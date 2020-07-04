# Contributing to Humanify

A simple guide on best practises and enviroment setup for contributing to Humanify.

## Setting up a developer enviroment

You first need to clone this repository with:

```bash
git clone https://github.com/ef4203/humanify && cd humanify/
```

Once you are inside of the `humanify/` directory, you need to make sure both [Python 3.8](https://www.python.org/) and [Pipenv](https://pipenv.pypa.io/en/latest/) are installed then you can install developer dependancies with:

```bash
pipenv install
```

And then enter the virtual enviroment:

```bash
pipenv shell
```

Once you have entered the virtual environment, you have successfully setup a developer enviroment! To run tests you can do `nosetests` or to lint the humanify directory, `pylint humanify/`.
