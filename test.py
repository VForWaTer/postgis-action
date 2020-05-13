from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

with engine.connect() as connection:
    connection.execute('Create database metacatalog;')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/metacatalog')

with engine.connect() as connection:
    connection.execute('create extension postgis;')
    res = connection.execute('select from PostGIS_full_version();')
    print(res)
