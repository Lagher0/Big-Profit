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
        self.end=self.start_time+duration
        self.radius=radius
        self.filter(pref_categories,init_loc)  
        self.score=0
        self.user=user
        self.last_loc=init_loc
        
    def checktimeLimit(self): #checks if the game is over based on time limit
        if self.end<time.clock():
            return True
        return False
    
    def filter(self,prefs,init_loc): # filters the list based on type preferences and radius
        conn=sqlite3.connect('db.sqlite3')
        c=conn.cursor()
        self.locations=[]
        if prefs=="all":
            self.locations=c.execute("SELECT * FROM locations").fetchall()
        else:
            for preference in prefs:  #select each prerence match with a query and then concat lists
             location=c.execute("SELECT * FROM locations WHERE type='%s'" % preference).fetchall()
             self.locations+=location       
        for location in self.locations: #then remove locations that are too far away
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
            #self.detour()
            return True
        return False
    def detour(self):
        x=input()
        if x=='0':
            del self.locations[1]
        else:
            del self.locations[0]
    def estimate_time(self,current_loc,estimate_speed):
        distance=dist2d(current_loc,(self.locations[0][2],self.locations[0][3]))
        time_req=distance/estimate_speed
        if self.end-time.clock()< time_req:
            print("Not enough time to reach destination")
        return time_req
        
            

             
       
        
        
    
        
        
            
def main():
    firstHunt=hunt(10,"all",60,(23,10),"user")
    print(firstHunt.locations)
    current_loc=(0,0)
    while not len(firstHunt.locations)==0 and not firstHunt.checktimeLimit():
       
        while not firstHunt.verify((current_loc)) and not firstHunt.checktimeLimit():
             time.sleep(0.05)
             if current_loc[0]> firstHunt.locations[0][2]:
                 current_loc=(current_loc[0]-1,current_loc[1])
             elif current_loc[0] < firstHunt.locations[0][2]:
                 current_loc= (current_loc[0]+1,current_loc[1])
             if current_loc[1]> firstHunt.locations[0][3]:
                 current_loc=(current_loc[0],current_loc[1]-1)
             elif current_loc[1] < firstHunt.locations[0][3]:
                 current_loc=(current_loc[0],current_loc[1]+1)
                
            
            
    print(len(firstHunt.locations))
    print(firstHunt.score)
    
    
        
        
     
if __name__== "__main__":
  main()
        
        
