import os

# directories and files

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DESIGN_DIR = os.path.join(BASE_DIR, 'rsc')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

DB_DIR = os.path.join(BASE_DIR, 'databases')
DB_LOGIN_PATH = os.path.join(DB_DIR, 'users.db')
DB_TIMERS_PATH = os.path.join(DB_DIR, 'timers.db')
DB_PATH = os.path.join(DB_DIR, 'database.db')

# windows information

MY_COMPANY = "rudie"
MY_PRODUCT = "Hot-line my dairy"
MY_SUBPRODUCT = "calendar"
VERSION = "0.1"

# design / interface

UI_MAIN_WINDOW = os.path.join(DESIGN_DIR, 'main_window.ui')

UI_ERRORS_WINDOW = os.path.join(DESIGN_DIR, 'errors.ui')
UI_TIMERS_WINDOW = os.path.join(DESIGN_DIR, 'timers.ui')
UI_LOGIN_WINDOW = os.path.join(DESIGN_DIR, 'login.ui')
UI_FILTERS_WINDOW = os.path.join(DESIGN_DIR, 'filters.ui')
#production

DEBUG = True
