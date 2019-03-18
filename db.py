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
