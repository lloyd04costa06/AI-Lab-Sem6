from graphics import *
import time

class JUGS:

    def __init__(self,jug1Size,jug2Size,goal):
        self.jug1S=jug1Size
        self.jug2S=jug2Size
        self.g=goal
        self.win=GraphWin("prog",400,600)
        self.label1 = Text(Point(100,200+self.jug1S*10+10), 'Jug-1')
        self.label1.draw(self.win)

        self.label2 = Text(Point(250,200+self.jug1S*10+10), 'Jug-2')
        self.label2.draw(self.win)

        self.label23 = Text(Point(200,30), 'WATER JUG PROBLEM')
        self.label23.draw(self.win)

        self.jug1=Rectangle(Point(60,200-self.jug1S*10),Point(160,200+self.jug1S*10))
        self.jug1.draw(self.win)

        self.jug2=Rectangle(Point(310,200-self.jug2S*10),Point(210,200+self.jug1S*10))
        self.jug2.draw(self.win)

        self.Law={
            1:"Fill Jug-1",
            2:"Fill Jug-2",
            3:"Empty Jug-1",
            4:"Empty Jug-2",
            5:"Pour Water from Jug-2 to Jug-1 until Jug-1 is Full",
            6:"Pour Water from Jug-1 to Jug-2 until Jug-1 is Full",
            7:"Transfer Entire amount of Jug-2 to Jug1",
            8:"Transfer Entire amount of Jug-1 to Jug2",
            None:"Initial State"
        }



        

    def JugAction(self,lis):
        
        r=50
        z=200+self.jug1S*10+80
        RU=200+self.jug1S*10+280
        for j in lis:
            if r%400==0:
                r=50
                z=z+20
                
            self.label4 = Text(Point(r, z), str(j))
            self.label4.draw(self.win)

            self.label43 = Text(Point(200, RU), str(self.Law[j.rule]))
            self.label43.draw(self.win)
        
            if j.x!=0:
                self.jug1Water=Rectangle(Point(60,200-j.x*10),Point(160,200+self.jug1S*10))
                self.jug1Water.setFill("blue")
                self.jug1Water.draw(self.win)

            if j.y!=0:
                self.jug2Water=Rectangle(Point(310,200-j.y*10),Point(210,200+self.jug1S*10))
                self.jug2Water.setFill("blue")
                self.jug2Water.draw(self.win)

            time.sleep(5)
            
            if j.x!=0:
                self.jug1Water.undraw()
            if j.y!=0:
                self.jug2Water.undraw()
            self.label43.undraw()
            r=r+50

        self.jug1Water=Rectangle(Point(60,200-self.g.x*10),Point(160,200+self.jug1S*10))
        self.jug1Water.setFill("blue")
        self.jug1Water.draw(self.win)
        
        
           
            
         
              

            
            


        self.win.getMouse()
        self.win.close()

    # jug2Water=Rectangle(Point(300,50),Point(200,200))
    # jug2Water.setFill("blue")
    # jug2Water.draw(win)
   
