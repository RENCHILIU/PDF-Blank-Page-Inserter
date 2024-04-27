from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,  # Disable argv emulation
    'packages': ['PyQt5', 'PyPDF2'],
}

setup(
    app=APP,
    name="PDF Blank Page Inserter",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
