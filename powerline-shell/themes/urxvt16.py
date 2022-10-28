# Basic theme which only uses colors in 0-15 range

class Color(DefaultColor):
    USERNAME_FG = 3
    USERNAME_BG = 0
    USERNAME_ROOT_FG = 9

    HOSTNAME_FG = 0
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 8 # dark grey
    PATH_FG = 15 # light grey
    CWD_FG = 5 # white
    SEPARATOR_FG = 15 # same as PATH_FG

    READONLY_BG = 14
    READONLY_FG = 0

    REPO_CLEAN_BG = 2  # green
    REPO_CLEAN_FG = 15  # black
    REPO_DIRTY_BG = 9  # red
    REPO_DIRTY_FG = 15 # white

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 2
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 13
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0
