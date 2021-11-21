from cogs import *
from cogs.config import *
from cogs.boot import Boot
from cogs import fonts

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
    