# -*- coding: utf-8 -*-
#imported stuff
import turtle,random,types,unicodedata,os,math,time
import "./Modes/easy.py"
import "./gui.py"
#turtle settings
turtle.speed(0)
turtle.hideturtle()
#lists
square=[15,15,30,30,30,15]
alphabet=list("abcdefghij")
ships=[5,4,3,3,2]
ship_names=["Aircraft Carrier","Battleship","Submarine","Cruiser","Destroyer"]
player1_ship=[[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
player2_ship=[[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
player1_hit=[[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
player2_hit=[[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
player1_hit_xy=[]
player2_hit_xy=[]
player1_shoot_xy=[]
player2_shoot_xy=[]
player1_ship_xy=[]
player2_ship_xy=[]
player1_red_xy=[]
player2_red_xy=[]
#definitions
def red_sq(self):
    self.color("#ff0000")
    self.pendown()
    self.setheading(90)
    self.begin_fill()
    for t in square:
        self.forward(t)
        self.left(90)
    self.end_fill()
turtle.red_sq=types.MethodType(red_sq, turtle)
turtle.red_sq
def cross(self):
    self.color("#000000")
    self.pendown()
    self.setheading(45)
    for i in range(4):
        self.forward(20)
        self.backward(20)
        self.left(90)
turtle.cross=types.MethodType(cross, turtle)
turtle.cross
def grid(self):
    self.color("#000000")
    for i in range(10):
        self.penup()
        self.goto((i*40)-200,200)
        self.pendown()
        self.write(str(i+1),font=("Arial",24))
    for i in range(10):
        self.penup()
        self.goto(-240,(i*40)-200)
        self.pendown()
        self.write(alphabet[9-i],font=("Arial",24))
    for i in range(11):
        self.penup()
        self.goto(-200,(i*40)-200)
        self.pendown()
        self.goto(200,(i*40)-200)
    for i in range(11):
        self.penup()
        self.goto((i*40)-200,200)
        self.pendown()
        self.goto((i*40)-200,-200)
turtle.grid = types.MethodType(grid, turtle)
turtle.grid
def mark(list,object):
    turtle.penup()
    co_x=(list[1]*(40))-180
    co_y=((list[0]*(-40))+180)
    turtle.goto(co_x,co_y)
    if object==0:
        turtle.red_sq()
    else:
        turtle.cross()
def ship_pos(var):
    i=0
    if var==1:
        list=player1_hit_xy
    elif var==2:
        list=player2_hit_xy
    elif var==3:
        list=player1_red_xy
    elif var==4:
        list=player2_red_xy
    elif var==5:
        list=player1_shoot_xy
    else:
        list=player2_shoot_xy
    if var>4:
        object=1
    else:
        object=0
    while i<len(list):
        sublist=list[i]
        mark(sublist,object)
        i+=1
def only_num(s):
    a = unicodedata.category(str(s))
    if a in ("Nd"):
        return True
    else:
        return False
#narative
print ("""
.______        ___   .___________.___________. __       _______ 
|   _  \      /   \  |           |           ||  |     |   ____|   
|  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__      
|   _  <    /  /_\  \    |  |        |  |     |  |     |   __|     
|  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____.    
|______/  /__/     \__\  |__|        |__|     |_______||_______|
     _______. __    __   __  .______   
    /       ||  |  |  | |  | |   _  \  
   |   (----`|  |__|  | |  | |  |_)  | 
    \   \    |   __   | |  | |   ___/  
.----)   |   |  |  |  | |  | |  |      
|_______/    |__|  |__| |__| | _|     """)
print ("...")
print ("Copyright © 2017 by Aragorn, Yicheng. All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, write to the publisher, addressed “Attention: Permissions Coordinator,” at the address below.")
print ("...")
#ask whether you want to play in single or multi
boolean=True
while boolean:
    setting=(str(input("What mode would you like to play in? (Single or Multi): "))).lower().strip()
    setting=setting[0]
    if setting=="s" or setting=="m":
        boolean=False
        break
    else:
        print ("...")
        print ("Type Single or Multi to play")
        print ("...")
#for single player
if setting=="s":
    print ("...")
    #select difficulty
    boolean=True
    while boolean:
        difficulty=input("Select difficulty: Easy, Normal, Hard, IMPOSSIBRU (Typing only the first letter for the difficulty is enough.)").lower().strip()
        difficulty=difficulty[0]
        if difficulty=="e" or difficulty=="n" or difficulty=="h" or difficulty=="i":
            print ("Difficulty selected:")
            if difficulty=="e":
                print ("""
                    __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
   oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
   oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
    *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
    *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
        *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
          *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*     
             *OOOOOOOOo           oOOOOOOOO*    
                 *OOOOOOOOOOOOOOOOOOOOO*
                      \"\"ooooooooo\"\"
 _____                
|  ___|               
| |__  __ _ ___ _   _ 
|  __|/ _` / __| | | |
| |__| (_| \__ \ |_| |
\____/\__,_|___/\__, |
                 __/ |
                |___/""")
            elif difficulty=="n":
                print ("""
________________________8888888888888888888________
____________________888___________________8888_____
________________888_________________________8888___
______________88______________________________888__
___________888_________________________________888_
_________88_____________________________________888
________88_________88888___________88888_________88
______88__________888888__________888888_________88
_____88___________8888____________8888___________88
____88___________________________________________88
___88___________________________________________88_
__88____________________8888____________________88_
_88_______________888888888888888______________88__
_88____________8888___________88888___________88___
888_________888__________________88__________88____
88_________8______________________88________88_____
888______8________________________88_______88______
888_____8_________________________88_____88________
_888___________________________________88__________
__888________________________________88____________
___888____________________________88_______________
____8888______________________888__________________
_______88888_____________88888_____________________
____________8888888888888__________________________
 _   _                            _ 
| \ | |                          | |
|  \| | ___  _ __ _ __ ___   __ _| |
| . ` |/ _ \| '__| '_ ` _ \ / _` | |
| |\  | (_) | |  | | | | | | (_| | |
\_| \_/\___/|_|  |_| |_| |_|\__,_|_|""")
            elif difficulty=="h":
                print ("""
____________________88888888888 
_______________88888888888888888888 
____________88888888111111111188888888 
__________8888811111111111111111111888888 
________88888111111111111111111111111188888 
_______8888111111111111111111111111111118888 
_____8888111188811111111111111111118881118888 
____888811111888111111111111111111188811111888 
___88811111118881111111111111111111888111111888 
__8888111188888811111111111111111118888881111888 
__88811188888888111111111111111111188888888111888 
_8881118888___88811111111111111111888___888811888 
_88811888____8888811111111111111118888____8881188 
_8811888_____8888881111111111111188888_____8811888 
88811888_____8888888811111111111888888_____8881888 
88811888_____8888888888888888888888888_____8811188 
888111888____8888888888888888888888888____88811188 
8881118888___8888888888111118888888888___888111888 
88811118888___88888888111111888888888___8888111888 
_8811111188888888888811111111188888888888811111888 
_888111111188888888111111111111188888888111111188 
_888111111111111111111111111111111111111111111888 
__8881111111111111111888888888111111111111111888 
___888111111111111118888888888811111111111111888 
____8881111111111188881111111888811111111111888 
____888811111111118881111111118881111111118888 
______888811111111111111111111111111111118888 
_______888811111111111111111111111111118888 
_________888881111111111111111111111188888 
___________88888811111111111111111888888 
_____________888888888811118888888888 
_________________8888888888888888

 _   _               _ 
| | | |             | |
| |_| | __ _ _ __ __| |
|  _  |/ _` | '__/ _` |
| | | | (_| | | | (_| |
\_| |_/\__,_|_|  \__,_|""")
            else:
                print ("""
───────▄██████████████████▄───────
────▄███████████████████████▄─────
───███████████████████████████────
──█████████████████████████████───
─████████████▀─────────▀████████──
██████████▀───────────────▀██████─
███████▀────────────────────█████▌
██████───▄▀▀▀▀▄──────▄▀▀▀▀▄──█████
█████▀──────────────────▄▄▄───████
████────▄█████▄───────▄█▀▀▀█▄──██▀
████──▄█▀────▀██─────█▀────────█▀─
─▀██───────────▀────────▄███▄──██─
──██───▄▄██▀█▄──▀▄▄▄▀─▄██▄▀────███
▄███────▀▀▀▀▀──────────────▄▄──██▐
█▄▀█──▀▀▀▄▄▄▀▀───────▀▀▄▄▄▀────█▌▐
█▐─█────────────▄───▄──────────█▌▐
█▐─▀───────▐──▄▀─────▀▄──▌─────██▐
█─▀────────▌──▀▄─────▄▀──▐─────██▀
▀█─█──────▐─────▀▀▄▀▀─────▌────█──
─▀█▀───────▄────────────▄──────█──
───█─────▄▀──▄█████████▄─▀▄───▄█──
───█────█──▄██▀░░░░░░░▀██▄─█──█───
───█▄───▀▄──▀██▄█████▄██▀─▄▀─▄█───
────█▄────▀───▀▀▀▀──▀▀▀──▀──▄█────
─────█▄────────▄▀▀▀▀▀▄─────▄█─────
──────███▄──────────────▄▄██──────
─────▄█─▀█████▄▄────▄▄████▀█▄─────
────▄█───────▀▀██████▀▀─────█▄────
───▄█─────▄▀───────────▀▄────█▄───
──▄█─────▀───────────────▀────█▄──
──────────────────────────────────
▐▌▐█▄█▌▐▀▀█▐▀▀▌─█▀─█▀─▐▌▐▀█▐▀█─█─█
▐▌▐─▀─▌▐▀▀▀▐──▌─▀█─▀█─▐▌▐▀▄▐▀▄─█─█
▐▌▐───▌▐───▐▄▄▌─▄█─▄█─▐▌▐▄█▐─█─█▄█""")
            boolean=False
        else:
            print ("...")
            print ("type e for easy mode, n for normal made, h for hard mode or i for IMPOSSIBREW mode")
            print ("...")
    #computer putting ships
    for i in ships:
        boolean=True
        while boolean:
            counter=0
            h_v=random.randrange(0,2)
            if h_v==0:
                h=random.randrange(0,10-i)
                v=random.randrange(0,10)
            else:
                h=random.randrange(0,10)
                v=random.randrange(0,10-i)
            if h_v==0:
                for disp in range(i):
                    sublist=player1_ship[h+disp]
                    if sublist[v]==False:
                        counter+=1
                    else:
                        break
            else:
                for disp in range(i):
                    sublist=player1_ship[h]
                    if sublist[v+disp]==False:
                        counter+=1
                    else:
                        break
            if counter==i:
                boolean=False
                ship=[]
                if h_v==0:
                    for disp in range(i):
                        sublist=player1_ship[h]
                        sublist[v]=True
                        ship.append([h,v])
                        player1_red_xy.append([h,v])
                        h+=1
                else:
                    for disp in range(i):
                        sublist=player1_ship[h]
                        sublist[v]=True
                        ship.append([h,v])
                        player1_red_xy.append([h,v])
                        v+=1
                player1_ship_xy.append(ship)
    print ("...")
    #player putting ships
    turtle.grid()
    for i in range(5):
        boolean=True
        while boolean:
            counter=0 
            h_v=input("Do you want to place your %s (%s x 1 ship) horizontally or vertically? (H or V): "%(ship_names[i],ships[i])).lower().strip()
            if h_v=="h" or h_v=="v":
                boolean=False
            else:
                print ("...")
                print ("Type H for a horizontal boat and V for a vertical boat")
                print ("...")
        print ("...")
        if h_v=="h":
            boolean=True
            while boolean:
                XY=list(input("Type the top left hand coordinate of the ship. (e.g. A1)").lower().strip())
                if len(XY)==2 and only_num(XY[1]):
                    XY[1]=int(XY[1])-1
                    if XY[0] in alphabet and float(XY[1]).is_integer() and XY[1]<11-ships[i]:
                        XY[0]=alphabet.index(XY[0])
                        for disp in range(ships[i]):
                            sublist=player2_ship[XY[0]]
                            if sublist[XY[1]+disp]==False:
                                counter+=1
                else:
                    print ("...")
                    print ("Try again.")
                    print ("...")
                if counter==ships[i]:
                    boolean=False
        else:
            boolean=True
            while boolean:
                XY=list(input("Type the top left hand coordinate of the ship. (e.g. A1)").lower().strip())
                if len(XY)==2 and only_num(XY[1]):
                    XY[1]=int(XY[1])-1
                    if XY[0] in alphabet and alphabet.index(XY[0])<11-ships[i]:
                        XY[0]=alphabet.index(XY[0])
                        for disp in range(ships[i]):
                            sublist=player2_ship[XY[0]+disp]
                            if sublist[XY[1]]==False:
                                counter+=1
                elif len(XY)==3 and XY[1]=="1" and XY[2]=="0":
                    XY[1]=9
                    XY.remove("0")
                    if XY[0] in alphabet and alphabet.index(XY[0])<11-ships[i]:
                        XY[0]=alphabet.index(XY[0])
                        for disp in range(ships[i]):
                            sublist=player2_ship[XY[0]+disp]
                            if sublist[XY[1]]==False:
                                counter+=1
                else:
                    print ("...")
                    print ("Try again.")
                    print ("...")
                if counter==ships[i]:
                    boolean=False
        print ("...")
        if counter==ships[i]:
            boolean=False
            ship=[]
            if h_v=="h":
                for disp in range(ships[i]):
                    sublist=player2_ship[XY[0]]
                    sublist[XY[1]+disp]=True
                    mark([XY[0],XY[1]+disp],0)
                    ship.append([XY[0],XY[1]+disp])
                    player2_red_xy.append([XY[0],XY[1]+disp])
            else:
                for disp in range(ships[i]):
                    sublist=player2_ship[XY[0]+disp]
                    sublist[XY[1]]=True
                    mark([XY[0]+disp,XY[1]],0)
                    ship.append([XY[0]+disp,XY[1]])
                    player2_red_xy.append([XY[0]+disp,XY[1]])
            player2_ship_xy.append(ship)
    #0 is player, 1 is computer
    turn=0
    destroyed=0
    imposibru_counter=0
    #delete coordinate when a hit is made
    while not(player1_ship_xy==[] or player2_ship_xy==[]):
        if turn==0:
            turtle.clear()
            turtle.grid()
            ship_pos(4)
            ship_pos(6)
            time.sleep(5)
            turtle.clear()
            turtle.grid()
            ship_pos(1)
            ship_pos(5)
            boolean=True
            while boolean:
                XY=list(input("Where do you want to hit? (e.g. A1)").lower().strip())
                if len(XY)==2 and only_num(XY[1]):
                    XY[1]=int(XY[1])-1
                    if XY[0] in alphabet:
                        XY[0]=alphabet.index(XY[0])
                        sublist=player1_hit[XY[0]]
                        if sublist[XY[1]]==False:
                            boolean=False
                            sublist[XY[1]]=True
                elif len(XY)==3 and XY[1]=="1" and XY[2]=="0":
                    XY[1]=9
                    XY.remove("0")
                    if XY[0] in alphabet:
                        XY[0]=alphabet.index(XY[0])
                        sublist=player1_hit[XY[0]]
                        if sublist[XY[1]]==False:
                            boolean=False
                            sublist[XY[1]]=True
                else:
                    print ("...")
                    print ("Try again.")
                    print ("...")
            mark(XY,1)
            player1_shoot_xy.append(XY)
            if XY in player1_red_xy:
                print ("hit")
                mark(XY,0)
                player1_hit_xy.append(XY)
                for i in range(len(player1_ship_xy)):
                    sublist=player1_ship_xy[i]
                    if XY in sublist:
                        sublist.remove(XY)
                        if sublist==[]:
                            destroyed=player1_ship_xy.index([])
                            print ("ship sunk")
                if player1_ship_xy[destroyed]==[]:
                    player1_ship_xy.remove([])
            else:
                print ("miss")
            print ("...")
        else:
            if difficulty=="e":
                easy()
            elif difficulty=="n":
                print ("n")
            elif difficulty=="h":
                print ("h")
            else:
                sublist=player2_red_xy[imposibru_counter]
                h=sublist[0]
                v=sublist[1]
                imposibru_counter+=1
            player2_shoot_xy.append([h,v])
            if [h,v] in player2_hit_xy:
                player2_hit_xy.append([h,v])
                for i in range(len(player2_ship_xy)):
                    sublist=player2_ship_xy[i]
                    if [h,v] in sublist:
                        sublist.remove([h,v])
                        if sublist==[]:
                            destroyed=player1_ship_xy.index([])
            if player1_ship_xy[destroyed]==[]:
                player1_ship_xy.remove([])
        turn=(turn+1)%2
#for multiplayer
else:
    print ("Multiplayer is currently unavilable")
    print ("""

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ \"$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
\"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  \"\"\"$$$
   \"$$$\"\"\"\"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     \"$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     \"$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$\"\"\"\"\"\"\"\"
 \"\"\"\"       $$$$    \"$$$$$$$$$$$$$$$$$$$$$$$$$$$$\"      o$$$
            \"$$$o     \"\"\"$$$$$$$$$$$$$$$$$$\"$$\"         $$$
              $$$o          \"$$\"\"$$$$$$\"\"\"\"           o$$$
               $$$$o                                o$$$\"
                \"$$$$o      o$$$$$$o\"$$$$o        o$$$$
                  \"$$$$$oo     \"\"$$$$o$$$$$o   o$$$$\"\"
                     \""$$$$$oooo  \"$$$o$$$$$$$$$\"\"\"
                        \"\"$$$$$$$oo $$$$$$$$$$
                                \"\"\"\"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$\"
                                      \"$$$\"\"\"\"
______           _            _ _   _       _ _   
|  _  \         | |          (_) | | |     (_) |  
| | | |___  __ _| | __      ___| |_| |__    _| |_ 
| | | / _ \/ _` | | \ \ /\ / / | __| '_ \  | | __|
| |/ /  __/ (_| | |  \ V  V /| | |_| | | | | | |_ 
|___/ \___|\__,_|_|   \_/\_/ |_|\__|_| |_| |_|\__|""")
