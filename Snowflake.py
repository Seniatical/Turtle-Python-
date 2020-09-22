import turtle

def snowflake(t, lengthSide, levels): 
    if levels == 0: 
        t.forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(t, lengthSide, levels-1) 
    t.left(60) 
    snowflake(t, lengthSide, levels-1) 
    t.right(120) 
    snowflake(t, lengthSide, levels-1) 
    t.left(60) 
    snowflake(t, lengthSide, levels-1) 


anms = turtle.Turtle()
#anms.shape("turtle")
anms.color("#1f3143", "#1f3143")
  
anms.speed(100000000)                    
length = 500.0
  
anms.penup()
anms.fd(-150)
anms.pendown()

#anms.begin_fill()

for i in range(3):     
    snowflake(anms, length, 4) 
    anms.right(120) 

#anms.end_fill()

turtle.mainloop()   
