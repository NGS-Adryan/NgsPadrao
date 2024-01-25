import PyInstaller.__main__

from ngsconfig import PROJECT_NAME

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    f'-n {PROJECT_NAME}',
    '--add-data=token.key;.',
    '--add-data=NgsPadrao.ini;.'
])
