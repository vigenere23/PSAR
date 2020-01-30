import os

os.system('uwsgi --socket 0.0.0.0:5000 --protocol=http --enable-threads -w src.main:app')
