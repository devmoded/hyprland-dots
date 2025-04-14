#!/usr/bin/env python3

import os

walls_path = '$HOME/.hdotsfiles/wallpapers'

print(f'Обои размещены в \'{walls_path}\'')
os.system(f'ls {walls_path}')

number_wall = input()

if number_wall == 'list':
    os.system(f'cat {walls_path}/.walls_summary.txt')
    number_wall = input()
if number_wall == 'dark':
    os.system(f'ls {walls_path}/dark')

    number_wall = input()
    os.system(f'hyprctl hyprpaper preload {walls_path}/dark/{number_wall}.png')
    os.system(f'hyprctl hyprpaper wallpaper \', {walls_path}/dark/{number_wall}.png\'')
if number_wall == 'light':
    os.system(f'ls {walls_path}/light')

    number_wall = input()
    os.system(f'hyprctl hyprpaper preload {walls_path}/light/{number_wall}.png')
    os.system(f'hyprctl hyprpaper wallpaper \', {walls_path}/light/{number_wall}.png\'')
else:
    print('Error')
