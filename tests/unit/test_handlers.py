from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from growthlib import bootstrap
from growthlib.domain import commands
from growthlib.services import handlers, unit_of_work
from growthlib.adapters import repository

from growthlib.adapters.orm import start_mappers
from growthlib.services.unit_of_work import FakeUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())


class TestAddGrowth:
    def test_add_single_growth(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.AddGrowthCommand(
                0,
                f"John",  # Name
                f"Smith", #Lname
                f"http://example.com",  # url
                35, #head
                28, #weight
                3, #hight
                2, #age
                f"boy", #gender
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.Growth.get_by_name(f"John") is not None
        assert bus.uow.committed

    def test_get_growth_by_id(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.AddGrowthCommand(
                85,
                f"John",  # Name
                f"Smith", #Lname
                f"http://example.com",  # url
                35, #head
                28, #weight
                3, #hight
                2, #age
                f"boy", #gender
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.Growth.get_by_id(85) is not None
        assert bus.uow.committed

    def test_get_growth_by_url(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.AddGrowthCommand(
                85,
                f"John",  # Name
                f"Smith", #Lname
                f"http://example.com",  # url
                35, #head
                28, #weight
                3, #hight
                2, #age
                f"boy", #gender
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.Growth.get_by_url(f"http://example.com") is not None
        assert bus.uow.committed

    def test_get_all_growth(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)        
        bus.handle(
            commands.AddGrowthCommand(
                85,
                f"John",  # Name
                f"Smith", #Lname
                f"http://example.com",  # url
                35, #head
                28, #weight
                3, #hight
                2, #age
                f"boy", #gender
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        nuto = nu + timedelta(days = 2, hours=12)

        bus.handle(
            commands.AddgrowthCommand(
                85,
                f"Lisa",  # Name
                f"Davice", #Lname
                f"http://example.com",  # url
                38, #head
                35, #weight
                3.5, #hight
                4, #age
                f"girl", #gender
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
        
            )
        )



        records = bus.uow.Growth.get_all()
        assert len(records) == 2