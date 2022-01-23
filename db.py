import psycopg2
import os

def connect_to_db():
    """ 
    Connect to DB
    """
    database_url = os.environ.get('DATABASE_URL', 'postgres://localhost/flask_test')
    conn = psycopg2.connect(database_url, sslmode='allow')
    return conn

def query(sql, params=[]):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows

def procedure(procname, params=[]):
    db = connect_to_db()
    cursor = db.cursor()
    arity = ", ".join(["%s"] * len(params))
    sql = f"call {procname}({arity})"
    cursor.execute(sql, params)
    db.commit()
    cursor.close()
    db.close()