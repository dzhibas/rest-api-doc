# -*- coding: utf-8 -*-
import os
import codecs
import fnmatch
import expressions as e
from models import Docblock

from mako.lookup import TemplateLookup

template_lookup = TemplateLookup(directories=[os.path.join(os.path.dirname(__file__), 'templates/')],
                                 input_encoding='utf-8', output_encoding='utf-8',
                                 encoding_errors='replace')

doc_template = template_lookup.get_template("doc.html")


def get_controllers(folder, args):
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


def parse(folder, args):
    methods_count = 0
    documentation_count = 0

    found_blocks = []
    for controller_filename in get_controllers(folder, args):
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