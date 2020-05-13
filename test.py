from sqlalchemy import create_engine
import os

port = os.environ.get('POSTGRES_PORT', '5432')
print('[PORT] %s' % port)

engine = create_engine('postgresql://postgres:postgres@localhost:%s/postgres' % port)

with engine.connect() as connection:
    connection.execute('commit')
    connection.execute('Create database metacatalog;')

engine = create_engine('postgresql://postgres:postgres@localhost:%s/metacatalog' % port)

with engine.connect() as connection:
    connection.execute('create extension postgis;')
    res = connection.execute('select from PostGIS_full_version();')
    print(res)
