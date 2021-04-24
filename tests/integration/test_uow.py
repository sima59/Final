import threading
import time
import traceback
from datetime import datetime, timezone
from typing import List
from unittest.mock import Mock
import pytest
from growthlib.domain.models import  Growth
from growthlib.services import unit_of_work

pytestmark = pytest.mark.usefixtures("mappers")


        
def insert_Growth(session, name: str,Lname: str ,url: str,head: float,weight:float,hight:float,age:int, gender:str, date_added: str, date_edited: str, notes: str=None, ):
    session.execute(
        """
        INSERT INTO growth (name,Lname,head,weight,hight,age,gender, url, notes, date_added, date_edited) 
        VALUES (:name, :url, :notes, :date_added, :date_edited)
        """,
        dict(
            name=name,
            Lname=Lname,
            head=head,
            weight=weight,
            hight=hight,
            age=age,
            gender=gender, 
            url=url,
            notes=notes,
            date_added=date_added,
            date_edited=date_edited,
        ),
    )

def test_can_retreive_growth(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_Growth(session, f"Test", f"http://example.com", nu.isoformat(), nu.isoformat())
    session.commit()

    Growth: Growth= None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        Growth = uow.Growth.get_by_name(f"John")
        assert Growth.name == f"John"
  

