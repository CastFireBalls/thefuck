"""
Fixes 'git psuh' → 'git push' (and similar transpositions)

When your fingers get ahead of themselves and 'push' becomes 'psuh',
or 'puhs', or 'puss'.
"""

_typos = {'psuh', 'puhs', 'puss'}


def match(command):
    parts = command.script_parts
    return (len(parts) >= 2
            and parts[0] == 'git'
            and parts[1] in _typos)


def get_new_command(command):
    parts = command.script_parts
    parts[1] = 'push'
    return ' '.join(parts)
