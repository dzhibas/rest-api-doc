#!/usr/bin/python

# -*- coding: utf-8 -*-

import codecs
from datetime import datetime
import os
import fnmatch
from parserapi import expressions as e
from parserapi.models import Docblock
from parserapi.config import modules as module_description

from mako.lookup import TemplateLookup
from mako import exceptions

import argparse

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

template_lookup = TemplateLookup(directories=['templates/'],
                                 input_encoding='utf-8', output_encoding='utf-8',
                                 encoding_errors='replace')

doc_template = template_lookup.get_template("doc.html")


def get_controllers(folder):
    for root, dirnames, filenames in os.walk(folder):
        for filename in fnmatch.filter(filenames, args.filter):
            yield os.path.join(root, filename)


def how_many_actions(code):
    return len(e.action.findall(code))


def get_actions(code):
    return e.action.findall(code)


def get_docblock(code):
    return e.docblock.findall(code)


def group_by_module(blocks):
    r = {}
    for b in blocks:
        group = b.getgroup()
        if group not in r.keys():
            r[group] = []
            r[group].append(b)
        else:
            r[group].append(b)
    return r


def parse(folder):
    methods_count = 0
    documentation_count = 0

    found_blocks = []
    for controller_filename in get_controllers(folder):
        f = codecs.open(controller_filename, "r", encoding='utf-8')
        code = "".join(f.readlines())
        f.close()

        methods_count += how_many_actions(code)

        blocks = get_docblock(code)

        if len(blocks) > 0:
            for b in blocks:
                module_name = e.module.findall(controller_filename)
                parsed_block = Docblock(b)
                parsed_block.filename = controller_filename

                if parsed_block.is_api_doc:
                    if len(module_name) > 0:
                        parsed_block.module = module_name[0]

                    found_blocks.append(parsed_block)
                    documentation_count += 1

    if args.coverage and methods_count > 0:
        print("Service documentation coverage")
        print("{0} service methods found and {1} documented. Coverage: {2}%".format(
              methods_count, documentation_count, documentation_count * 1. / methods_count * 100))

    return found_blocks


if __name__ == "__main__":
    blocks = parse(args.dir)
    grouped_blocks = group_by_module(blocks)
    try:
        output = doc_template.render(blocks=blocks, grouped_blocks=grouped_blocks,
                                     when=datetime.today(), modules=module_description)

        with codecs.open(args.output, "wb", encoding='utf-8') as f:
            f.write(output)
    except:
        print(exceptions.text_error_template().render())
