# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:16:08 2020

@author: Bence
"""
import sqlite3

conn=sqlite3.connect('db.sqlite3')

c=conn.cursor()
locs=[('Edinburgh castle','historic',32,10),
      ('Pollock Halls','uni-life',44,1),
      ('Princes Street','shopping area',30,15)]
c.executemany('INSERT INTO locations VALUES (?,?,?,?)',locs)
'''c.execute( CREATE TABLE locations (name text, type text, lat real, lon real) )'''
for row in c.execute('SELECT * FROM locations '):
    print(row[0])

conn.commit()

conn.close()
