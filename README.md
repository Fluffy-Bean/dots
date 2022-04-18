# Config Files

Fluffy's config files for Arch Linux, but should work on other distros.

## Colour Schemes

I did NOT make any of the colour schemes, so some of the config files cannot be included (so far just the Alacritty config)
Please refer to the original repositories for those

- [Paradise](https://github.com/Manas140/paradise)
- [Gruvbox](https://github.com/morhetz/gruvbox)

## How to use

### The dependencies

Yes, some stuff have dependencies

| App       | Extra configuration needed? |
|-----------|-----------------------------|
| Discord   | Yes   (BetterDiscord)       |
| Spotify   | Yes   (Spicetify)           |
| Polybar   | Yes   (Extensions)          |
| Alacritty | No                          |
| Firefox   | Yes   (Flags)               |
| Rofi      | No                          |

Please read through this as some things will not work just by copy and pasting into the .config folder.
If you feel like I missed a dependency, please contact me on the following:

- Issue on GitHub
- [Twitter](https://twitter.com/fluffybeanUwU)
- [Telegram](https://t.me/Fluffy_Bean)

### How to use configs

#### Discord

1. Download and install BetterDiscord
2. Move the themes from the Discord folder into the themes folder on BetterDiscord (usually under .config/BetterDiscord/themes)
3. Go into your discord settings
4. Under BetterDiscord section go into themes and choose (Gruvbox or Paradise)

#### Spotify

1. Download and install Spicetify
2. Install the marketplace extension
3. Install both Dribbblish theme and Custom CSS plugin
4. Go into the custom css section, F12 by default, and paste the colours.css code into the window that now opened

#### Polybar

1. Add text!

#### Firefox

1. Add text!

#### Rofi - Optional

1. Go into the rofi config file
2. Change the image

or

2. Remove the image overall and by editing line 70 out

## ToDo

- Make a script to automate all this
- Fix errors
- Finish README

## License

Open source UwU license
