#print ("Hello World")
#hi =  len("Hello")
#print (hi) ;

#defining a function using def keyword
def my_function():
        print("Hello")
        print("Bye")

#type the name of the function to call it
my_function()


#Hurdle 4 SOLUTION
def turn_right():
    turn_left() 
    turn_left() 
    turn_left() 


def jump():
           #move()
           turn_left()
           move()
           turn_right()
          
         


while not at_goal() :
    if wall_in_front():
        jump()
    else:
        move()
        
    
