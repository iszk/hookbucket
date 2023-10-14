# config application
# テスト用の config の内容を出力するだけのアプリケーション

"""
applicatin はみんな Result を返すようにする

"""

from returns.result import Success, Failure

from chalicelib import config

def show_config():
    c = config.config()

    ret = Success(c)
    return ret
