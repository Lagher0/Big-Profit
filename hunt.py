# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:59:47 2020

@author: Bence
"""
import time
import sqlite3
import math

class hunt():
    def __init__(self,duration,pref_categories,radius,init_loc,user):
        self.start_time=time.clock()
        self.duration=duration
        self.radius=radius
        self.filter(pref_categories,init_loc)  
        self.score=0
        self.user=user
    def checktimeLimit(self):
        if self.duration<time.clock()-self.start_time:
            '''print ("Game Over")'''
            return True
        '''print("Game still on")'''
        return False
    def filter(self,prefs,init_loc):
        conn=sqlite3.connect('db.sqlite3')
        c=conn.cursor()
        category_filter=[]
        self.locations=[]
        for preference in prefs: 
             location=c.execute("SELECT * FROM locations WHERE type='%s'" % preference).fetchall()
             category_filter+=location
        for location in category_filter:
            distance= math.sqrt(math.pow((init_loc[0]-location[2]),2)+math.pow((init_loc[1]-location[3]),2))
            if(distance<self.radius):
                self.locations+=location
    def verify(self,current_loc):
        distance= math.sqrt(math.pow((current_loc[0]-self.locations[0][3]),2)+math.pow((self.init_loc[1]-location[3]),2))
        
            

             
       
        
        
    
        
        
            
def main():
    firstHunt=hunt(5,['uni-life','historic'],60,(23,10),"user")
    print(firstHunt.locations)
    time.sleep(3)
    firstHunt.checktimeLimit()
    
        
        
     
if __name__== "__main__":
  main()
        
        
