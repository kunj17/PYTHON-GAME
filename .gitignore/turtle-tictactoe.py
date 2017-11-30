import turtle,time,sys
wind=turtle.Screen()
plr=turtle.Turtle()
played={1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80,9:90}
mv=0
wincon=0
op=[0]
win=False
kg=True

def make_xo(ffcp,fx,fy):
    if ffcp==1:
        
        if p1=='X':
            
            plr.penup();
            plr.goto(fx,fy);
            plr.pendown();
            plr.setheading(0)
            plr.right(45);
            plr.forward(67.8);
            plr.penup();
            plr.goto(fx+48,fy);
            plr.pendown();
            plr.setheading(0)
            plr.right(90+45);
            plr.forward(67.8);
            
        elif p1=='O':
            
            plr.penup();
            plr.goto(fx+36,fy-72);
            plr.pendown();
            plr.setheading(0)
            plr.circle(48);

    if ffcp==2:
        
        if p2=='X':
            
            plr.penup();
            plr.goto(fx,fy);
            plr.pendown();
            plr.setheading(0)
            plr.right(45);
            plr.forward(67.8);
            plr.penup();
            plr.goto(fx+48,fy);
            plr.pendown();
            plr.setheading(0);
            plr.right(90+45);
            plr.forward(67.8);
            
        elif p2=='O':
            
            plr.penup();
            plr.goto(fx+36,fy-72);
            plr.pendown();
            plr.setheading(0)
            plr.circle(48);
    
    played[mv]=ffcp;
    
    if gwin():
        
        return True;
    
    else:
        
        return False;
            
def dtm(fcp,fmv):
    
        if fmv==1:
            
            wn=make_xo(fcp,-96,-24);
            
        elif fmv==2:
            
            wn=make_xo(fcp,-96+120,-24);
            
        elif fmv==3:
            
            wn=make_xo(fcp,-96+120+120,-24);
            
        elif fmv==4:
            
            wn=make_xo(fcp,-96,-120-24);
            
        elif fmv==5:
            
            wn=make_xo(fcp,-96+120,-120-24);
            
        elif fmv==6:
            
            wn=make_xo(fcp,-96+120+120,-120-24);
            
        elif fmv==7:
            
            wn=make_xo(fcp,-96,-240-24);
            
        elif fmv==8:
            
            wn=make_xo(fcp,-96+120,-240-24);
            
        elif fmv==9:
            
           wn=make_xo(fcp,-96+120+120,-240-24);
           
        return wn;
    
def drawboard():

            wind.bgcolor("lightgreen")
            plr.color("black")
            plr.shape("triangle")
            plr.right(90);
            plr.forward(120*3);
            plr.penup();
            plr.goto(120,0);
            plr.pendown();
            plr.forward(120*3);
            
            plr.penup();
            plr.goto(-120,-120);
            plr.pendown();
            plr.left(90);
            plr.forward(120*3);

            plr.penup();
            plr.goto(-120,-240);
            plr.pendown();
            plr.forward(120*3);

def dwb():
    if wincon==1:
            plr.penup();
            plr.goto(-120,-60);
            plr.pendown();
            plr.setheading(0)
            plr.forward(120*3);

    elif wincon==2:
            plr.penup();
            plr.goto(-120,-60-120);
            plr.pendown();
            plr.setheading(0)
            plr.right(0);
            plr.forward(120*3);
        
    elif wincon==3:
            plr.penup();
            plr.goto(-120,-60-240);
            plr.pendown();
            plr.setheading(0)
            plr.right(0);
            plr.forward(120*3);
            
    elif wincon==4:
            plr.penup();
            plr.goto(-60,0);
            plr.pendown();
            plr.setheading(0)
            plr.right(90);
            plr.forward(120*3);

        
    elif wincon==5:
            plr.penup();
            plr.goto(-60+120,0);
            plr.pendown();
            plr.setheading(0)
            plr.right(90);
            plr.forward(120*3);
    elif wincon==6:
            plr.penup();
            plr.goto(-60+120+120,0);
            plr.pendown();
            plr.setheading(0)
            plr.right(90);
            plr.forward(120*3);
        
    elif wincon==7:
            plr.penup();
            plr.goto(-120,0);
            plr.pendown();
            plr.setheading(0)
            plr.right(45);
            plr.forward(120*3.5);

        
    elif wincon==8:
            plr.penup();
            plr.goto(240,0);
            plr.pendown();
            plr.setheading(0)
            plr.right(135);
            plr.forward(120*3.5);

        
def cfw():
    global wincon
    
    i=0
    while i<9:
        i+=1
        if i==1 or i==4 or i==7:
            #horizontal
            if played[i]==played[i+1] and played[i+1]==played[i+2]:
                if i==1:
                    wincon=1
                if i==4:
                    wincon=2
                if i==7:
                    wincon=3
                return True
        if i==1 or i==2 or i==3:
            #vertital
             if played[i]==played[i+3] and played[i+3]==played[i+6]:
                if i==1:
                    wincon=4
                if i==2:
                    wincon=5
                if i==3:
                    wincon=6
                return True
        if i==1:
            #cross to right
             if played[i]==played[i+4] and played[i+4]==played[i+8]:
                wincon=7
                return True
        if i==3:
            #cross to left
             if played[i]==played[i+2] and played[i+2]==played[i+4]:
                wincon=8
                return True
    return False


def gwin():
    if cfw():
        win=True
        return True
    else:
        win=False
        return False

    
def play(fmv):
    if not win:
        if fmv not in op:
            op.append(fmv);
            av.remove(fmv);

            return True
        else:
            global kg
            print("BAD INPUT")
            print("PROGRAM TERMINATED")
            kg=False
            return False
    else:
        return False
#--------------------------------------------------------------

#Setting up screen
print("------------------TIC TAC TOE-----------------------------")
print("PLAYER 1- SELECT X OR O:");
p1=sys.stdin.read(1)
p2='O' if p1=='X' else 'X'
cp=1
av=[1,2,3,4,5,6,7,8,9]
drawboard()
while kg:
    print("AVAILABLE =",av)
    print("ENTER YOUR MOVE PLAYER-",cp," :")
    sys.stdin.read(1);
    mv=sys.stdin.read(1);
    mv=int(mv);

    if play(mv):
        if len(av)>0:
            if not dtm(cp,mv):
               print("")
               
            else:
               dwb();
               print("!!!!!!!!!!!!!!!!!!!!!!!CONGRATULATIONS !!!!!!!!!!!!!!!!!!!!!!!")
               print("PLAYER ",cp," WINS ")
               break;
        else:
            print("------------TIE-------------")
            break;
               
            
    else:
        kg=False
        
    cp=2 if cp==1 else 1
        
print("")
