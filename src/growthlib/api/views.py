from growthlib.services import unit_of_work


def Growth_view(name: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT name, FROM Growth WHERE name = :name
            """,
            dict(name=name),
        )
    return [dict(r) for r in results]