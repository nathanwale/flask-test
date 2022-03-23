from sqlalchemy import create_engine, select, update as sql_update
from sqlalchemy.orm import sessionmaker
from urllib.parse import urlparse, urlunparse
import os
from contextlib import contextmanager

def init_engine():
    db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost/flask_test')
    parsed_url = urlparse(db_url)
    if parsed_url.scheme == 'postgres':
        db_url = urlunparse(('postgresql', *parsed_url[1:]))
    print(f"connecting to databse at {db_url}")
    return create_engine(db_url, echo=True, future=True)

Session = sessionmaker(init_engine(), future=True)


#
# Run a sqlalchemy statement
#
def run(statement):
    with Session() as session:
        result = session.execute(statement).scalars().all()
    return result

#
# Add an object
#
def add(object):
    with Session() as session:
        session.add(object)
        session.commit()

#
# Get by ID
#
def get(orm_class, id):
    with Session() as session:
        result = session.get(orm_class, id)
    return result

#
# Update
#
@contextmanager
def update(orm_class, id):
    with Session() as session:
        item = session.get(orm_class, id)
        try:
            yield item
        finally:    
            session.commit()

