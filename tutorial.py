import colorama
from colorama import Fore, Back, Style
from termcolor import colored
colorama.init(autoreset=True)
print(Fore.RED + 'red text')
print('hello')
print(colored('python', 'green', attrs=['bold']))