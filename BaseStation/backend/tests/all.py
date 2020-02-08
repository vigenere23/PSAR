import os

def run_all():
  os.system("python -m unittest discover -s tests -p '*Test.py'")

if __name__ == '__main__':
  run_all()
