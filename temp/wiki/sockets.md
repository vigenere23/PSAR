> **WARNING! WARNING! PLEASE READ [THIS](#sending-events)**

## Communication

The main communication method that will be used between the base station, the robot and the interface is based on the socket protocol. It's an event-based asynchronous method of communication that will help us achieve real-time communication, which is especially usefull for sending commands to the robot or displaying system informations on the interface without the need of constantly poolling. 

## Sockets

Since sockets are event-based, their implementation and support architecture differs greatly from the basic http. Each message that is beeing send does not wait for a response. That means there is a complete separation between the modules that handles the requests and those that "responds" to them. Here, by "responding" we mean sending a new event, but in the other direction. The modules that handles the receiving of data are called `event handlers` and those which sends the data, `event emitters`. 

On a socket-based communication, only 1 single server can exist. Others are called "socket clients" (or simply "clients"). The server is the only one that can broadcast messages (broadcast means sending a message to every client). Therefore, the server can communicate (in both ways) to both the robot and the interface, but the interface cannot directly communicate to the robot (events will need to be redistributed from the base station).

### Events

Events are the commands or actions. They basically correspond to the last element after the `/` in conventional REST routes (like in `/messages/create`, `create` will be the name of the event). Their name should follow the `snake_case` convention (**very important**) and should generally not be very long (usually 1 to 2 words). Every event is asynchronous and thus not necessarly sent or received in the wanted order. Fallback mecanisms should be put in place to prevent such asynchronous errors.

Normally, there are two types of event names :

- If an event specifies an action that should be made, the name should be a verb in the present tense, like `move` or `take_something`.
- If, in the contrary, the event indicates a change that has already been made, then it should be in the past tense, like `speed_changed` or `task_started`.

#### Sending events

There are 2 ways to send events :

- `send`: will only send to the connected client. This should **only** be used for:
    - interface to base-station
    - base-station to interface
    - robot to base-station
    - **DOES NOT WORK FROM BASE-STATION TO ROBOT!!!**
- `emit`: will broadcast the message to all the clients. This is only available from the base-station to the robot or interface.
    - **USE THIS FROM BASE-STATION TO ROBOT!!!**

### Messages / data / payload

This is the content of the event. It could either be a direct value (like an `int`, a `string` or an `array`) or it could be a more complex data type (usually a `dict` in Python, that will be transformed to `json`). This payload can only be a single element of data, so if multiple arguments need to be sent, they will need to be encapsulated in either an array (not prefered) or a dictionary (better). 

### Namespaces

Namespaces are what separated the routes for the different modules in the app. It usually corresponds to the word before the last `/` in a conventional REST route (like in `/messages/create`, `messages` will be the name of the namespace). Therefore, by using namespaces, event names should be simplier and should **not** contain the namespace in them. As an exemple, an event named `sequence_started` in the `sequence` namespace is totally wrong, as the word `sequence` is uselessly repeated. Simply `started` would be plenty enough.

For now, there are only 2 namespaces used in the app, since only 2 main modules exists : 

- `sequence`: Everything related to the execution of the sequence (and thus of each task).
- `robot`: Everything related to robot commands or information.

## Libraries used

- **Base station** : For the server, we will use the [`flask-socketio`](https://flask-socketio.readthedocs.io/en/latest/) library as it handles both the socket protocol, the WebSockets (for handling http sockets) and the creation of a web server. 
- **Robot** : For the robot, we will use the [`python-socketio-client`](https://python-socketio.readthedocs.io/en/latest/client.html) library for connecting to the socket server (base station). This library works quite like the `flask-socketio` if used with class-based namespaces (what we use). 
- **Interface** : Since the interface is programmed in js, we will use the well established [`Socket.IO`](https://socket.io/get-started/chat/) library. It is immensly simple and fun to use and should work right out of the box without any specific configuration. There's also a [Vue integration](https://www.npmjs.com/package/vue-socket.io) available to easily make the `socket` instance globally available.

[BACK](./README.md)
