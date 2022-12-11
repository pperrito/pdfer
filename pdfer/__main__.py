import sys
from .app import run_action

if len(sys.argv) < 3:
    print("Укажите команду и файл(ы), с которыми нужно работать")
    exit()

run_action(sys.argv[1], sys.argv[2:])
