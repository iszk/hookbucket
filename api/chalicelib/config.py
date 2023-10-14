
import dataclasses
import os
from typing import Annotated, Any, Iterable

import toml
from pydantic import BaseModel, SecretStr, ValidationError

class ConfigGeneral(BaseModel):
    stage: str
    application_name: str

class ConfigFoo(BaseModel):
    hogehoge: str

class Config(BaseModel):
    general: ConfigGeneral
    foo: ConfigFoo

_config:Config|None = None

def config() -> Config:
    global _config
    if _config is None:
        _config = _read()
    return _config

def _read() -> Config:
    fname = os.environ.get("CONFIG_FILE") or "chalicelib/application_config.toml"
    obj = toml.load(fname)
    cfg = Config(**obj)
    print("👹")
    print(cfg)
    print(cfg.foo.hogehoge)
    return cfg
