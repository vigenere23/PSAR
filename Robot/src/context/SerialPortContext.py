from injector import Module, Binder
from src.argparser import args
from src.domain.robot.SerialPort import SerialPort
from src.infrastructure.serial_ports.RealSerialPort import RealSerialPort
from src.infrastructure.serial_ports.FakeSerialPort import FakeSerialPort


class SerialPortContext(Module):

    def configure(self, binder: Binder):
        if args.serial_port == 'fake':
            binder.bind(SerialPort, to=FakeSerialPort)
        else:
            binder.bind(SerialPort, to=RealSerialPort(args.serial_port))
