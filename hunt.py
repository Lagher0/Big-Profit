# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:59:47 2020

@author: Bence
"""
import time
import sqlite3

class hunt():
    def __init__(self,locations,duration,user):
        self.locations=locations
        self.start_time=time.clock()
        self.duration=duration
        self.score=0
        self.user=user
    def checktimeLimit(self):
        if self.duration<time.clock()-self.start_time:
            self.gameover()
            '''print ("Game Over")'''
            return True
        '''print("Game still on")'''
        return False
    def gameover(self):
        
        
            
def main():
    firstHunt=Hunt([],5)
    print(firstHunt.start_time)
    time.sleep(3)
    firstHunt.checktimeLimit()
    
        
        
     
if __name__== "__main__":
  main()
        
        
