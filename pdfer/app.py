from .services import services
from pathlib import Path
import os


def run_action(action, params):
    for service in services:
        if service.command == action:
            service(params).run_action()
            exit(0)
    print("Неизвестная команда. Доступные команды:")
    for s in services:
        print(f"{s.command} - {s.doc}")


def main():
    while True:
        for i, a in enumerate(services, start=1):
            print(f"[{i}] {a.command} - {a.doc}")
        print("[0] Выйти")
        choice = int(input("Выберите: "))

        if choice == 0:
            exit(0)

        if choice > 0 and choice < len(services):
            services[choice - 1](input("Параметры: ")).run_action()

        os.system("cls")


if __name__ == "__main__":
    main()
