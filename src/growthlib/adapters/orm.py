"""
Note: this is significantly refactored to use the Imperative (a.k.a. Classical) Mappings (https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings)
That would have been common in 1.3.x and earlier.
"""
import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)

from sqlalchemy.orm import registry, mapper, relationship
from sqlalchemy.sql.sqltypes import FLOAT, Float, REAL

from growthlib.domain.models import Growth

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = MetaData()

"""
Pure domain Growth:
id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
LName TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL,
date_edited TEXT NOT NULL,
head INTEGER,
weight INTEGER,
hight INTEGER,
Age INTEGER,
Gender TEXT
"""
Growth = Table(
    "Growth",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("Name", String(255)),
    Column("LName", String(255)),
    Column("url", String(255)),
    Column("head", Float),
    Column("weight", Float),
    Column("hight", Float),
    Column("age", Integer),
    Column("gender", Text),
    Column("notes", Text),
    Column("date_added", Text),
    Column("date_edited", Text),
)

def start_mappers():
    
    logger.info("starting mappers")
    # mapper_registry.map_imperatively(Growth, Growth)
    mapper(Growth, Growth)

