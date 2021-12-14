import ctypes

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    LF_FACESIZE = 32
    def __init__(self):
        pass
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

class ChangeFont():
    def __init__(self, fontface):
        self.__STD_OUTPUT_HANDLE = -11
        self.__font = CONSOLE_FONT_INFOEX()
        self.__font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
        self.__font.nFont = 12
        self.__font.dwFontSize.X = 8
        self.__font.dwFontSize.Y = 16
        self.__font.FontFamily = 54
        self.__font.FontWeight = 400
        self.__font.FaceName = fontface
        self.__setup()
        

    def __setup(self):
        handle = ctypes.windll.kernel32.GetStdHandle(self.__STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(self.__font))