import psycopg2
import psycopg2.extras
hostname = 'localhost'
database ='Telecom_db'
username ='postgres'
pwd = '1234'
port_id = 5432
conn = None
cur = None

try:
    
    with psycopg2.connect(host= hostname, dbname= database, user= username, password="1234", port=port_id) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
             cur.execute('DROP TABLE IF EXISTS employee')
            
             create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id  int PRIMARY KEY,
                            name varchar(40) NOT NULL,
                            salary int,
                            dept_id varchar(30)) '''
             cur.execute(create_script)
             insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES(%s, %s, %s, %s)'
             insert_values = [(1, 'James', 12000, 'D1'),(2, 'Robin', 15000, 'D2'), (3, 'Xavier', 20000, 'D3')]
             for record in insert_values:
                    cur.execute(insert_script, record)
             update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
             cur.execute(update_script) 
                                
                                           
             cur.execute('SELECT * FROM EMPLOYEE')
        
             for record in cur.fetchall():
                        print(record['name'], record['salary'])
except Exception as error:
    print(error)
finally:
  if conn is not None:
            conn.close()
conn.close()
