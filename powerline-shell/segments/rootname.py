
def add_rootname_segment(powerline):
    import os
    #~ no quality control, bash only!
    if os.getenv('USER') == 'root':
        bg = Color.USERNAME_ROOT_BG
        fg = 0 # black
        rootname_prompt = '\\u'
        powerline.append(rootname_prompt, fg, bg)

