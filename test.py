from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class MyPerson(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None


def create_people():
    person_1 = MyPerson(name="Deadpond", age=30)
    person_2 = MyPerson(name="Spider-Boy")
    person_3 = MyPerson(name="Rusty-Man", age=48)

    session = Session(engine)

    session.add(person_1)
    session.add(person_2)
    session.add(person_3)

    session.commit()



sqlite_file_name = "database.db"
postgres_url = "postgresql://postgres:example@localhost:5432/"

engine = create_engine(postgres_url, echo=True)

SQLModel.metadata.create_all(engine)
create_people()