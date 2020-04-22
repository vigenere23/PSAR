import { indexSocket as socket } from '../socketNamespaces'

export function on (eventName, callback) {
  return socket.on(eventName, callback)
}
