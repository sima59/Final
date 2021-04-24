from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

from growthlib.domain import commands, events, models

if TYPE_CHECKING:
    from . import unit_of_work

def add_Growth(
    cmd: commands.AddGrowthCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        # look to see if we already have this  data 
        Growth = uow.Growth.get_by_name(value=cmd.name)
        
    
        
        # checks to see if the list is empty
        if not Growth:
            Growth = models.Growth(
                cmd.id, cmd.name, cmd.Lname,cmd.head, cmd.weight, cmd.hight, cmd.age, cmd.gender ,cmd.notes, cmd.date_added, cmd.date_edited, 
            )
        # checks to see if the age>20

        
        if uow.Growth.get_by_age(value=cmd.age)>20:
             error = 'Age should be less than 20'

        else:
            uow.Growth.add(Growth)
        uow.commit()

# ListGrowthCommand: order_by: str order: str
def list_Growth(
    cmd: commands.ListGrowthCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    Growth = None
    with uow:
        Growth = uow.Growth.get_by_age()
       #Growth = uow.Growth.all()
    return Growth


# DeleteGrowthCommand: id: int
def delete_Growth(
    cmd: commands.DeleteGrowthCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


# EditGrowthCommand(Command):
def edit_Growth(
    cmd: commands.EditGrowthCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


EVENT_HANDLERS = {
    events.GrowthAdded: [add_Growth],
    events.GrowthListed: [list_Growth],
    events.GrowthDeleted: [delete_Growth],
    events.GrowthEdited: [edit_Growth],
}  

COMMAND_HANDLERS = {
    commands.AddGrowthCommand: add_Growth,
    commands.ListGrowthCommand: list_Growth,
    commands.DeleteGrowthCommand: delete_Growth,
    commands.EditGrowthCommand: edit_Growth,
}  # type: Dict[Type[commands.Command], Callable]
