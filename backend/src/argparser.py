from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

__parser = ArgumentParser(
    formatter_class=ArgumentDefaultsHelpFormatter
)

__parser.add_argument(
    '-s', '--sequence', type=str, default='main',
    choices=['main', 'special-tasks', 'robot'],
    help='defines the set of tasks to run'
)

__parser.add_argument(
    '-e', '--event-type', type=str, default='socket',
    choices=['socket'],
    help="choose an event technology"
)

__parser.add_argument(
    '-c', '--camera', type=str, default='/dev/video2',
    help="choose the video device on which the camera is located"
)

__parser.add_argument(
    '-t', '--table', type=int, default=1,
    help="choose the table to load right calibrations. Between 1 and 6."
)

args = __parser.parse_args()
