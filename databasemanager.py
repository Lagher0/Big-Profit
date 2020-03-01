# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:16:08 2020

@author: Bence
"""
import sqlite3
import json
import re 
import random
places = json.load(open('locations-all.json'))
conn=sqlite3.connect('db.sqlite3')
c=conn.cursor()
places_dic = places[0]
print(places_dic)
columns = list(places_dic.keys())
columns.remove("rate")
columns.remove("osm")
columns.remove("wikidata")
#print(places_dic['point'])
#print(places_dic['point']['lon'])
#print(places_dic.keys())
#print(places_dic.items())
c.execute( '''CREATE TABLE IF NOT EXISTS locations (location_id text NOT NULL PRIMARY KEY, name text NOT NULL, posx real, posy real) ''')
c.execute( '''CREATE TABLE IF NOT EXISTS categories (categorie_id text NOT NULL PRIMARY KEY, category text NOT NULL) ''')
c.execute( '''CREATE TABLE IF NOT EXISTS link (link_id text NOT NULL PRIMARY KEY,location_id REFERENCES MODULES(location_id),catgories_id REFERENCES MODULES(categorie_id)) ''')

#places_dic['xid'],places_dic['name'],float(places_dic['point']['lon']),float(places_dic['point']['lat'])
for i in range(0,len(places)):
    places_dic = places[i]
    values = [places_dic['xid'],places_dic['name'],places_dic['point']['lon'],places_dic['point']['lat']]
    values2 = [i]
    for item in re.split(',', places_dic['kinds']):
        j = 0
        if i == 0 and j == 0:
            c.execute('''INSERT INTO  categories VALUES (?,?) ''', [str(i)+str(random.randint(1000,10200401201)),item])
            print("Sucess")
        else:     
            for value in c.execute('''SELECT category FROM categories'''):
                value = re.sub('[^a-zA-Z0-9_]','',value)
                print(value)
                if value != item:
                    print("I'm here!")
                    c.execute('''INSERT INTO  categories VALUES (?,?) ''', [str(i)+str(random.randint(1000,10200401201)),item])
                else:
                    pass
    #c.execute(''' INSERT INTO locations  VALUES (?,?,?,?) ''', values)
    
#

#for row in c.execute('SELECT * FROM locations '):
 #   print(row)

for row in c.execute('SELECT * FROM categories'):
    print(row)

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='locations' ''')
if c.fetchone()[0]==1: 
	print("Exists 1")


c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='categories' ''')
if c.fetchone()[0]==1: 
	print("Exists 2")

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='link' ''')

if c.fetchone()[0]==1: 
	print("Exists 3")

"""

locs=[('Edinburgh castle','historic',32,10),
      ('Pollock Halls','uni-life',44,1),
      ('Princes Street','shopping area',30,15)]
<<<<<<< HEAD
<<<<<<< HEAD
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

=======
'''c.executemany('INSERT INTO locations VALUES (?,?,?,?)',locs)'''
=======
c.executemany('INSERT INTO locations VALUES (?,?,?,?)',locs)
>>>>>>> e0ce9bfe733cad04cd8a804b69b4b6c68e7ec6d6
'''c.execute( CREATE TABLE locations (name text, type text, lat real, lon real) )'''
>>>>>>> 11cdba47d40ee5774fe219471be64ee5302ebbce
for row in c.execute('SELECT * FROM locations '):
    print(row[0])
"""
conn.commit()

conn.close()
