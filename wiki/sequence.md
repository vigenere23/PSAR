# Sequence and tasks

## Sequence

The sequence system works with **tasks**, with are small units that should represent a real-life tasks as of defined by the project's statement. These tasks can either represent a robot's action (e.g. take puck, measure resistance, etc.) or a system action (e.g. calibrate). Each task can of course do more that one thing. For exemple, measuring the resitance needs the robot to move to that station first, which itself needs finding the robot and finding the right path.

Here is the list of tasks that are defined for now :

0. **Configure (not a task, actions here will only be performed once)**
    - Load configuration profiles for camera
    - Load units convertions
1. **Calibrate**
    - Rotate robot to the right direction (facing upward)
    - Find objects (table, pucks, pillars, zones, etc.)
2. **Measure resistance (retryable)**
    - Rotate robot to face the resistance station
    - Move to resistance station
    - Measure resistance
        - if failing, move robot back and retry
        - else, save resistance value
3. **Capture arrow table (retryable)**
    - Move robot back
    - Rotate robot to face end of table
    - Move robot to arrow table
    - Capture table
        - if fails, move robot back and/or sideways and retry
        - else, save arrow value
4. **Capture letter table (retryable)**
    - Move robot back
    - Rotate robot to face end of table
    - Move robot to letter table
    - Capture table
        - if fails, move robot back and/or sideways and retry
        - else, save letter value
5. **Take first puck (retryable)**
    - Rotate to face first puck
    - Move to first puck
    - Delegate to robot (use robot camera, adjust position, take puck)
        - if fails, move back and/or sideways, then retry
        - else, save first puck as taken
6. **Take second puck (same as 5.)**
7. **Take third puck (same as 5.)**
8. **Drop first puck (retryable)**
    - Move to puck position #1
    - Delegate to robot (use robot camera, adjust position, drop puck)
        - if puck not well dropped, take puck, and retry
        - else, save first puck as dropped
9. **Drop second puck (same as 8.)**
10. **Drop third puck (same as 8.)**
11. **Final task**
    - Move robot to center of green square
    - Turn red light on

## Task

As said earlier, a `task` should represent an independent unit of work. It can consist of multiple actions, but usually represents a goal as stated in the projet's assignement.

### Types of failure

Most of the tasks can fail for multiple reasons (connectivity problems, light reflects on image, etc.). These failures can represent different importance in the sequence, thus we have to correctly define them.

- #### `WarningException`

  A failure that can happen but that **will** be handled by the next task or that will not affect the remaing tasks. This will be handled by the container and a corresponding event will be sent. The present task will end and the next one will start normally.

- #### `RetryException`

  A failure that indicates that the task should be retried. That should be reserved to error that **can** happen, but are mostly due to a specific random context that is not controlable. 

  > Please note that to be handled, the `execute` method **needs** to be attached to the [Retryable](#retryabletimes-int) decorator. 

- #### Any other exception

  Any other exception will be treated as **critical** and will **terminate** the entire sequence. This is to ensure that every exception that needs to be handled will be handled, and that unexcepted exception will remain unexpected. 

### Decorators

There are some decorators that helps removing boiler-plates needed for common situations.

- #### `Retryable(times: int)`

  Indicates that a task should be retried a maximum of `times` times. To retried, the task needs to raise a `RetryException`. Else, the exception will be unhandled and thus considered critical. 

[BACK](./README.md)
