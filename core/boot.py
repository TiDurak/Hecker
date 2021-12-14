from .config import *
from .core import Engine
import keyboard
from colorama import Fore, Back, Style

class Boot():
    def __init__(self):
        pass
    def startup(self):
        print(f'{Fore.GREEN}{settings["app_name"]} {settings["version"]} by {settings["author"]}')
        self.command = input(f'Нажмите Enter для продолжения, или введите комманду :) ')
        
        
        try:
            engine = Engine(self.command)
            engine.binary()
        except KeyboardInterrupt:
            print(Style.RESET_ALL + Fore.BLACK + Back.BLUE)
            print('Остановлено! Нажмите любую клавишу для закрытия')
            self.pause = keyboard.read_key()
    