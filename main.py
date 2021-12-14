from core import *
from core.config import *
from core.boot import Boot
from core import fonts

import os
import colorama


class Main():
    def __init__(self):
        pass
    def setup(self):
        boot = Boot()
        boot.startup()
    
if __name__ == '__main__':
    colorama.init()
    font_change = fonts.ChangeFont('Segoe UI')
    main = Main()
    main.setup()
    