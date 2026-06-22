from thefuck.rules.git_push_typo import match, get_new_command
from thefuck.types import Command


def test_match():
    assert match(Command('git psuh', ''))
    assert match(Command('git puhs', ''))
    assert match(Command('git puss', ''))
    assert match(Command('git psuh origin main', ''))
    assert not match(Command('git push', ''))
    assert not match(Command('git push origin main', ''))
    assert not match(Command('git', ''))
    assert not match(Command('ls', ''))


def test_get_new_command():
    assert get_new_command(Command('git psuh', '')) == 'git push'
    assert get_new_command(Command('git puhs', '')) == 'git push'
    assert get_new_command(Command('git puss', '')) == 'git push'
    assert get_new_command(Command('git psuh origin main', '')) == 'git push origin main'
