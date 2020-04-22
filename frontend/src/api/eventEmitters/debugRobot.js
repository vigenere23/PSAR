import { debugRobotSocket as socket } from '../socketNamespaces'

export function sendMove (speedX, speedY) {
  socket.emit('move', { x: speedX, y: speedY })
}
