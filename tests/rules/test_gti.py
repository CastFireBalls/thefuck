from thefuck.rules.gti import match, get_new_command
from thefuck.types import Command


def test_match():
    assert match(Command('gti', ''))
    assert match(Command('gti status', ''))
    assert match(Command('gti push origin main', ''))
    assert not match(Command('git', ''))
    assert not match(Command('git status', ''))
    assert not match(Command('ls', ''))


def test_get_new_command():
    assert get_new_command(Command('gti', '')) == 'git'
    assert get_new_command(Command('gti status', '')) == 'git status'
    assert get_new_command(Command('gti push origin main', '')) == 'git push origin main'
