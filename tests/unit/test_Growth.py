from datetime import date, datetime, timedelta
import random

from growthlib.domain import events
from growthlib.domain.models import Growth

ok_urls = ["http://", "https://"]




def test_growth_id_is_unique():
    pass


def test_that_age_is_more_than_twenty():

    created: str = datetime.now().isoformat()
    edited: str = created
    Growth = Growth(0, "John","Smith","http://www.example/com",35,28,3,25,"boy", None, created, created)

    assert Growth.age_added > 20


def test_that_age_is_less_than_zero():

    created: str = datetime.now().isoformat()
    edited: str = created
    Growth = Growth(0, "John","Smith","http://www.example/com",35,28,3,-2,"boy", None, created, created)

    assert Growth.age_added < 0

def test_that_gender_is_not_boy_or_girl():

    created: str = datetime.now().isoformat()
    edited: str = created
    Growth = Growth(0, "John","Smith","http://www.example/com",35,28,3,25,"boy", None, created, created)

    assert Growth.gender_added =="unknown"
    

def test_new_growth_added_and_edited_times_are_the_same():
    # arrange
    created: str = datetime.now().isoformat()

    # act
    edited: str = created
    Growth = Growth(0, "John","Smith","http://www.example/com",35,28,3,2,"boy", None, created, created)

    # assert
    assert Growth.date_added == Growth.date_edited


def test_new_growth_url_is_well_formed():
    # arrange
    created: str = datetime.now().isoformat()
    edited: str = created

    # act
    Growth = Growth(0, "John","Smith","http://www.example/com",35,28,3,2,"boy", None, created, created)
    # list comprehensions - https://www.w3schools.com/python/python_lists_comprehension.asp
    okay = [prefix for prefix in ok_urls if Growth.url.startswith(prefix)]
    # any function - https://www.w3schools.com/python/ref_func_any.asp
    assert any(okay)


def test_that_edit_time_is_older_than_created_time():
    # arrange
    created: str = datetime.now().isoformat()
    edited: str = created

    # act
    Growth = Growth(0, "John","Smith","http://www.example/com",35,28,3,2,"boy", None, created, edited)

    Growth.notes = "This is a test"
    hours_addition = random.randrange(1, 8)
    edit_time = datetime.fromisoformat(Growth.date_edited)
    Growth.date_edited = (edit_time + timedelta(hours=hours_addition)).isoformat()

    # assert
    assert Growth.date_added < Growth.date_edited

def test_that_head_is_more_than_60():

    created: str = datetime.now().isoformat()
    edited: str = created
    Growth = Growth(0, "John","Smith","http://www.example/com",59,28,3,25,"boy", None, created, created)

    assert Growth.head_added >60

