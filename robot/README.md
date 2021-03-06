# PSAR - Robot

![robot-moving](https://user-images.githubusercontent.com/32545895/79999160-9695b100-8489-11ea-904b-cf8804416c93.gif)

## Before starting

**PLEASE** have a look at the [wiki](../wiki/README.md), it is quite usefull!

### Folder structure

- `/src` for the code in python
- `/scripts` for that kind of command-line interface stuff
- `/tests` for your tests
- `/lib` for your C-language libraries
- `/doc` for most documentation
- `/apidoc` for the API docs.

## Setup

We will use pipfile to facilitate python environment. Here is a [guide on how to use pipenv](https://realpython.com/pipenv-guide/).

### Installation

1. First, install python on your computer. For now, you will need to install python version 3.5 on your device.
2. In the root directory, use the command `pipenv install` to install a python virtual environment and all required dependencies.

If you are on bash, you can simply source the `setup` script.

```bash
source scripts/setup
```

### Usage

- When installing a new module, use `pipenv install <module _name'>` instead of the traditionnal `pip install '<module _name'>` . This will add the module to the list of dependencies.

## Running

```bash
python -m src.main
```

## Tests

### Running

```bash
pipenv run nose2
```

### Coverage

```bash
pipenv run coverage run && pipenv run coverage report
```
