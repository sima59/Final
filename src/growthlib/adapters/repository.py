from abc import ABC, abstractmethod
from datetime import datetime

# making use of type hints: https://docs.python.org/3/library/typing.html
from typing import List, Set

from sqlalchemy.sql.sqltypes import Float, Integer

from growthlib.adapters import orm
from growthlib.domain.models import Growth


class AbstractGrowthRepository(ABC):
    def __init__(self):
        # seen is in reference to events detected
        self.seen = set()

    def add(self, Growth: Growth) -> None:
        # add to repo
        self._add(Growth)
        # add to event list
        self.seen.add(Growth)

    def get_all(self) -> list[Growth]:
        Growth: list[Growth] = self._get_all()
        if Growth:
            self.seen.update(Growth)
        return Growth

    def get_by_id(self, value: int) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_id(value)
        if Growth:
            self.seen.add(Growth)
        return Growth        

    def get_by_name(self, value: str) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_name(value)
        if Growth:
            self.seen.add(Growth)
        return Growth

    def get_by_Lname(self, value: str) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_Lname(value)
        if Growth:
            self.seen.add(Growth)
        return Growth

    def get_by_head(self, value: float) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_head(value)
        if Growth:
            self.seen.add(Growth)
        return Growth    

    def get_by_weight(self, value: float) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_weight(value)
        if Growth:
            self.seen.add(Growth)
        return Growth   


    def get_by_age(self, value: Integer) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_age(value)
        if Growth<20:
            self.seen.add(Growth)
              
        return Growth   

    def get_by_gender(self, value: str) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_gender(value)
        if Growth:
            self.seen.add(Growth)
        return Growth   


    def get_by_hight(self, value: float) -> Growth:
        # get from repo
        Growth: Growth = self._get_by_hight(value)
        if Growth:
            self.seen.add(Growth)
        return Growth   


    @abstractmethod
    def _add(self, Growth: Growth) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _add_all(self, Growth: list[Growth]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def _delete(Growth: Growth) -> None:
        raise NotImplementedError("Derived classes must implement delete")

    @abstractmethod
    def _get_all(self) -> list[Growth]:
        raise NotImplementedError("Derived classes must implement get_all")

    @abstractmethod
    def _get_by_id(self, value: int) -> Growth:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_name(self, value: str) -> Growth:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_Lname(self, value: str) -> Growth:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _update(self, Growth: Growth) -> None:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def _update(self, Growt: list[Growth]) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemyGrowthRepository(AbstractGrowthRepository):
    """
    Uses guidance from the basic SQLAlchemy 1.4 tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self,Growth: Growth) -> None:
        self.session.add(Growth)
        # self.session.commit()

    def _add_all(self, Growth: list[Growth]) -> None:
        self.session.add_all(Growth)
        # self.session.commit()

    def _delete(self, Growth: Growth) -> None:
        pass

    def _get_all(self) -> list[Growth]:
        return self.session.query(Growth).all()

    def _get_by_id(self, value: int) -> Growth:
        answer = self.session.query(Growth).filter(Growth.id == value)
        return answer.one()

    def _get_by_name(self, value: str) -> Growth:
        answer = self.session.query(Growth).filter(Growth.title == value)
        return answer.one()

    def _get_by_Lname(self, value: str) -> Growth:
        answer = self.session.query(Growth).filter(Growth.Lname == value)
        return answer.one()

    def _get_by_url(self, value: str) -> Growth:
        answer = self.session.query(Growth).filter(Growth.url == value)
        return answer.one()

    def _get_by_head(self, value: float) -> Growth:
        answer = self.session.query(Growth).filter(Growth.head == value)
        return answer.one()

    def _get_by_weight(self, value: Float) -> Growth:
        answer = self.session.query(Growth).filter(Growth.weight == value)
        return answer.one()

    def _get_by_hight(self, value: float) -> Growth:
        answer = self.session.query(Growth).filter(Growth.hight == value)
        return answer.one()

    def _get_by_age(self, value: int) -> Growth:
        answer = self.session.query(Growth).filter(Growth.age == value)
        return answer.one()

    def _get_by_gender(self, value: str) -> Growth:
        answer = self.session.query(Growth).filter(Growth.gender == value)
        return answer.one()

    def _update(self, Growth) -> None:
        pass

    def _update(self, Growth: list[Growth]) -> None:
        pass


class FakeGrowthRepository(AbstractGrowthRepository):
    """
    Uses a Python list to store "fake" growth: https://www.w3schools.com/python/python_lists.asp
    """

    def __init__(self, Growth):
        super().__init__()
        self._Growth = set(Growth)

    def _add(self, growth) -> None:
        self._Growth.add(growth)

    def _add_all(self, Growth: list[Growth]) -> None:
        self._Growth.update(Growth)

    def _delete(self, Growth: Growth) -> None:
        self._Growth.remove(Growth)

    def _get_all(self) -> list[Growth]:
        return self._Growth

    # python next function: https://www.w3schools.com/python/ref_func_next.asp
    def _get_by_id(self, value: int) -> Growth:
        return next((b for b in self._Growth if b.id == value), None)

    def _get_by_name(self, value: str) -> Growth:
        return next((b for b in self._Growth if b.name == value), None)

    def _get_by_Lname(self, value: str) -> list[Growth]:
        return next((b for b in self._Growth if b.Lname == value), None)

    def _get_by_head(self, value: float) -> list[Growth]:
        return next((b for b in self._Growth if b.head == value), None)

    def _get_by_weight(self, value: float) -> list[Growth]:
        return next((b for b in self._Growth if b.weight == value), None)

    def _get_by_hight(self, value: float) -> list[Growth]:
        return next((b for b in self._Growth if b.hight == value), None)

    def _get_by_age(self, value: int) -> list[Growth]:
        return next((b for b in self._Growth if b.age == value), None)

    def _get_by_gender(self, value: str) -> list[Growth]:
        return next((b for b in self._Growth if b.gender == value), None)


    def _update(self, Growth: Growth) -> None:
        try:
            idx = self._Growth.index(Growth)
            bm = self._Growth[idx]
            with Growth:
                bm.id = Growth.id
                bm.Name = Growth.Name
                bm.Lname = Growth.Lname
                bm.url = Growth.url
                bm.head = Growth.head
                bm.weight = Growth.weight
                bm.hight = Growth.hight
                bm.age = Growth.age
                bm.gender = Growth.gender
                bm.notes = Growth.notes
                bm.date_added = Growth.date_added
                bm.date_edited = datetime.utc.now()
                self._Growth[idx] = bm
        except:
            self._Growth.append(Growth)

        return None

    def _update(self, Growth: list[Growth]) -> None:
        for inbm in Growth:
            self._update(inbm)
