#db.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'superestrellas',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}