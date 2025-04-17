#!/usr/bin/env python3

import os

walls_path = '$HOME/.hdotsfiles/wallpapers' # Путь до каталога с обоями

print(f'Обои размещены в \'{walls_path}\'') # Вывод пути до каталога с обоями
os.system(f'ls {walls_path}') # Вывод доступных элементов в каталоге с обоями

main_input = input() # Получение введённого текста или номера

def set_wall(path, wall_num):
    os.system(f'hyprctl hyprpaper preload {walls_path}/{path}/{wall_num}.png') # Презагрузка обоев
    os.system(f'hyprctl hyprpaper wallpaper \', {walls_path}/{path}/{wall_num}.png\'') # Установка обоев

if main_input == 'list':
    os.system(f'cat {walls_path}/.walls_summary.txt') # Вывод доступных обоев с описанием в их каталогах (требуется изменять файл)
    main_input = input()
if main_input == 'dark':
    os.system(f'ls {walls_path}/dark')

    main_input = input()
    set_wall('dark', main_input)
if main_input == 'light':
    os.system(f'ls {walls_path}/light')

    main_input = input()
    set_wall('light', main_input)
else:
    print('Error')
