from pydantic import BaseModel, Field
from returns.result import Failure

CODE_UNKNOWN = 'unknown'

class Summary(BaseModel):
    code: str
    option: str | None = Field(default=None)
    message: str

class Error(Exception):
    def __init__(self, summary:Summary|None, cause:Exception|None=None):
        self.cause = cause
        self.summaries:list[Summary] = []
        if summary:
            self.summaries.append(summary)


"""
# handler層
user に見せる為に詰め替える
エラーコード+OPTION +MESSAGE に詰め替える
実際は message を足すくらいか

# application
エラーコードとかの形にしておく
AUTH, SERVER, CLIENTの3つくらいのエラーがあればよいか
厳密にはauthもclientの一種だけどまあいい

[ { error_code, option } ]
みたいな感じ



# それ以下
それなりに好きなようにしていい

"""
