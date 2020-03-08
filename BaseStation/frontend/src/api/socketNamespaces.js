import socketConfig from '../config/socket'
import { SocketConnectionFactory } from './SocketConnectionFactory'

const baseUrl = `${socketConfig.host}:${socketConfig.port}`
const socketConnectionFactory = new SocketConnectionFactory(baseUrl)

export const indexSocket = socketConnectionFactory.create('')
export const sequenceSocket = socketConnectionFactory.create('sequence')
export const debugRobotSocket = socketConnectionFactory.create('debug_robot')
