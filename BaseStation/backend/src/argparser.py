from argparse import ArgumentParser

__parser = ArgumentParser()
__parser.add_argument('-s', '--sequence', type=str, default='main')
__parser.add_argument('-e', '--event-type', type=str, default='socket')
args = __parser.parse_args()
