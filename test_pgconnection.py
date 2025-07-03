import os
import psycopg

os.environ['PGHOST'] = 'early-regular-bulldog.a1.pgedge.io'
os.environ['PGUSER'] = 'admin'
os.environ['PGDATABASE'] = 'pg'
os.environ['PGSSLMODE'] = 'require'
os.environ['PGPASSWORD'] = '8O08Hpa9K843XZRsTm0M69IJ'

def main():
    connection = psycopg.connect()
    cursor = connection.cursor()
    cursor.execute('SELECT node_name FROM spock.node')
    node_names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    print(node_names)

if __name__ == '__main__':
    main()
