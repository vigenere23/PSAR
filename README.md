![Robot](https://github.com/vigenere23/iRondelle/workflows/Robot/badge.svg)
![Backend](https://github.com/vigenere23/iRondelle/workflows/Backend/badge.svg)
![Frontend](https://github.com/vigenere23/iRondelle/workflows/Frontend/badge.svg)

# Partially Supervised Autonomous Robot (PSAR)

![obstacle detection](https://user-images.githubusercontent.com/32545895/79995493-49afdb80-8485-11ea-9100-70d93fb9326a.gif)

> Obstacle detection

PSAR is a small robot built to do many tasks. It is mounted on a 4-wheel base equipped with a small camera and a gripper. There is also a top-view camera (called the *World camera*) to help with pathfinding. The robot is said to be *partially supervised* because its decisions are greatly help by 2 external factors : a top-view camera and aruco markers. 

The main goal is to take 3 pucks and place them on the corners or a square. The pucks to take, the deposit order and the corners on which to deposit the pucks are all determined by various detection tasks :

- Calculating a resistor value by analyzing the circuit's electric current and voltage
- Determining the orientation of a specific arrow from a set of 9
- Determining the letter at a specific position from a set of 9
- Determining the position of each stations on the table

Throughout the course, some obstacles (pillars) will be placed on the table. The system will have to detect them and find a path to dodge them. The overall goal is to complete as many rounds as possible in only 10 minutes. There is also a set of information to be displayed in real-time while the robot performs its tasks, like the internal state of the backend and robot, the consumption levels, the planned and real paths, etc.

Unfortunately, due to COVID-19 measures of prevention, the laboratory of experimentation was closed mid-semester, which prevented us to collect data and perform tests that were necessary for the completion of the project.

You can view the full report [here](./report_fr.pdf).

## Structure info

The complete project is seperated into 3 sub-projects :

1. [robot](./robot/)
2. [backend](./backend/)
3. [frontend](./frontend/)

For more general info about the project, the standards and the tools, **PLEASE** visit the [wiki](./wiki/README.md)!

## Quick setup

If your console is bash based, you can simply run the `setup` script.

```bash
./scripts/setup
```

## Main software contributors

- [GASTP33 (vigenere23)](https://github.com/vigenere23) (me)
- [DODRO35](https://github.com/DODRO35)

## Work I've done

- Architecture (simplified clean architecture) in all subprojects
- Sequence system with autonaumous tasks (with failure handling and retry system)
- Obstacle and robot detection
- Pathfinding algorithm and optimization
- Socket communication
- Enforcement of SOLID*T* principles
- Automatic dependency injection
- Optimizations in CI pipeline
- Frontend Vue setup and configuration (with optimized Vuetify plugin integration)
- Small part of UI design (sequence viewer and top bar)
- Assisted DODRO35 as a co-chief of the team
- Main reviewer (along with DODRO35)

## Known caveats

- There is a ton of missing tests. With the human ressources and the time available, we decided to put more effort into maximizing the number of features requested and relied on manual testing while developing.
- The frontend only has a small portion actually connected to the backend and the design could be further simplified and better decomposed into components (instead of relying on global classes)

## Additionnal screenshots

![interface](https://user-images.githubusercontent.com/32545895/79995525-559b9d80-8485-11ea-8eb5-da559d9e587b.png)

> Interface

![pathfinding](https://user-images.githubusercontent.com/32545895/79995535-57fdf780-8485-11ea-9db2-c3519ae6d9ab.png)

> Pathfinding

![pathfinding comparison](https://user-images.githubusercontent.com/32545895/79996265-3fdaa800-8486-11ea-9684-33518cf86680.png)

> Pathfinding : comparison between search grid creation algorithm (me) and path finding algorithm (library)

![letters detection](https://user-images.githubusercontent.com/32545895/79996432-757f9100-8486-11ea-8f18-fab6d475b798.jpg)

> Letters detection

![robot](https://user-images.githubusercontent.com/32545895/79996550-97791380-8486-11ea-922f-d490bf7130a2.jpg)

> Robot (upside-down)

![robot-moving](https://user-images.githubusercontent.com/32545895/79999160-9695b100-8489-11ea-904b-cf8804416c93.gif)

> Robot in action
