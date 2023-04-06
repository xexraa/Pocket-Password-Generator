import configparser


config = configparser.ConfigParser()
config.read('config.ini')

FONT_TYPE = config.get('DEFAULT', 'FONT_TYPE')
FONT_SIZE = 30
SET_DEFAULT_EMAIL_OR_USERNAME = config.get('DEFAULT', 'SET_DEFAULT_EMAIL_OR_USERNAME')
MIN_LETTERS = config.getint('DEFAULT', 'MIN_LETTERS')
MAX_LETTERS = config.getint('DEFAULT', 'MAX_LETTERS')
MIN_SYMBOLS = config.getint('DEFAULT', 'MIN_SYMBOLS')
MAX_SYMBOLS = config.getint('DEFAULT', 'MAX_SYMBOLS')
MIN_NUMBERS = config.getint('DEFAULT', 'MIN_NUMBERS')
MAX_NUMBERS = config.getint('DEFAULT', 'MAX_NUMBERS')
