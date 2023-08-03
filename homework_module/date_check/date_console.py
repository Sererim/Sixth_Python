from .date import date
from sys import argv


def console_call():
    raw = argv[1:]
    d = ""
    for x in raw:
        d += x
    print(date(d))
    

if __name__ == "__main__":
    console_call()
