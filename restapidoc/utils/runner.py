#!/usr/bin/env python

import argparse
from datetime import datetime
from restapidoc.restapidoc import parse, group_by_module, doc_template
from restapidoc.config import modules as module_description
from mako import exceptions
import codecs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--coverage", help="ouputs into stdin documentation coverage",
                        action="store_true", default=False)
    parser.add_argument("-d", "--dir", help="folder in which we need look for documentation annotation. default: test_src_folder/",
                        default="test_src_folder/")
    parser.add_argument("--filter", help="gob filter in which files to search. default: *Controler*.php",
                        default="*Controller*.php")
    parser.add_argument("-o", "--output", help="output filename. default: documentation.html",
                        default="documentation.html")
    args = parser.parse_args()

    blocks = parse(args.dir, args)
    grouped_blocks = group_by_module(blocks)
    try:
        output = doc_template.render(blocks=blocks, grouped_blocks=grouped_blocks,
                                     when=datetime.today(), modules=module_description)

        with codecs.open(args.output, "wb", encoding='utf-8') as f:
            f.write(output)
    except:
        print(exceptions.text_error_template().render())

if __name__ == '__main___':
    main()