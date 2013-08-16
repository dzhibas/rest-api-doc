RESTful api documentation generation script
===================

Installation
==
pip install -r requirements.txt

Usage
==
python parse.py

Help
==
    usage: parse.py [-h] [-c] [-d DIR] [--filter FILTER] [-o OUTPUT]

    optional arguments:
      -h, --help            show this help message and exit
      -c, --coverage        ouputs into stdin documentation coverage
      -d DIR, --dir DIR     folder in which we need look for documentation
                            annotation. default: test_src_folder/
      --filter FILTER       gob filter in which files to search. default:
                            *Controler*.php
      -o OUTPUT, --output OUTPUT
                            output filename. default: documentation.html

open generated documentation.html