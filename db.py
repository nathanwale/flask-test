from sqlalchemy import create_engine, text
from urllib.parse import urlparse, urlunparse
import os

def init_engine():
    db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost/flask_test')
    parsed_url = urlparse(db_url)
    if parsed_url.scheme == 'postgres':
        db_url = urlunparse(('postgresql', *parsed_url[1:]))
    print(f"connecting to databse at {db_url}")
    return create_engine(db_url, echo=True, future=True)
    
engine = init_engine()

#
# Run a DB query
#
def query(sql, params={}):
    with engine.connect() as conn:
        result = conn.execute(
            text(sql),
            params
        )
        
    return result.all()


#
# Call a db Procedure
#
def procedure(procname, params={}):
    with engine.begin() as connection:
        arity = ", ".join(f":{k}" for k in params.keys())
        sql = f"call {procname}({arity})"
        result = connection.execute(
            text(sql),
            params
        )
        connection.commit()
    return result
