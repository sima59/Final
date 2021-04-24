from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional


"""
Pure domain growth:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
date_edited TEXT NOT NULL
"""

class Growth:

    def __init__(self, id: int, name: str,Lname: str,url: str,head: float,weight: float,hight: float,age: int, gender: str, notes: str, date_added: datetime, date_edited: datetime):
        self.id = id
        self.name = name
        self.Lname = Lname
        self.url=url
        self.head = head
        self.weight = weight
        self.hight = hight
        self.age = age
        self.gender = gender
        self.notes = notes
        self.date_added = date_added
        self.date_edited = date_edited
        self.events = []
