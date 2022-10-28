
def add_username1_segment(powerline):
    import os
    if powerline.args.shell == 'bash':
        user_prompt = '\\u'
    elif powerline.args.shell == 'zsh':
        user_prompt = '%n'
    else:
        user_prompt = '%s' % os.getenv('USER')

    if os.getenv('USER') == 'root':
        fgcolor = Color.USERNAME_ROOT_FG
    else:
        fgcolor = Color.USERNAME_FG

    powerline.append(user_prompt, fgcolor, Color.USERNAME_BG)
