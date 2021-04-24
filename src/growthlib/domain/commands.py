"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass


@dataclass
class AddGrowthCommand(Command):
    """
    This command is a dataclass that encapsulates a growth
    This uses type hints: https://docs.python.org/3/library/typing.html
    """
    id: int
    name: str
    Lname: str
    # data["date_added"] = datetime.utcnow().isoformat()
    url: str
    head:float
    weight:float
    hight:float
    age:int
    gender:str
    date_added: str
    date_edited: str
    notes: Optional[str] = None


@dataclass
class ListGrowthCommand(Command):
    order_by: str
    order: str


@dataclass
class DeleteGrowthCommand(Command):
    id: int


@dataclass
class EditGrowthCommand(Command):
    id: int
    name: str
    Lname: str
    url: str
    # data["date_added"] = datetime.utcnow().isoformat()
    head:float
    weight:float
    hight:float
    age:int
    gender:str
    date_added: str
    date_edited: str
    notes: Optional[str] = None
