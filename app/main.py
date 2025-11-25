import sys


def main():
    sys.stdout.write("$ ")
    cmd = input()
    if cmd:
        print(f'{cmd}: command not found')


if __name__ == "__main__":
    main()
