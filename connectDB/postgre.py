import traceback
import psycopg2
from psycopg2.extras import RealDictCursor

def connect(h, d, u, pw, p):
    
    query = "CREATE TABLE ipman_list (ip TEXT PRIMARY KEY, name TEXT, address TEXT);"    
    try:
        conn = psycopg2.connect(host=h, user=u, password=pw, dbname=d, port=p)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        print("PostgreSQL server information")
        print(conn.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cur.execute("SELECT version();")
        # Fetch result
        record = cur.fetchone()
        print("You are connected to - ", record, "\n")
        
        #print(query)
        #cur.execute(query)
        #conn.commit()
        
    except (Exception, psycopg2.Error) as error:
        print('Fail to connect DB >>', error)
        
    finally:
        if (conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")