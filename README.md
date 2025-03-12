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

 # Printed barcodes

poetry run python3 bc.py --qr "Hello, Inna" my_barcode 
poetry run python3 bc.py --qr 'Aloke Kumar Das' aloke --ext png --no-print-text
poetry run python3 bc.py --qr 'Inna Makarenko' inna --ext png --no-print-text
poetry run python3 bc.py --qr 'Michael Korntheuer' michael --ext png --no-print-text
poetry run python3 bc.py --qr 'Yannick Allarad' yannick --ext png --no-print-text
poetry run python3 bc.py --qr 'Yifan Yang' yifan --ext png --no-print-text
poetry run python3 bc.py --qr '_top_left' tl --ext png --no-print-text
poetry run python3 bc.py --qr '_top_right' tr --ext png --no-print-text
poetry run python3 bc.py --qr '_bottom_left' bl --ext png --no-print-text
poetry run python3 bc.py --qr '_bottom_right' br --ext png --no-print-text
poetry run python3 bc.py --qr 'ROYCE' royce_cap --ext png --no-print-text
poetry run python3 bc.py --qr 'royce' royce --ext png --no-print-text
poetry run python3 bc.py --qr 'Yannick Allard' yannick --ext png --no-print-text
poetry run python3 bc.py --qr 'iihe' iihe --no-print-text --ext png
poetry run python3 bc.py --qr 'upt' upt --ext png --no-print-text
poetry run python3 bc.py --qr 'ipt' ipt --ext png --no-print-text
poetry run python3 bc.py --qr '18TESTBONDS_700' 18TESTBONDS_700 --ext png --no-print-text
poetry run python3 bc.py --qr '40TESTBONDS_700' 40TESTBONDS_700 --ext png --no-print-text
poetry run python3 bc.py --qr '18FUNCBONDS_400_500' 18FUNCBONDS_400_500 --ext png --no-print-text
poetry run python3 bc.py --qr '40FUNCBONDS_400_500' 40FUNCBONDS_400_500 --ext png --no-print-text
poetry run python3 bc.py --qr 'tb_top' tb_top --ext png --no-print-text
poetry run python3 bc.py --qr 'tb_bottom' tb_bottom --ext png --no-print-text
poetry run python3 bc.py --qr 'func_top' func_top --ext png --no-print-text
poetry run python3 bc.py --qr '_func_top' func_top --ext png --no-print-text
poetry run python3 bc.py --qr '_tb_bottom' tb_bottom --ext png --no-print-text
poetry run python3 bc.py --qr '_tb_top' tb_top --ext png --no-print-text
poetry run python3 bc.py --qr '_func_bottom' func_bottom --ext png --no-print-text