import io from 'socket.io-client'
const path = 'http://localhost:5000'
const socket = io.connect(path)
const sequenceSocket = io.connect(path + '/sequence')
const demoSocket = io.connect(path + '/debug_robot')
const logMessage = message => console.log(message)

const connect = () => {
  socket.on('connect', () => console.log('connected'))
}

const startSequence = () => sequenceSocket.emit('start')
const stopSequence = () => sequenceSocket.emit('stop')

socket.on('message', logMessage)

const move = (xSpeed, ySpeed) => {
  demoSocket.emit('move', { x: xSpeed, y: ySpeed })
  console.log(xSpeed, ySpeed)
}

export {
  connect,
  startSequence,
  stopSequence,
  move
}
