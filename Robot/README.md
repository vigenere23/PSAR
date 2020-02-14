# Design 3 - The Robot

## File Architecture

- `/src` for the code in python
- `/scripts` for that kind of command-line interface stuff
- `/tests` for your tests
- `/lib` for your C-language libraries
- `/doc` for most documentation
- `/apidoc` for the API docs.

## How to install

We will use pipfile to facilitate python environment here is a [guide on how to use pipenv](https://realpython.com/pipenv-guide/)

### The basics :

- First install python on your computer, for now you need to install python version 3.5 on your device
- In the root directory use the command `pipenv install` to install a python env and all required dependencies
- done

### Nice to know :

- When installing a new module use `pipenv install 'module name'` instead of the traditionnal `pip install 'module name'` this will add the module in the pipfile as a dependency

## Run

```bash
python -m src.main
```
