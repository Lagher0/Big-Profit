# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:59:47 2020
0.0001 lat = 11 meters
1 mile =1609.34
1 lat =69 miles
@author: Bence
"""
import time
import sqlite3
import math
import random
def dist2d(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))
def hour_toSeconds(hours):
    return hours*3600
def miles_toLat(miles):
    return miles/69.0
class hunt():
    def __init__(self,duration,pref_categories,radius,init_loc,user):
        self.start_time=time.clock()
        self.end=self.start_time+hour_toSeconds(duration)
        self.radius=miles_toLat(radius)
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
        type_filtered=[]
        if prefs=="all":
            type_filtered=c.execute("SELECT * FROM locations").fetchall()
        else:
            for preference in prefs:  #select each prerence match with a query and then concat lists
             location=c.execute("SELECT * FROM locations WHERE type='%s'" % preference).fetchall()
             type_filtered.append(location)       
        for location in type_filtered: #then remove locations that are too far away
            distance=dist2d(init_loc,(location[2],location[3]))
            if(distance<self.radius):
                self.locations.append(location)
        random.shuffle(self.locations) #to shuffle locations randomly
        
    def verify(self,current_loc): # checks if user is close enough to the location,if yes, location is removed from and points are awarded
        distance=dist2d(current_loc,(self.locations[0][2],self.locations[0][3]))
        if distance<0.0006 : #distance approximately 60 meters to verify arriving to destination
            dist_for_points=dist2d(self.last_loc,current_loc)
            self.score+=dist_for_points* 10000 #might need to change variable later
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
    def ignore(self):
        if len(self.locations)!=0:
            del self.locations[0]
    def display_Time(self):
        remaining_time=self.end-time.clock()
        return int(remaining_time)
        
            

             
       
        
        
    
        
        
            
def main():
    step_size=0.00001
    firstHunt=hunt(1,"all",0.7,(-3.18634,55.953472),"user")
    data_size=len(firstHunt.locations)
    #print(firstHunt.locations)
    print(data_size)
    current_loc=(-3.186034,55.953472)
    while not len(firstHunt.locations)==0 and not firstHunt.checktimeLimit():
        print(firstHunt.locations[0][1])
       
        while not firstHunt.verify((current_loc)) and not firstHunt.checktimeLimit():
             if current_loc[0]> firstHunt.locations[0][2]:
                 current_loc=(current_loc[0]-step_size,current_loc[1])
             elif current_loc[0] < firstHunt.locations[0][2]:
                 current_loc= (current_loc[0]+step_size,current_loc[1])
             if current_loc[1]> firstHunt.locations[0][3]:
                 current_loc=(current_loc[0],current_loc[1]-step_size)
             elif current_loc[1] < firstHunt.locations[0][3]:
                 current_loc=(current_loc[0],current_loc[1]+step_size)
                
            
            
    print(data_size-len(firstHunt.locations))
    print(firstHunt.score)
    
    
        
        
     
if __name__== "__main__":
  main()