# Python logger

## How it works

I could explain it all but [Real Python](https://realpython.com/python-logging/) is better than me to do that so if you want/need a complete explanation click on the link.

## Important to know

### Create a new logger

Since the root logger is already created with the right handler the only thing you should do is create a logger specify the appropriate parent, either: `BaseStation` or `Robot`

So for example, if we want to create a logger for the RobotEventHandler on the BaseStation it would look like this:

```python
import logging
# ...

logger = logging.getLogger('BaseStation.RobotEventHandler')

# ...
```

### How to use it

It's really as simple as it can be to use a logger, examples are made form the root logger `BaseStation`.

#### Normal usage

```python
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

output:

```
21:34:09 - BaseStation - DEBUG - debug message
21:34:09 - BaseStation - INFO - info message
21:34:09 - BaseStation - WARNING - warn message
21:34:09 - BaseStation - ERROR - error message
21:34:09 - BaseStation - CRITICAL - critical message
```

#### Exception message

In case you have a try-except there's a dedicated function to log exception message that will include the Traceback as well:

```python
try:
    raise ValueError("test")
except:
    logger.exception('exception message')
```

output:

```
21:34:09 - BaseStation - ERROR - exception message
Traceback (most recent call last):
  File ".../src/main.py", line 32, in init_logging
    raise ValueError("test")
ValueError: test
```

> Paths have been shorten

### Change logger level

The config is located in the config directory in a file named: logging.yml
In this file, the only case where you could need to change it is to change the level of the logger.
To do that locate the logger under the loggers section and change the line to the level of logger that suits your need, here are the available levels: 

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

[BACK](./README.md)
