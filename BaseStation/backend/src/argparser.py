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

args = __parser.parse_args()
