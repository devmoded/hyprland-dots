# Требуемые пакеты:
## Основные
Hyprland, Waybar, Wofi, Kitty, Hyprpaper, Hyprlock, Nemo, nwg-look, swaync:
```bash
sudo pacman -S hyprland waybar wofi kitty hyprpaper hyprlock nemo nwg-look swaync
```

## SDDM:
```bash
sudo pacman -S sddm
systemctl enable sddm
```

## papirus-icon-theme:
```bash
pacman -S papirus-icon-theme
```

Установить [papirus-folders](https://github.com/PapirusDevelopmentTeam/papirus-folders) 
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
