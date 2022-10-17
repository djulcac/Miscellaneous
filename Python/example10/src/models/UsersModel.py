from datetime import datetime, timezone

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import select
import sqlalchemy

from .. import Base

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    lastname = Column(String(100))
    email = Column(String(50),nullable=False,unique=True)
    phone = Column(String(50))
    createdAt = Column(DateTime(timezone=True),default=datetime.now)
    updatedAt = Column(DateTime(timezone=True),default=datetime.now)
    deleted = Column(Boolean,default=False)
    # number = Column(Integer,default=23)
    def __repr__(self):
        return f"Users(id={self.id!r}, name={self.name!r}, lastname={self.email!r})"

    
    def insert(self,session,data):
        '''
        data: json
            campos del modelo
        '''
        _data = {}
        columns = [
            'name',
            'lastname',
            'email',
            'phone',
            # 'createdAt',
            # 'updatedAt',
            # 'deleted',
        ]
        for key in columns:
            if key in data:
                _data[key] = data[key]
        if not 'createdAt' in _data:
            _data['createdAt'] = datetime.now(timezone.utc)
        if not 'updatedAt' in _data:
            _data['updatedAt'] = datetime.now(timezone.utc)
        if not 'deleted' in _data:
            _data['deleted'] = False

        # Validar si hay repetidos
        q = select(Users).where(Users.email==_data['email']).limit(1)
        r = session.scalar(q)
        if not r == None:
            return {'error':True,'type':'unique','column':'email'}
        # Insertar
        r = Users(**_data)
        session.add(r)
        session.flush() # obtener el id
        _id = r.id
        session.commit()
        return {'error':False,'id':_id}

    def get_all(self,session,offset=0,limit=20):
        c = session.query(Users).filter(Users.deleted==False).count()
        q = select(Users).filter(Users.deleted==False).offset(offset).limit(limit)
        r = session.scalars(q)
        return c,r

    def get_one(self,session,ID):
        q = select(Users).filter(Users.deleted==False,Users.id == ID)
        r = session.scalar(q)
        return r
    
    def delete(self,session,ID):
        # https://docs.sqlalchemy.org/en/14/core/dml.html#sqlalchemy.sql.expression.update
        q = sqlalchemy.update(Users).where(Users.id == ID).values(deleted=True)
        session.execute(q)
        session.commit()
        return True
    
    def update(self,session,ID,data):
        '''
        data: json
            campos del modelo
        '''
        _data = {}
        columns = [
            'name',
            'lastname',
            'email',
            'phone',
        ]
        for key in columns:
            if key in data:
                _data[key] = data[key]
        _data['updatedAt'] = datetime.now(timezone.utc)

        # Validar si hay repetidos
        r = None
        if 'email' in _data:
            q = select(Users).where(Users.email==_data['email']).limit(1)
            r = session.scalar(q)
        if not r == None and r.id != ID:
            return {'error':True,'type':'unique','column':'email'}
        # Insertar
        q = sqlalchemy.update(Users).where(Users.id == ID).values(**_data)
        session.execute(q)
        session.commit()
        return {'error':False,'id':ID}
