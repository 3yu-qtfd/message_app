import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

#.envファイルの相対パスを取得
dotenv_path = join(dirname(__file__), '.env')

#load_dotenv読み込み
load_dotenv(dotenv_path)

DBNAME = os.environ.get("DB_NAME")
USER = os.environ.get("USER_NAME")
PASS = os.environ.get("PASSWORD")
