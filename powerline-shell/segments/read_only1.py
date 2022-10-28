import os

def add_read_only1_segment(powerline):
    cwd = powerline.cwd or os.getenv('PWD')

    if not os.access(cwd, os.W_OK):
        powerline.append('%s' % 'ro', Color.READONLY_FG, Color.READONLY_BG)
