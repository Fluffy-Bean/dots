# Config Files

Fluffy's config files for Arch Linux!!!!!!!!!

## Colour Schemes and Scripts

I did NOT make any of the colour schemes, so some of the config files cannot be included (so far just the Alacritty config)
Please refer to the original repositories for those

- [Paradise](https://github.com/Manas140/paradise)
- [Gruvbox](https://github.com/morhetz/gruvbox)

There are also some scripts I did not make such as a Rofi bash script, [here's the original](https://github.com/adi1090x/polybar-themes/blob/master/simple/grayblocks/scripts/powermenu.sh)

## How to use

### The dependencies

Yes, some stuff have dependencies

| App       | Extra configuration needed? |
|-----------|-----------------------------|
| Discord   | Yes   (BetterDiscord)       |
| Spotify   | Yes   (Spicetify)           |
| Polybar   | Yes   (Scripts)             |
| Alacritty | Yes   (colours)             |
| Firefox   | Yes   (Flags)               |
| Rofi      | Optional                    |

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

This has [this spotify module](https://github.com/Jvanrhijn/polybar-spotify) as a dependency I cannot include, please put the script(s) in a scripts file

#### Firefox

1. Add text!

#### Rofi - Optional

Change the image (the raccoon is good though)

## ToDo

- Make a bash script to automate all this
- Fix errors
- Finish README

## Done

- Removed hard-coded directories mostly

## Licence

Open source UwU licence
