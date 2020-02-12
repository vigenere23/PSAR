# Design 3 -  The Base Station

## Before starting...

### Folder structure

- `/src` for the code in python
- `/scripts` for that kind of command-line interface stuff
- `/tests` for your tests
- `/lib` for your C-language libraries
- `/doc` for most documentation
- `/apidoc` for the API docs.

### Clean architecture (in `src/` and `tests/`)

- `domain` : the core functionalities or the app. That's where all the logic, sub-systems, vision, etc. goes.
- `interface` : that's where our receiving APIs go. This layer is responsble for receiving commands and dispatching them to the core system. It is normally divided into one folder per technology, wich forms small sub-parts of the complete API. No class should ever have a dependency on this layer. 
  - `/rest_api` : Could be a folder for all the rest APIs controllers
  - `socket_api` : Folder for all the socketIO's event handlers (by namespace)
- `infrastructure` : where the system communicates with the outside world. Normally, a domain abstract class should represent every class in this layer, such that the usage will the completly decoupled with the technological implementation. For exemple, for sending events we are now using sockets (from `flask-socketio`), but one day we might change that with another technology. So, the domain should only use those domain abstractions (like `RobotEventEmitter`) instead of directly using the infrastructure implementations (like `RobotNamespace` - specific to sockets). 
  - `/socket_emitters` : the folder that contains all socketIO's event emitters. They should be regroup by namespace (like `RobotNamespace`). 
  - `/repositories` : the folder for normally fetching data (synchronously) or saving data. This could be used for managing the global context (would actually be a great idea I think). 

## Setup

We will use pipfile to facilitate python environment. Here is a [guide on how to use pipenv](https://realpython.com/pipenv-guide/).

### Installation

1. First, install python on your computer. For now, you will need to install python version 3.5 on your device.
2. In the root directory, use the command `pipenv install` to install a python virtual environment and all required dependencies.

### Usage

- When installing a new module, use `pipenv install <module _name'>` instead of the traditionnal `pip install '<module _name'>` . This will add the module to the list of dependencies.

## Running

```bash
python -m src.main
```

## Testing

```bash
python -m tests.all
```
