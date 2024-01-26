# -*- coding: utf-8 -*-

"""
    Arquivo contendo configurações e função para printar no terminal
e escrever no arquivo f'{PROJECT_NAME}_{DATE_START_PROGRAM}.log'

   =|=-*-=-*-=-*-=-*-=*-=-*-=-*-=-*-=-*-=-*-=-*-=|=
    |  Variáveis:                                |
    |    PROJECT_NAME: Nome do projeto           |
    |    DATE_START_PROGRAM: Data da execução    |
   =|=-*-=-*-=-*-=-*-=*-=-*-=-*-=-*-=-*-=-*-=-*-=|=

"""

import logging
from datetime import datetime

from ngsconfig import DIR_LOG, PROJECT_NAME

START_PROGRAM = datetime.now()
DATE_START_PROGRAM = START_PROGRAM.strftime('%Y-%m-%d')
HOUR_START_PROGRAM = START_PROGRAM.strftime('%H:%M:%S')

logging.basicConfig(
    filename=f'{DIR_LOG}{PROJECT_NAME}_{DATE_START_PROGRAM}.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%d-%b-%y %H:%M:%S'
)

def log_and_print(msg: str, level: int=logging.INFO) -> None:
    """Escreve no arquivo de logs e printar no terminal

    Args:
        msg (str): Menssagem a ser inserida no log
        level (int): Nível do log, por padrão é logging.INFO.

    Returns:
        None: Não tem retorno
    """
    print(msg)
    match level:
        case logging.INFO:
            return logging.info(msg)
        case logging.CRITICAL:
            return logging.critical(msg)
        case logging.ERROR:
            return logging.error(msg)
        case logging.WARNING:
            return logging.warning(msg)
        case logging.DEBUG:
            return logging.debug(msg)


if __name__ == '__main__':
    log_and_print('teste')
