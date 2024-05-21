"""
   =|=-*-=-*-=-*-=-*-=*-=-*-=-*-=|=
    | Created by Adryan Maikel!  |
    | Date: 26/01/2024           |
    | Versão: 1.0                |
   =|=-*-=-*-=-*-=-*-=*-=-*-=-*-=|=

"""

from ngsconfig import PROJECT_NAME as pname, log_and_print as lprint

__version__ = "1.0"


def main():
    lprint(f"{pname} iniciado. Versão: {__version__}")


if __name__ == '__main__':
    main()
