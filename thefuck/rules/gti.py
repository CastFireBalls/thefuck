"""
Fixes the common typo 'gti' → 'git'

Everyone who types fast has accidentally typed 'gti' instead of 'git'.
This rule catches that and corrects it.
"""


def match(command):
    return command.script_parts and command.script_parts[0] == 'gti'


def get_new_command(command):
    return 'git' + command.script[3:]
