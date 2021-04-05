'''This is for rolling dice'''
import random
import copy
i=[[1,6],[3,4],[2,5]]
lst =[]
print('initial values: ',i)
count = 0

def dice(i):
    print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}
                    
                                          """)
dice(i) 
print("\nR-roll right\nL-roll left\nU-roll up\nD-roll down\nQ-quit")
random.shuffle(i)
print(i)
   
def right_roll(right):
   
    right[1][0],right[2][1],right[1][1],right[2][0]=right[2][0],right[1][0],right[2][1],right[1][1]
    dice(right)
    print("right")
    print(right)
    r = copy.deepcopy(right)
    lst.append([r,'right'])     

def left_roll(left):
    
    left[1][0],left[2][0],left[1][1],left[2][1]=left[2][1],left[1][0],left[2][0],left[1][1]
    dice(left)
    print("left")
    print(left)
    r = copy.deepcopy(left)
    lst.append([r,'left'])    

def up_roll(up):
    
    up[0][0],up[1][1],up[1][0],up[0][1]= up[1][0],up[0][0],up[0][1],up[1][1]
    dice(up)
    print("up")
    r = copy.deepcopy(up)
    lst.append([r,'up'])
    print(up)   
    
def down_roll(down):

    down[1][0],down[0][0],down[0][1],down[1][1]=down[0][0],down[1][1],down[1][0],down[0][1]
    dice(down) 
    print("down")
    r = copy.deepcopy(down)
    lst.append([r,'down'])
    print(down)    
    
while True:
    select = ((input('pick your move: ').strip()[0]).upper())
    if select == 'R' :
        count+=1
        right_roll(i)
        
    elif select == 'L':
        count+=1
        left_roll(i)
        
    elif select == 'U':
        count+=1
        up_roll(i)
        
    elif select == 'D':
        count+=1
        down_roll(i)
        
    elif select == 'F':
        count+=1
        front_roll(i)
        
    elif select == 'B':
        count+=1
        back_roll(i)
        
    elif select == 'Q':
        print(count)
        print("**********Hey!!! This is Your Final Dice**********")
        for i,j in lst:
            print(i)
            dice(i)
            print(j)
        print("this is latest position")
        dice(i)
        print("________________________________")
        break
       
    else:
        print("This is Invalid move \nPlease Enter R/L/U/D to Rotate or Q to Quit.")
