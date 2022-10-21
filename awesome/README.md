## Work in Progress

# Asewome WM

![](/images/001.png)

This is my first go at customzing Awesome. The config is roundly based on one of the Copycat themes; multicolour but I have removed much, changed and added my own touches.

I will be updating this repo as regularly as I can as I want to try and split the config files into a more logical form. 

A number of the widgets come from https://github.com/streetturtle/awesome-wm-widgets they work nicely and are minimul which I like. I have included within my dots but be sure to check the main repo for updates and credit.

*** NOTE***   The logout menu gives no additional prompt when you click shutdown, restart or logout.

I have removed a lot of the keybindings I use as they are for applications most people will not use as they are specific to my job. I have also tried to list all the dependancies below or include within the dots so the config should work for most people out of the box.

## Menu
Dmenu and Rofi both setup
dmenu keybinding mod + r
refi keybinding mod + shift + x

    -- Prompt
    awful.key({ modkey }, "r", function ()
    awful.util.spawn("dmenu_run") end,
              {description = "run dmenu", group = "launcher"}),
    awful.key({ modkey, "Shift"   }, "x", function ()
    awful.util.spawn("rofi -show drun -theme ") end,
              {description = "run dmenu", group = "launcher"}),

## Standards Apps / Keybindings

    local modkey       = "Mod4"
    local altkey       = "Mod1"
    local terminal     = "alacritty"
    local editor       = os.getenv("code") or "nvim"
    local browser      = "brave"
    local filemanager  = "pcmanfm"
    local emailclient  = "thunderbird"

### Terminal

As listed above and below, I use alacritty for terminal emulation. The keybinding is Mod + Return/Enter

    awful.key({ modkey,           }, "Return", function () awful.spawn(terminal) end,
              {description = "open a terminal", group = "launcher"}),
    awful.key({ modkey, "Control" }, "r", awesome.restart,

### File Manager, Web Browser and email

PcmanFM is setup as my file manager, brave as my browser and thunderbird as mail

    -- User programs
    -- if using multimonitor setup add and wish applications to spawn to a specific screen and tag edit below as
    --{ rule = { instance ="brave" },
    --  properties = {screen = 1, tag = "1"} }),
    awful.key({ modkey }, "q", function () awful.spawn(browser) end,
              {description = "open a browser", group = "launcher"},
              { rule = { instance ="brave" },
                properties = {tag = "1"} }),
    awful.key({ modkey,           }, "e", function () awful.spawn(filemanager) end,
              {description = "open a file manager", group = "launcher"},
              { rule = { instance ="pcmanfm" },
                properties = {tag = "3"} }),
    awful.key({ modkey,           }, "a", function () awful.spawn(emailclient) end,
              {description = "open  email", group = "launcher"},
              { rule = { instance ="thunderbird" },
                properties = {tag = "5"} }),

### Autostart
Nitrogen will need to run and have a wallpaper set, after that it should remember and restore.

    --Autostart
    awful.spawn.with_shell("picom")
    awful.spawn.with_shell("nitrogen --restore")
    awful.spawn.with_shell("nm-applet")
    awful.spawn.with_shell("volumeicon")
    awful.spawn.with_shell("lxsession")





## Dependencies 

    alacritty
    brave
    dmenu
    rofi
    freedesktop
    lain
    nitrogen
    picom
    networkmanager
    lxappearance
    alsa-utils
    alsa-plugins

For Arch

    sudo pacman -S dmenu rofi alacritty brave-bin picom networkmanager lxappearance alsa-utils alsa-plugins nitrogen

Theme : Otis Forest - https://www.gnome-look.org/p/1619506 

Icons : Breeze Dark White - https://store.kde.org/p/1259380

The wallpaper pictures is included.

For the widgets, as mentioned above they are from the below linked repo. Check it out for updates, issues and credit for the work.
https://github.com/streetturtle/awesome-wm-widgets 




