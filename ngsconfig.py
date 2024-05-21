"""Arquivo encarregado de configurar o projeto."""

from cryptography.fernet import Fernet

from configparser import ConfigParser
import logging as log
from datetime import datetime

START_PROGRAM = datetime.now()
PROJECT_NAME = "NgsPadrao"

CONFIG = ConfigParser()
CONFIG.read(f"src/{PROJECT_NAME}.ini")

NGS_CONFIG = CONFIG["config"]
EMP, DIR_LOG = NGS_CONFIG["emp"], NGS_CONFIG["diretorio_log"]

DB = CONFIG["database"]
ORACLE_USER, PASS_DB, CLIENT = DB["user"], DB["password"], DB["client_dir"]
HOST, PORT, SERVICE = DB["host"], int(DB["port"]), DB["service"]
with open("src/token.key", "rb") as TOKEN:
    ORACLE_PASS = Fernet(TOKEN.read()).decrypt(PASS_DB.encode()).decode()

DATE_START_PROGRAM = START_PROGRAM.strftime("%Y%m%d")

log.basicConfig(filename=f"{DIR_LOG}{PROJECT_NAME}_{DATE_START_PROGRAM}.log",
                filemode="a", level=log.INFO, datefmt="%d-%b-%y %H:%M:%S",
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def write_log(text: str, level: int = log.INFO):
    """Escreve no arquivo de logs.

    :param text: str - Menssagem a ser inserida no log.
    :param level: int - Nível do log. Padrão é log.INFO.
    """
    match level:
        case log.INFO:
            return log.info(text)
        case log.CRITICAL:
            return log.critical(text)
        case log.ERROR:
            return log.error(text)
        case log.WARNING:
            return log.warning(text)
        case log.DEBUG:
            return log.debug(text)


def log_and_print(text: str, level: int = log.INFO, end = "\n"):
    """Escreve no arquivo de logs e printar no terminal.

    :param text: str - Menssagem a ser printada e inserida no log.
    :param level: int - Nível do log. Padrão é log.INFO.
    :param end: str - O que vai conter no final do print. Padrão é "\\n".
    """
    print(text, end=end)
    write_log(text, level)


if __name__ == "__main__":
    log_and_print("Teste")
