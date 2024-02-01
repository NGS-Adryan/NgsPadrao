# NgsPadrao

## Configurar o *Ambiente virtual*

* Criar o ambiente

```cmd
python -m venv python
```

* Ativar o ambiente no *windows*

```bash
.\python\Scripts\activate
```

* Desativar o ambiente

```bash
deactivate
```

## Bibliotecas Utilizadas

1. **cryptography**
1. **oracledb**

Instalar as bibliotecas no *ambiente virtual*

```bash
pip install cryptography oracledb
```

## Gerar o arquivo *requirements.txt*

```bash
pip freeze > requirements.txt
```

## Instalar com base no arquivo *requirements.txt*

```bash
pip install -r requirements.txt
```

## Gerar o executável

```bash
pyinstaller --onefile main.py --icon icon.ico -n # filename_exe
```
