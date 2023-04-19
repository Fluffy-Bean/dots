# ----------------------------------------
#  Importing
# ----------------------------------------
#  Used to move workspaces and windows
from libqtile import layout
from libqtile.command import lazy
from libqtile.config import EzKey, Group, Match, Screen

from modules.keybinds import keys
from modules.themes import theme


# ----------------------------------------
#  Groups
# ----------------------------------------
#  Listing usable groups/workspaces
groups = [
    Group("1", label="1"),
    Group("2", label="2"),
    Group("3", label="3"),
    Group("4", label="4"),
    Group("5", label="5"),
    Group("6", label="6"),
    Group("7", label="7"),
    Group("8", label="8"),
    Group("9", label="9"),
]


# ----------------------------------------
#  Keybinds
# ----------------------------------------
#  Used to move view/application to
#  different workspace/group
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            EzKey("M-%s" % i.name, lazy.group[i.name].toscreen()),
            # mod1 + shift + letter of group => move focused window to group
            EzKey("M-S-%s" % i.name, lazy.window.togroup(i.name)),
        ]
    )
    
border = dict(
    border_focus=theme[0],
    border_normal=theme[3],
    border_width=0,
    margin=8,
)

layouts = [
    layout.MonadTall(**border, ratio=0.5),
    layout.MonadThreeCol(**border),
    layout.MonadWide(**border, ratio=0.69),
    layout.Spiral(**border),
    layout.Max(**border),
]
floating_layout = layout.Floating(
    **border,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(wm_class="pinentry"),  # GPG key password entry
        Match(title="Picture-in-Picture"),  # FireFox
        Match(wm_class="ssh-askpass"),  # ssh-askpass
    ],
)

screens = [ Screen() ]