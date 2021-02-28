import os
import sys


# if os.path.isdir(upload_dir) is False:
# os.mkdir(upload_dir)

EXEC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'Password123'
    UPLOAD_FOLDER = os.path.join(EXEC_DIR, 'uploads')

    # Create the upload folder if its deleted
    if os.path.isdir(UPLOAD_FOLDER) is False:
        os.mkdir(UPLOAD_FOLDER)


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
