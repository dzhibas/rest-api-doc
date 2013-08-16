import expressions as e
import re
from config import modules as module_description
import hashlib


class Param:
    def __init__(self, param):
        self.paramtype, self.name, self.type, self.rest = param
        self.required = False
        if "required" in self.rest.lower() and "not required" not in self.rest.lower():
            self.required = True
            self.rest = self.rest.replace("required", "")
        self.rest = self.rest.replace("not required", "")


class Example:
    def __init__(self, example):
        example_type, example_code = example
        self.type = example_type
        self.code = example_code

    def getcode(self):
        return self.code.encode("latin-1", errors='replace')


class Docblock:
    def __init__(self, block=""):
        self.file = ""
        self.module = ""
        self.route = ""
        self.method = ""
        self.group = ""
        self.examples = []
        self.params = []
        self.description = ""
        self.filename = ""
        self.returns = ""
        self.block = block
        self.working = True
        self.deprecated = False
        self.non_working = ""

        self.is_api_doc = False
        self.is_api_doc = self.parse()

    def parse(self):
        """
        parses dockblock and returns true if it's rest API dockblock
        false if it's not
        """

        if "@method" not in self.block or "@route" not in self.block:
            return False

        self.block = self.cleanup_docblock()

        self.route = self._get_route()
        self.method = self._get_method()
        self.group = self._get_group()
        self.returns = self._get_returns()
        self.params = self._get_params()
        self.non_working = self._get_non_working()

        self.examples = self._get_examples()

        # rest is considered to be as description
        self.description = self.block.strip()

        return True

    def uniq(self):
        return hashlib.sha224(self.method+self.route+self.getgroup()).hexdigest()

    def is_danger(self):
        if not self.working or self.deprecated:
            return "danger"
        return ""

    def cleanup_docblock(self):
        docblock = e.cleanup.sub(r"\1", self.block)
        docblock = re.sub(r"^ ", "", docblock, 0, re.M)
        return docblock[3:-2]

    def getgroup(self):
        if self.group != "":
            return self.group.lower()
        return self.module.lower()

    def get_module_desc(self):
        if self.getgroup() in module_description.keys():
            return module_description[self.getgroup()]
        return ""

    def _get_route(self):
        finds = e.route.findall(self.block)
        if len(finds) > 0:
            self.remove_code_block(e.route)
            return finds[0]
        return ""

    def _get_method(self):
        finds = e.method.findall(self.block)
        if len(finds) > 0:
            self.remove_code_block(e.method)
            return finds[0]
        return [0]

    def _get_group(self):
        finds = e.ingroup.findall(self.block)
        if len(finds) > 0:
            self.remove_code_block(e.ingroup)
            return finds[0]
        return ""

    def _get_returns(self):
        find = e.returns.findall(self.block)
        if len(find) > 0:
            self.remove_code_block(e.returns)
            return find[0]
        return ""

    def _get_params(self):
        found_params = e.params.findall(self.block)

        if len(found_params) > 0:
            self.remove_code_block(e.params)
            return [Param(p) for p in found_params]

        return []

    def _get_non_working(self):
        f = e.nonworking.findall(self.block)
        if len(f) > 0:
            self.remove_code_block(e.nonworking)
            t, m = f[0]
            if t.lower().strip() == "deprecated":
                self.deprecated = True
            else:
                self.working = False
            return m
        return ""

    def _get_examples(self):
        f = e.examples.findall(self.block)
        if len(f) > 0:
            self.remove_code_block(e.examples)
            return [Example(c) for c in f]
        return []

    def remove_code_block(self, pattern):
        self.block = pattern.sub("", self.block)

    def __str__(self):
        return "%s %s (%s)" % (self.method.upper(), self.route, self.group)
