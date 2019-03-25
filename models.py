# db.py
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

user_session = Table(
    'user_session', meta,
    Column('user_id', Integer, unique=True),
    Column('intent_name', String(200), nullable=False),

)

fact = Table(
    'fact', meta,

    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('fact_name', String(300), nullable=False),
    Column('fact_value', String(300), nullable=False),



)


async def add_fact(conn, user_id, fact_name, fact_value):
    result = await conn.execute(
        fact.select()
        .where(fact.c.user_id == user_id).where(fact.c.fact_name == fact_name))
    fact_record = await result.first()
    if not fact_record:
        await conn.execute(fact.insert().values(user_id=user_id, fact_name=fact_name), fact_value=fact_value)
    else:





