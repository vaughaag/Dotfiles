import re
import subprocess
import os

GIT_SYMBOLS = {
    'detached': 'dt',
    'ahead': 'ah',
    'behind': 'bh',
    'staged': 'st',
    'notstaged': 'ns',
    'untracked': 'ut',
    'conflicted': 'xx'
}

def get_PATH():
    """Normally gets the PATH from the OS. This function exists to enable
    easily mocking the PATH in tests.
    """
    return os.getenv("PATH")

def git_subprocess_env():
    return {
        # LANG is specified to ensure git always uses a language we are expecting.
        # Otherwise we may be unable to parse the output.
        "LANG": "C",

        # https://github.com/milkbikis/powerline-shell/pull/126
        "HOME": os.getenv("HOME"),

        # https://github.com/milkbikis/powerline-shell/pull/153
        "PATH": get_PATH(),
    }


def parse_git_branch_info(status):
    info = re.search('^## (?P<local>\S+?)''(\.{3}(?P<remote>\S+?)( \[(ahead (?P<ahead>\d+)(, )?)?(behind (?P<behind>\d+))?\])?)?$', status[0])
    return info.groupdict() if info else None


def _get_git_detached_branch():
    p = subprocess.Popen(['git', 'describe', '--tags', '--always'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         env=git_subprocess_env())
    detached_ref = p.communicate()[0].decode("utf-8").rstrip('\n')
    if p.returncode == 0:
        branch = u'{} {}'.format(GIT_SYMBOLS['detached'], detached_ref)
    else:
        branch = 'Big Bang'
    return branch


def parse_git_stats(status):
    stats = {'untracked': 0, 'notstaged': 0, 'staged': 0, 'conflicted': 0}
    for statusline in status[1:]:
        code = statusline[:2]
        if code == '??':
            stats['untracked'] += 1
        elif code in ('DD', 'AU', 'UD', 'UA', 'DU', 'AA', 'UU'):
            stats['conflicted'] += 1
        else:
            if code[1] != ' ':
                stats['notstaged'] += 1
            if code[0] != ' ':
                stats['staged'] += 1

    return stats


def _n_or_empty(_dict, _key):
    return _dict[_key] if int(_dict[_key]) > 1 else u''

def anti_vowel(text):
    vow = ["a", "e", "i", "o", "u", "y"]
    chars = []

    for i in text: #No need of the two separate loops
        if i.lower() not in vow:
            chars.append(i)

    return "".join(chars)

def add_git1_segment(powerline):
    try:
        p = subprocess.Popen(['git', 'status', '--porcelain', '-b'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             env=git_subprocess_env())
    except OSError:
        # Popen will throw an OSError if git is not found
        return

    pdata = p.communicate()
    if p.returncode != 0:
        return

    status = pdata[0].decode("utf-8").splitlines()

    branch_info = parse_git_branch_info(status)
    stats = parse_git_stats(status)
    dirty = (True if sum(stats.values()) > 0 else False)

    if branch_info:
        branch = branch_info['local']
    else:
        branch = _get_git_detached_branch()

    branch = anti_vowel(branch)

    bg = Color.REPO_CLEAN_BG
    fg = Color.REPO_CLEAN_FG
    if dirty:
        bg = Color.REPO_DIRTY_BG
        fg = Color.REPO_DIRTY_FG

    powerline.append('%s' % branch, fg, bg)

    def _add(_dict, _key, fg, bg):
        if _dict[_key]:
            _str = u'{}{}'.format(_n_or_empty(_dict, _key), GIT_SYMBOLS[_key])
            powerline.append(_str, fg, bg)

    if branch_info:
        _add(branch_info, 'ahead', Color.GIT_AHEAD_FG, Color.GIT_AHEAD_BG)
        _add(branch_info, 'behind', Color.GIT_BEHIND_FG, Color.GIT_BEHIND_BG)
    _add(stats, 'staged', Color.GIT_STAGED_FG, Color.GIT_STAGED_BG)
    _add(stats, 'notstaged', Color.GIT_NOTSTAGED_FG, Color.GIT_NOTSTAGED_BG)
    _add(stats, 'untracked', Color.GIT_UNTRACKED_FG, Color.GIT_UNTRACKED_BG)
    _add(stats, 'conflicted', Color.GIT_CONFLICTED_FG, Color.GIT_CONFLICTED_BG)
