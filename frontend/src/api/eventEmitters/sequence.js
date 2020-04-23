import { sequenceSocket as socket } from '../socketNamespaces'

export function sendStartSequence () {
  socket.emit('start')
}

export function sendStopSequence () {
  socket.emit('stop')
}
