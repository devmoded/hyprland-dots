# 🪪 Main part

> [!WARNING]
> The project is no longer being developed.

> [!WARNING]
> This text was translated using Google Translate.

<p align=center>
    <a href="https://github.com/devmoded/hyprland-dots/blob/main/README.md">
        <img height=25px alt="README-ru badge" src="https://img.shields.io/badge/README-ru-blue?style=flat-square">
    </a>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/devmoded/hyprland-dots/blob/main/README-en.md">
        <img height=25px alt="README-en badge" src="https://img.shields.io/badge/README-en-blue?style=flat-square">
    </a>
</p>

## Programs
🎛️ **Bar:** `waybar` (Based on configs from [Andrey0189/hyprland-rice](https://github.com/Andrey0189/hyprland-rice) and [lgaboury/Sway-Waybar-Install-Script](https://github.com/lgaboury/Sway-Waybar-Install-Script/tree/master/.config/waybar))<br>
🖥️ **Display manager:** `sddm` (Based on the config from [JaKooLit/simple-sddm](https://github.com/JaKooLit/simple-sddm/tree/main))<br>
💻 **Terminal:** `kitty`<br>
🗃️ **File manager:** `nemo`<br>
📹 **Video player:** `vlc`<br>
⌨️ **Code editor:** `zed`, `neovim`<br>

## Content
- [Screenshots](#%EF%B8%8F-screenshots)
- [Installation, configuration](#%EF%B8%8F-installation-configuration)
- [Required packages](#required-packages)
- [Advice](#if)

## 🖼️ Screenshots
![Background](hdots_screenshots/background.png)
![Some apps](hdots_screenshots/some_apps.png)
![Pixel background](hdots_screenshots/background_pixeled.png)

# ⚙️ Installation, configuration

## Installing everything:

```bash
sudo pacman -S hyprland waybar wofi kitty hyprpaper hyprlock nemo nwg-look swaync hyprpolkitagent xdg-desktop-portal-hyprland
sudo pacman -S nvim zed obsidian obs-studio steam telegram-desktop loupe cool-retro-term xreader libreoffice-fresh libreoffice-fresh-ru btop timeshift fastfetch vlc
sudo pacman -S noto-fonts noto-fonts-extra noto-fonts-emoji ttf-font-awesome otf-font-awesome ttf-jetbrains-mono ttf-jetbrains-mono-nerd ttf-montserrat otf-montserrat
sudo pacman -S sddm
systemctl enable sddm
sudo pacman -S qt5-quickcontrols2 qt5-graphicaleffects qt5-svg
git clone https://github.com/JaKooLit/simple-sddm.git ~/simple-sddm
sudo mv ~/simple-sddm /usr/share/sddm/themes/
git clone https://github.com/devmoded/hyprland-dots.git
cd hyprland-dots
mv .hdotsfiles $HOME
mv .icons $HOME
mv .config $HOME/.config
sudo cp $HOME/.hdotsfiles/wallpapers/dark/2.png /usr/share/sddm/themes/Backgrounds/eos_dark.png
pacman -S papirus-icon-theme
yay -S hyprshot wlogout
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
```
*\* Detailed setup instructions below*
<br>
*\*\* You also need to install a theme [orchis-theme](#orchis-green-dark)*

---

### Description:

#### Necessary and other packages:

```bash
sudo pacman -S hyprland waybar wofi kitty hyprpaper hyprlock nemo nwg-look swaync hyprpolkitagent xdg-desktop-portal-hyprland
sudo pacman -S nvim zed obsidian obs-studio steam telegram-desktop loupe cool-retro-term xreader libreoffice-fresh libreoffice-fresh-ru btop timeshift fastfetch vlc
sudo pacman -S noto-fonts noto-fonts-extra noto-fonts-emoji ttf-font-awesome otf-font-awesome ttf-jetbrains-mono ttf-jetbrains-mono-nerd ttf-montserrat otf-montserrat
```

#### SDDM:

```bash
sudo pacman -S sddm
systemctl enable sddm
sudo pacman -S qt5-quickcontrols2 qt5-graphicaleffects qt5-svg
git clone https://github.com/JaKooLit/simple-sddm.git ~/simple-sddm
sudo mv ~/simple-sddm /usr/share/sddm/themes/
```

#### Dotfiles:

```bash
git clone https://github.com/devmoded/hyprland-dots.git
cd hyprland-dots
mv .hdotsfiles $HOME
mv .icons $HOME
mv .config $HOME/.config
sudo cp $HOME/.hdotsfiles/wallpapers/dark/2.png /usr/share/sddm/themes/Backgrounds/eos_dark.png
```

#### Other:

```bash
pacman -S papirus-icon-theme
yay -S hyprshot wlogout
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
```

## Required packages:
### Main
Hyprland, Waybar, Wofi, Kitty, Hyprpaper, Hyprlock, Nemo, nwg-look, swaync, hyprpolkitagent, xdg-desktop-portal-hyprland:
```bash
sudo pacman -S hyprland waybar wofi kitty hyprpaper hyprlock nemo nwg-look swaync hyprpolkitagent xdg-desktop-portal-hyprland
```
### Additional
NeoVim, Zed, Obsidian, OBS Studio, Steam, Telegram, Loupe, Cool Retro Term, Xreader, LibreOffice, Btop, Timeshift, Fastfetch, VLC:
```bash
sudo pacman -S nvim zed obsidian obs-studio steam telegram-desktop loupe cool-retro-term xreader libreoffice-fresh libreoffice-fresh-ru btop timeshift fastfetch vlc
```

### Fonts:
```bash
sudo pacman -S noto-fonts noto-fonts-extra noto-fonts-emoji ttf-font-awesome otf-font-awesome ttf-jetbrains-mono ttf-jetbrains-mono-nerd ttf-montserrat otf-montserrat
```

---

### SDDM:
```bash
sudo pacman -S sddm
systemctl enable sddm
```

#### **Installing SDDM Theme**:

The theme is used for SDDM [simple-sddm](https://github.com/JaKooLit/simple-sddm/tree/main)

Install `qt5-quickcontrols2, qt5-graphicaleffects, qt5-svg`

```bash
sudo pacman -S qt5-quickcontrols2 qt5-graphicaleffects qt5-svg
```

1. Open terminal and enter:
```bash
git clone https://github.com/JaKooLit/simple-sddm.git ~/simple-sddm
```
2. Transfer files:
```bash
sudo mv ~/simple-sddm /usr/share/sddm/themes/
```
3. Set the theme in the SDDM config:
```bash
sudo nano /usr/lib/sddm/sddm.conf.d/default.conf
---

[Theme]
Current=simple-sddm
...
```

#### **SDDM Theme Setup**:

```bash
sudo cp $HOME/.hdotsfiles/wallpapers/dark/2.png /usr/share/sddm/themes/Backgrounds/eos_dark.png
```

```bash
sudo nano /usr/share/sddm/themes/simple-sddm/theme.conf
---

[General]
Background="Backgrounds/eos_dark.png"
...
MainColor="#3cb478"
...
AccentColor="#3cb478"
...
BackgroundColor="#151515"
```

---

### papirus-icon-theme:
```bash
pacman -S papirus-icon-theme
```

Install [papirus-folders](https://github.com/PapirusDevelopmentTeam/papirus-folders?tab=readme-ov-file#papirus-installer) в HOME
```bash
papirus-folders -C green
```

### orchis-green-dark:
Install [orchis-theme](https://github.com/vinceliuice/Orchis-theme)
```bash
./install -t green
```

---

### [Hyprshot](https://github.com/Gustash/Hyprshot):
```bash
yay -S hyprshot
```

### [wlogout](https://github.com/ArtsyMacaw/wlogout):
```bash
yay -S wlogout
```

---

### NeoVim:
[NvChad](https://nvchad.com/) is used
```bash
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
```
```nvim
:MasonInstallAll
```
Remove `.git` directory from `.config/nvim/`

---

# If:
## Applications in wofi are opened via xterm:
In `/usr/share/applications/` find the `.desktop` file of the desired application and in the line
```bash
...
Exec=*kitty <and the command to execute (eg: vim)>
Terminal=false
```
\**(for example kitty)*
