from sqlalchemy import create_engine, text
import os

database_url = os.environ.get('DATABASE_URL', 'postgresql://localhost/flask_test')
engine = create_engine(database_url, echo=True, future=True)

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
