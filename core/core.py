from .config import *
from colorama import Fore, Back, Style
import string
import random

class Engine():
    def __init__(self, boot_option = None):
        self.boot_option = boot_option
        self.__dictionaries = {
            'default': [0, 1],
            'english': list(string.ascii_lowercase),
            'chinese': ['牡', 'マ', 'キ', 'グ', 'ナ', 'ル' 'フ', 'ァ', '系', '路', '克', '瑞', '大', '阪', '市', '立', '学', '鎰', '命', '科', 'ャ', 'マ', '能', '伝', '力', '影', 'ϒ', '灯', '人', 'は', '谷', '妻', 'Ѫ', 'ス', '丹', 'サ', '通', 'テ', '要', '玉'],
            'arabic': [u'\u0624', u'\u0622', u'\u062a', u'\u062b', u'\u062c', u'\u0633', u'\u0634', u'\u0635', u'\u0636', u'\u0637', u'\u0638', u'\u06b4']
        }
    
    def binary(self):
        try:
            print(random.choice(self.__dictionaries[self.boot_option]), end='')
        except Exception as e:
            self.boot_option = 'default'
        while True:
            print(random.choice(self.__dictionaries[self.boot_option]), end='')
