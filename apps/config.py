from pathlib import Path

basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = "aaaaaaaaaa"
    WTF_CSRF_SECRET_KEY = "bbbbbbbbbbb"
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

config = {
    "local": LocalConfig
}