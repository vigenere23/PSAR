from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

__parser = ArgumentParser(
    formatter_class=ArgumentDefaultsHelpFormatter
)

__parser.add_argument(
    '-s', '--serial-port', type=str, default='COM1',
    help='choose the serial port to use. Write \'fake\' for a fake one.'
)

args = __parser.parse_args()
