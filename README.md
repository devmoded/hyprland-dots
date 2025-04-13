# Требуемые пакеты:
## Основные
Hyprland, Waybar, Wofi, Kitty, Hyprpaper, Hyprlock, Nemo, nwg-look, swaync, hyprpolkitagent, xdg-desktop-portal-hyprland:
```bash
sudo pacman -S hyprland waybar wofi kitty hyprpaper hyprlock nemo nwg-look swaync hyprpolkitagent xdg-desktop-portal-hyprland
```
## Дополнительные
NeoVim, Zed, Obsidian, OBS Studio, Steam, Telegram, Loupe:
```bash
sudo pacman -S nvim zed obsidian obs-studio steam telegram-desktop loupe
```

## SDDM:
```bash
sudo pacman -S sddm
systemctl enable sddm
```

### Установка темы SDDM:

Для SDDM используется тема [simple-sddm](https://github.com/JaKooLit/simple-sddm/tree/main)

Установить `qt5-quickcontrols2, qt5-graphicaleffects, qt5-svg`

```bash
sudo pacman -S qt5-quickcontrols2 qt5-graphicaleffects qt5-svg
```

1. Открыть терминал и ввести:
```bash
git clone https://github.com/JaKooLit/simple-sddm.git ~/simple-sddm
```
2. Перенести:
```bash
sudo mv ~/simple-sddm /usr/share/sddm/themes/
```
3. Поставить тему в конфиге SDDM:
```bash
sudo nano /usr/lib/sddm/sddm.conf.d/default.conf
---

[Theme]
Current=simple-sddm
...
```

### Настройка темы SDDM:

```bash
sudo cp $HOME/.hdotsfiles/wallpapers/2.png /usr/share/sddm/themes/Backgrounds/eos_dark.png
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

## papirus-icon-theme:
```bash
pacman -S papirus-icon-theme
```

Установить [papirus-folders](https://github.com/PapirusDevelopmentTeam/papirus-folders?tab=readme-ov-file#papirus-installer) в HOME
```bash
papirus-folders -C green
```

## orchis-green-dark:
Установить [orchis-theme](https://github.com/vinceliuice/Orchis-theme)
```bash
./install -t green
```

## [Hyprshot](https://github.com/Gustash/Hyprshot):
```bash
yay -S hyprshot
```

## [wlogout](https://github.com/ArtsyMacaw/wlogout):
```bash
yay -S wlogout
```

## Шрифты:
```bash
sudo pacman -S noto-fonts noto-fonts-extra noto-fonts-emoji ttf-font-awesome otf-font-awesome ttf-jetbrains-mono ttf-jetbrains-mono-nerd ttf-montserrat otf-montserrat
```
