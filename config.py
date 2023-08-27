# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PW = os.getenv("MYSQL_PW")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DBNAME = os.getenv("MYSQL_DBNAME")

class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': MYSQL_USER,
      'password': MYSQL_PW,
      'host': MYSQL_HOST,
      'db_name': MYSQL_DBNAME
  })

Config = SystemConfig