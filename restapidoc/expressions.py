import re

action = re.compile(r"\s+public function (\w+)Action\(", re.S | re.I)

docblock = re.compile(r"((?:\/\*(?:[^*]|(?:\*+[^*\/]))*\*+\/))", re.M | re.S)
cleanup = re.compile(r"^\s+\*(.*?)$", re.M)

route = re.compile(r"^@route (.*)$", re.M)
ingroup = re.compile(r"^@(?:ingroup|group) (.*)$", re.M)
method = re.compile(r"^@method (.*)$", re.M)

returns = re.compile(r"^@(?:json_return|return|returns) (.*)$", re.M)

nonworking = re.compile(r"^@(notworking|deprecated) (.*)$", re.M)

# returns four groups: param_type, argname, type, description
params = re.compile(r"^@(?P<param_type>url|json|get|post)_?params? (?P<arg>[\w\.]+)(?: (?P<type>\w+)(?: (?P<else>.*?))?)?$", re.M | re.I)

examples = re.compile(r"@example (?P<type>\w+)\s*(?P<example>^(?:(?!@example).)*)", re.I | re.S | re.M)

module = re.compile(r"modules/(\w+)/controllers/", re.I)
