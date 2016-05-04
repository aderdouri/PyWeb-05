from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    func,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text, nullable=True)
    created = Column(DateTime, default=func.now())
    edited = Column(DateTime, default=func.now())

    @classmethod
    def all(cls, session):
        return session.query(cls).order_by(cls.id.desc()).all()

    @classmethod
    def by_id(cls, session, myid):
        return session.query(cls).filter(cls.id==myid).first()

Index('Entry_index', Entry.title, unique=True, mysql_length=255)
