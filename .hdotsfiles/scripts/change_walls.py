#!/usr/bin/env python3

import os

walls_path = '$HOME/.hdotsfiles/wallpapers'

print(f'Обои размещены в \'{walls_path}\'')
os.system(f'ls {walls_path}')
number_wall = input()

if number_wall == 'list':
    os.system('hyprctl hyprpaper listloaded')
else:
    os.system(f'hyprctl hyprpaper preload {walls_path}/{number_wall}.png')
    os.system(f'hyprctl hyprpaper wallpaper \', {walls_path}/{number_wall}.png\'')
