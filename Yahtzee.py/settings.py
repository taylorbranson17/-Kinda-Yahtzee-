from os import system,name
from time import sleep
from clear import Clear

class Settings:

    def __init__(self):
        self.clear_instance = Clear()
        self.rounds = 5

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def sleep(self, duration: int=3):
        sleep(duration)