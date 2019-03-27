# db.py
import logging

from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename='/home/bot_m.log')
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


async def get_user_session(conn, uid):

    result = await conn.execute(
        user_session.select()
        .where(user_session.c.user_id == uid))
    user_session_record = await result.first()
    if not user_session_record:
        await conn.execute(user_session.insert().values(user_id=uid, intent_name='start'))
    result = await conn.execute(
        user_session.select()
        .where(user_session.c.user_id == uid))
    user_session_record = await result.first()
    return user_session_record


async def add_fact(conn, uid, f_name, f_value):
    result = await conn.execute(
        fact.select()
        .where(fact.c.user_id == uid)
        .where(fact.c.fact_name == f_name))
    fact_record = await result.first()
    logging.info('f_value= ' + f_value)
    logging.info('fact= ' + str(fact_record) )
    if not fact_record:
        if f_value is not None:
            await conn.execute(fact.insert().values(user_id=uid, fact_name=f_name, fact_value=f_value) )





