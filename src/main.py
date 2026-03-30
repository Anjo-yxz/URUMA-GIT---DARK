from Bot.UrumaBot import UrumaBot
from Full.Logo import Logo
from colorama import Fore,Style

class Main:
    def __init__(self):
        pass
    
    def execute(self):
        print(Logo())
        print('\n')
        UrumaBot().execute()

if __name__ == '__main__':
    Main().execute()