from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import Growth

# from database import DatabaseManager

# module scope
# 


class Event(ABC):
    pass


@dataclass
class GrowthAdded(Event):
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


@dataclass
class GrowthEdited(Event):
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


@dataclass
class GrowthListed(Event):
    Growth: list[Growth]


@dataclass
class GrowthDeleted(Event):
    Growth: Growth



