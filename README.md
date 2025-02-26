# Requirements
 * git
 * python3.9
 * poetry

# Installation
 ```bash
 # install poetry
 curl -sSL https://install.python-poetry.org | python3 -

 # download codes
 git clone https://github.com/dlont/barcode.git

 # install python dependencies in virtual environement
 cd barcode
 poetry install
 ```
# Usage

 ```bash
 poetry run python bc.py --help
 poetry run python bc.py "Hello, Inna" my_barcode
 ```