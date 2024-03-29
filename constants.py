# constants.py


class Developer:
    version = '0.1.0'

class Internal:
    max_username_length = 16
    max_map_width  = 80
    max_map_height = 40

class Game:
    # Attack cooldown in ms
    lance_delay = 3000

class Map:
    space = ' '
    wall = '#'
    player_left = '<'
    player_right = '>'
    player_up = '^'
    player_down = 'v'
    lance_vertical = '|'
    lance_horizontal = '-'
    enemy = '@'


class Network:
    server_port = 2718 * 2 # 5436
