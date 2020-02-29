# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:16:08 2020

@author: Bence
"""
import sqlite3
conn=sqlite3.connect('db.sqlite3')
c=conn.cursor()

c.execute( '''CREATE TABLE IF NOT EXISTS locations (location_id text NOT NULL PRIMARY KEY, name text NOT NULL, posx real, posy real) ''')
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='locations' ''')
if c.fetchone()[0]==1: 
	print("Exists 1")

c.execute( '''CREATE TABLE IF NOT EXISTS categories (categorie_id text NOT NULL PRIMARY KEY, category text NOT NULL) ''')
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='categories' ''')
if c.fetchone()[0]==1: 
	print("Exists 2")

c.execute( '''CREATE TABLE IF NOT EXISTS link (link_id text NOT NULL PRIMARY KEY,location_id REFERENCES MODULES(location_id),catgories_id REFERENCES MODULES(categorie_id)) ''')
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='link' ''')

if c.fetchone()[0]==1: 
	print("Exists 3")

"""

locs=[('Edinburgh castle','historic',32,10),
      ('Pollock Halls','uni-life',44,1),
      ('Princes Street','shopping area',30,15)]
#Gets the table if it exits
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='locations' ''')
#if the count is 1, then table exists
if c.fetchone()[0]==1: 
	c.executemany('''INSERT INTO locations VALUES '(?,?,?)',locs)''')
else: 
    #Creates table if it doesn't exist
    c.execute( '''CREATE TABLE locations (name text, type text, posx real, posy real) ''')

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='categories' ''')
if c.fetchone()[0]==1:
    c.executemany('''INSERT INTO category VALUES '(?,?)',categories''')
else:
    c.execute( '''CREATE TABLE locations (name text, type text, posx real, posy real) ''')

for row in c.execute('SELECT * FROM locations '):
    print(row[0])
"""
conn.commit()

conn.close()
