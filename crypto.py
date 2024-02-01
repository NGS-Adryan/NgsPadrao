# -*- coding: utf-8 -*-

"""
    Arquivo contendo função para descriptografar a senha do banco vindo
do arquivo .ini e token.key.

    Função que recebe a senha griptografada e descriptografa.

>>> def decrypt_password(encrypted_password: bytes) -> str:

"""

from cryptography.fernet import Fernet

def decrypt_password(encrypted_password: bytes) -> str:
    """Função para descriptografar a senha do banco

    Args:
        encrypted_password (bytes): Passando a senha encriptografada

    Returns:
        str: Senha do banco
    """
    with open("token.key", "rb") as TOKEN:
        return  Fernet(TOKEN.read()).decrypt(encrypted_password).decode()


if __name__ == "__main__":
    print()