import io from 'socket.io-client'

export class SocketConnectionFactory {
  constructor (baseUrl) {
    if (baseUrl[baseUrl.lenght - 1] === '/') {
      baseUrl = baseUrl.slice(0, -1)
    }
    this.baseUrl = baseUrl
  }

  create (namespace = '') {
    if (namespace[0] === '/') {
      namespace = namespace.slice(1, namespace.length)
    }

    return io.connect(`${this.baseUrl}/${namespace}`)
  }
}
