from graphics import *
import time

class MissionaryAndCannibalsGraphics:

    def __init__(self,NoOfM,NoOfC,States):
        self.NM=NoOfM
        self.NC=NoOfC
        self.States=States
        self.win=GraphWin("prog",410,600)
        

        self.label23 = Text(Point(200,30), 'MISSIONARIES AND CANNIBALS PROBLEM')
        self.label23.draw(self.win)

        self.River=Rectangle(Point(130,60),Point(280,600))
        self.River.setFill('blue')
        self.River.draw(self.win)

        self.Boat=Rectangle(Point(130,300),Point(200,334))
        self.Boat.setFill('yellow')
        self.Boat.draw(self.win)

        self.LeftLabel1=Text(Point(40,200)," M ")
        self.LeftLabel2=Text(Point(90,200)," C ")
        self.LeftLabel1.draw(self.win)
        self.LeftLabel2.draw(self.win)

        self.RightLabel1=Text(Point(320,200)," M ")
        self.RightLabel2=Text(Point(370,200)," C ")
        self.RightLabel1.draw(self.win)
        self.RightLabel2.draw(self.win)

        self.LeftLabel11=Text(Point(40,220),str(self.NM))
        self.LeftLabel22=Text(Point(90,220),str(self.NC))
        self.LeftLabel11.draw(self.win)
        self.LeftLabel22.draw(self.win)

        self.RightLabel11=Text(Point(320,220),str(0))
        self.RightLabel22=Text(Point(370,220),str(0))
        self.RightLabel11.draw(self.win)
        self.RightLabel22.draw(self.win)

        time.sleep(3)
        self.LeftLabel11.undraw()
        self.LeftLabel22.undraw()
        self.RightLabel11.undraw()
        self.RightLabel22.undraw()
    
    def Sail_to_RIGHT(self):
        self.Boat.undraw()
        for i in range(130,218,29):
            self.Boat=Rectangle(Point(i,300),Point(i+70,334))
            self.Boat.setFill('yellow')
            self.Boat.draw(self.win)
            time.sleep(1)
            self.Boat.undraw()
        self.Boat=Rectangle(Point(210,300),Point(280,334))
        self.Boat.setFill('yellow')
        self.Boat.draw(self.win)
        # time.sleep(3)

    def Sail_to_LEFT(self):
        self.Boat.undraw()
        for i in range(218,127,-30):
            self.Boat=Rectangle(Point(i,300),Point(i+70,334))
            self.Boat.setFill('yellow')
            self.Boat.draw(self.win)
            time.sleep(1)
            self.Boat.undraw()

        self.Boat=Rectangle(Point(130,300),Point(200,334))
        self.Boat.setFill('yellow')
        self.Boat.draw(self.win)
        # time.sleep(3)
    
    def UpdateLeftBoard(self,Row,states):
                    self.LeftLabel11=Text(Point(40,Row),str(states[0]))
                    self.LeftLabel22=Text(Point(90,Row),str(states[1]))
                    self.LeftLabel11.draw(self.win)
                    self.LeftLabel22.draw(self.win)
    
    def UpdateRightBoard(self,Row,states):
                    self.RightLabel11=Text(Point(320,Row),str(states[3]))
                    self.RightLabel22=Text(Point(370,Row),str(states[4]))
                    self.RightLabel11.draw(self.win)
                    self.RightLabel22.draw(self.win)

            

        

       

        
        

    def Sail(self):
        Row=220
        for states in self.States:
           
            if states[2]=='l':
                    self.UpdateLeftBoard(Row,states)   
                    self.Sail_to_RIGHT()
                    self.UpdateRightBoard(Row,states)  
                    
            else:
                self.UpdateRightBoard(Row,states) 
                self.Sail_to_LEFT()
                self.UpdateLeftBoard(Row,states)  
            

            time.sleep(5)
            Row=Row+20
        self.Sail_to_RIGHT()
        



        
       

        self.win.getMouse()
        self.win.close()