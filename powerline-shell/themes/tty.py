# Basic theme which only uses colors in 0-7 range

class Color(DefaultColor):
    USERNAME_FG = 0
    USERNAME_BG = 3
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 0
    HOSTNAME_BG = 2

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 6
    PATH_FG = 0
    CWD_FG = 0 
    SEPARATOR_FG = 0

    READONLY_BG = 5
    READONLY_FG = 0

    REPO_CLEAN_BG = 2  # green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 3
    REPO_DIRTY_FG = 0

    JOBS_FG = 0
    JOBS_BG = 4

    CMD_PASSED_BG = 2
    CMD_PASSED_FG = 0
    CMD_FAILED_BG = 1
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    GIT_AHEAD_BG = 4
    GIT_AHEAD_FG = 0
    GIT_BEHIND_BG = 4
    GIT_BEHIND_FG = 0
    GIT_STAGED_BG = 2
    GIT_STAGED_FG = 0
    GIT_NOTSTAGED_BG = 5
    GIT_NOTSTAGED_FG = 0
    GIT_UNTRACKED_BG = 1
    GIT_UNTRACKED_FG = 0
    GIT_CONFLICTED_BG = 1
    GIT_CONFLICTED_FG = 0

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0
