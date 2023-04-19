# Original script made by https://github.com/Icy-Thought
# Ajusted by Fluffy for his use

from typing import List

from modules.workspaces import floating_layout, groups, layouts, screens
from modules.keybinds import keys, mouse

import modules.autostart

auto_fullscreen = True
auto_minimize = False
bring_front_click = True
cursor_warp = False

dgroups_app_rules = []
dgroups_key_binder = None
dpi_scale = 1.0

focus_on_window_activation = "smart"
follow_mouse_focus = False
reconfigure_screens = True

wmname = "Qtile"