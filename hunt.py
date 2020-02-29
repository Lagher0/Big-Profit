# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:59:47 2020

@author: Bence
"""
import time
import sqlite3
import math
import random
def dist2d(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))
class hunt():
    def __init__(self,duration,pref_categories,radius,init_loc,user):
        self.start_time=time.clock()
        self.duration=duration
        self.radius=radius
        self.filter(pref_categories,init_loc)  
        self.score=0
        self.user=user
        self.last_loc=init_loc
        
    def checktimeLimit(self): #checks if the game is over based on time limit
        if self.duration<time.clock()-self.start_time:
            return True
        return False
    
    def filter(self,prefs,init_loc): # filters the list based on type preferences and radius
        conn=sqlite3.connect('db.sqlite3')
        c=conn.cursor()
        category_filter=[]
        self.locations=[]
        for preference in prefs:  #select each prerence match with a query and then concat lists
             location=c.execute("SELECT * FROM locations WHERE type='%s'" % preference).fetchall()
             self.locations+=location
        for location in category_filter: #then remove locations that are too far away
            distance=dist2d(init_loc,(location[2],location[3]))
            if(distance>self.radius):
                self.locations.remove(location)
        random.shuffle(self.locations) #to shuffle locations randomly
        
    def verify(self,current_loc): # checks if user is close enough to the location,if yes, location is removed from and points are awarded
        distance=dist2d(current_loc,(self.locations[0][2],self.locations[0][3]))
        if distance<0.00060 : #distance might need to change here
            dist_for_points=dist2d(self.last_loc,current_loc)
            self.score+=dist_for_points* 100 #might need to change variable later
            self.score=int(round(self.score,0)) 
            self.last_loc=current_loc
            del self.locations[0]
            return True
        return False
        
            

             
       
        
        
    
        
        
            
def main():
    firstHunt=hunt(5,['uni-life','historic'],60,(23,10),"user")
    print(firstHunt.locations)
    firstHunt.verify((44,1))
    firstHunt.verify((43,1))
    print(firstHunt.locations)
    print(firstHunt.score)
    
    
        
        
     
if __name__== "__main__":
  main()
        
        
