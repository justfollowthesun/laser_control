import os

# directories and files

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DESIGN_DIR = os.path.join(BASE_DIR, 'rsc')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
DB_DIR = os.path.join(BASE_DIR, 'src')
DB_PATH = os.path.join(DB_DIR, 'db.db')

# windows information

MY_COMPANY = "rudie"
MY_PRODUCT = "Hot-line my dairy"
MY_SUBPRODUCT = "calendar"
VERSION = "0.1"

# design / interface

UI_MAIN_WINDOW = os.path.join(DESIGN_DIR, 'table_diagram.ui')
UI_LOGIN_WINDOW = os.path.join(DESIGN_DIR, 'dialog_v2.ui')
