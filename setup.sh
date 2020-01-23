pyenv install $(cat .python-version)
pyenv local $(cat .python-version)
cd BaseStation/backend
pipenv --rm
pipenv install
cd -
cd Robot
pipenv --rm
pipenv install
cd -
