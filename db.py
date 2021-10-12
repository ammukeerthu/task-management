from psycopg2 import connect
from psycopg2 import OperationalError

class Database(object):

    def __init__(self, hostname='localhost', port=5432, username='postgres', password='rootroot', db_name='mydb'):

        conn_string = "dbname='" + db_name + "' user='" + username + "' host='" + hostname + "' password='" + password + "'"
        self.conn = connect(conn_string)

        self.cur = self.conn.cursor()

        self.table_name = 'mytable'

    def get(self):

        query = "select * from " + self.table_name

        self.cur.execute(query)

        resp = self.cur.fetchall()

        data = []
        for r in resp:
            data.append({
                'id': r[0],
                'title': r[1].rstrip(),
                'description': r[2].rstrip()
            })

        return data

    def create(self, title, descr):

        query = "insert into " + self.table_name + " (title, descr) values ('" + title + "', '" + descr + "')"

        self.cur.execute(query)

        self.conn.commit()

    def delete(self, idx):

        query = "delete from " + self.table_name + " where id=" + idx + ")"

        self.cur.execute(query)

        self.conn.commit()

