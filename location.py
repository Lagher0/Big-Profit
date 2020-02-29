# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:34:17 2020

@author: Bence
"""
import sqlite3

class location():   
   def  __init__(self,name,position,loc_type):
        self.name=name
        self.loc_type=loc_type
        self.position=position
