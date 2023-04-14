import sys
import math
import string

#get the first number (the number of lines to read)
cases = int(sys.stdin.readline().rstrip())
 

#use the variable on line 6 to read that many lines
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    data = line.split(",") #split into list, divide by commas
    print(data[0]+"=", end = "") #print person's name followed by equals sign
    
    #reset numbers for each worker
    hours = 0
    minutes = 0
    
    for i in range(1, 6): #walk through next five slots of list
        time = data[i].split(":") #split up remaining cells into new list by the colon
        hours+=int(time[0]) #add first slot to hours
        minutes+=int(time[1]) #add second to minutes
        
    #print(hours, minutes) #uncomment for testing
        
    #this section converts minutes to hours when you have more than 60
    while minutes >=60:
        minutes-=60
        hours+=1
        
    #print out the appropriate hours statement
    if hours ==1:
        print("1 hour", end = "")
    elif hours >1:
        print(hours, "hours", end = "")
    else:
        print("0 hours", end = "")
    
    if minutes ==1:
        print(" 1 minute")
    elif minutes >1:
        print(" ", end = "")
        print(minutes, "minutes")
        

    
