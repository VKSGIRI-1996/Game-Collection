from tkinter import *
import sys
w = Tk()
w.geometry("2000x2000")
w.configure(bg ='light cyan')
w.title("All In One")

#Define Function
def Guess_The_Number():
    #a = int(input("Enter the Original Number"))
    print("GUESS THE NUMBER BETWEEN 1 TO 50")
    print()


    a = 24

    n = 4

    def attempt(n):
        if n == 0:
            pass
        else:
            print("You have",n," attempts to Get the Original number")

    def clue(n):
        if n == 3:
            print("Original number is multiple of 2 and 4")
        if n == 2:
            print("Original Number is Not a Square of any Natural Number")
        if n == 1:
            print("Sum of Digits Of original Number is 6")
        

    while True:
        attempt(n)
        clue(n)

        if n == 0:
            print("You Lose the Game")
            print("Original Number is",a)
            break
        
        b = int(input("Enter the Guess Number "))

        if b>a:
            print()
            print("This Number is Greater than Original Number")
            print()
            n = n-1

        elif b<a:
            print()
            print("This Number is Less than Original Number")
            print()
            n = n-1

        else:
            print()
            print("Congratulation! You got the Number")
            print()
            break
        

def Tic_tac():
    import os
    import time # time used for sleep operation inorder to have a startup

    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player=1

    ########win Flags##########    
    Win = 1    
    Draw = -1    
    Running = 0    
    Stop = 1    
    ###########################    
    Game = Running    
    Mark = 'X'    

    #Function to draw game board
    def Drawboard():
        print(" %c | %c | %c " % (board[1],board[2],board[3]))    
        print("___|___|___")    
        print(" %c | %c | %c " % (board[4],board[5],board[6]))    
        print("___|___|___")    
        print(" %c | %c | %c " % (board[7],board[8],board[9]))    
        print("   |   |   ")    


    #Function to check position is empty or not
    def Checkposition(x):
        if(board[x]==' '):
            return True
        else:
            return False
    #Function checks player has won or not
    def Checkwin():
        global Game
        #For horizontal winning condition
        if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
            Game = Win    
        elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
            Game = Win    
        elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
            Game = Win    
        #Vertical Winning Condition    
        elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
            Game = Win    
        elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
            Game = Win    
        elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
            Game=Win    
        #Diagonal Winning Condition    
        elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
            Game = Win    
        elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
            Game=Win    
        #Match Tie or Draw Condition    
        elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
            Game=Draw    
        else:            
            Game=Running    
        



    print("Tic-Tac-Toe Game ")    
    print("Player 1 [X] --- Player 2 [O]\n")
    print()
    print()
    print("Please wait for startup...")
    time.sleep(4) # i.e. 4 seconds
            
    while(Game == Running):
        os.system('cls') # cls helps in executing the command shell
        Drawboard()
        if(player % 2 !=0):
            print("Player 1's chance")
            Mark='X'
        else:
            print("Player 2's chance")
            Mark='O'
        choice = int(input("Enter the position between 1 to 9 where you want to mark:"))
        if(Checkposition(choice)):
            board[choice] = Mark
            player+=1
            Checkwin()
            
    os.system('cls') # to execute the command in subshell
    Drawboard()
    if(Game==Draw):
        print("GAME DRAW")
    elif(Game==Win):
        player-=1
        if(player%2!=0):
            print("PLAYER 1 WON")
        else:
            print("PLAYER 2 WON")



def Typing_Speed():
    pass

def Timer():
    import time
    while True:
        time_set = input("Enter The Setup Time in second(s): ")
        try:
            time_up = abs(int(time_set))
        except KeyboardInterrupt:
            break
        except:
            print("Not A Number!")
        while time_up > 0:
            m,s = divmod(time_up,60)
            h,m = divmod(m,60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left+'\r',end="")
            time.sleep(1)
            time_up -= 1
        print()
        print("Times Up")
        print()
    
def Songs():
    # Importing Required Modules & libraries
    #from tkinter import *
    import pygame
    import os
    # Defining MusicPlayer Class
    class MusicPlayer:
      # Defining Constructor
      def __init__(self,root):
        self.root = root
        # Title of the window
        self.root.title("Music Player")
        # Window Geometry
        self.root.geometry("1000x200+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        # Creating Track Frame for Song label & status label
        trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=400,height=200)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("C:/Users/GIRI PARIWAR/Desktop/c10/songs")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
          self.playlist.insert(END,track)
      # Defining Play Song Function
      def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()
      def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()
      def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()
      def unpausesong(self):
        # Displaying Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()
    # Creating TK Container
    root = Tk()
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
    # Root Window Looping
    root.mainloop()


def Calculator():
    expr=""
    def btnclk(n):
        global expr
        expr = expr + str(n)
        v.set(expr)
    def calculate():
        global expr
        result = eval(expr) #eval("12+5")
        v.set(result)
        pass
    def clear():
        global expr
        expr = ""
        v.set(expr)
    w = Tk()
    v=StringVar()
    w.configure(bg ='green')
    w.title("CALCULATOR")
    # w.geometry("300x200")

    # Design All Components
    E = Entry (w,textvariable=v,justify = "right",bg='cyan',font=('aerial',15,'bold'))
    B1 = Button(w,text="1",font=('aerial',15,'bold'),command=lambda:btnclk(1),bg='blue')
    B2 = Button(w,text="2",font=('aerial',15,'bold'),command=lambda:btnclk(2),bg='blue')
    B3 = Button(w,text="3",font=('aerial',15,'bold'),command=lambda:btnclk(3),bg='blue')
    B4 = Button(w,text="4",font=('aerial',15,'bold'),command=lambda:btnclk(4),bg='blue')
    B5 = Button(w,text="5",font=('aerial',15,'bold'),command=lambda:btnclk(5),bg='blue')
    B6 = Button(w,text="6",font=('aerial',15,'bold'),command=lambda:btnclk(6),bg='blue')
    B7 = Button(w,text="7",font=('aerial',15,'bold'),command=lambda:btnclk(7),bg='blue')
    B8 = Button(w,text="8",font=('aerial',15,'bold'),command=lambda:btnclk(8),bg='blue')
    B9 = Button(w,text="9",font=('aerial',15,'bold'),command=lambda:btnclk(9),bg='blue')
    B0 = Button(w,text="0",font=('aerial',15,'bold'),command=lambda:btnclk(0),bg='blue')
    Bequal = Button(w,text="=",font=('aerial',15,'bold'),command=lambda:calculate(),bg='blue')
    Bclear = Button(w,text="C",font=('aerial',15,'bold'),command=lambda:clear(),bg='blue')
    Bplus = Button(w,text="+",font=('aerial',15,'bold'),command=lambda:btnclk("+"),bg='blue')
    Bminus = Button(w,text="-",font=('aerial',15,'bold'),command=lambda:btnclk("-"),bg='blue')
    Bmul = Button(w  ,text="*",font=('aerial',15,'bold'),command=lambda:btnclk("*"),bg='blue')
    Bdiv = Button(w,text="/",font=('aerial',15,'bold'),command=lambda:btnclk("/"),bg='blue')

    # place all components at proper position
    #row 1
    E.grid(row = 1, column = 1,columnspan = 4)

    #row 2
    B1.grid(row = 2, column = 1)
    B2.grid(row = 2, column = 2)
    B3.grid(row = 2, column = 3)
    B4.grid(row = 2, column = 4)

    #row 3
    B5.grid(row = 3, column = 1)
    B6.grid(row = 3, column = 2)
    B7.grid(row = 3, column = 3)
    B8.grid(row = 3, column = 4)

    #row 4
    B9.grid(row = 4, column = 1)
    B0.grid(row = 4, column = 2)
    Bequal.grid(row = 4, column = 3)
    Bclear.grid(row = 4, column = 4)

    #row 5
    Bplus.grid(row = 5, column = 1)
    Bminus.grid(row = 5, column = 2)
    Bmul.grid(row = 5, column = 3)
    Bdiv.grid(row = 5, column = 4)


    w.mainloop()



#Design All Components
B1 = Button (w,text = "Guess The Number",height = 6, width = 40,font = ('aerial',20,'bold'),command = Guess_The_Number)
B2 = Button (w,text = "Tic Tac",height = 6, width = 40,font = ('aerial',20,'bold'),command = Tic_tac)
B3 = Button (w,text = "Typing_Speed",height = 6, width = 40,font = ('aerial',20,'bold'),command = Typing_Speed)
B4 = Button (w,text = "Clock Timer",height = 6, width = 40,font = ("aerial",20,'bold'),command = Timer)
B5 = Button (w,text = "Waana Go For Top Songs",height = 6, width = 40,font = ('aerial',20,'bold'),command = Songs)
B6 = Button (w,text = "Use Calculator",height = 6, width = 40,font = ("aerial",20,'bold'),command = Calculator)
#L= Label(w, bg = 'green', text  = "Subscribe",height = 2,width = 40,font = ("aerial",20,'bold'))
B7 = Button(w, bg = 'green', text  = "Subscribe",height = 2,width = 40,font = ("aerial",20,'bold'))

#Place All The Components
#Row 1,1
B1.grid(row = 1, column =1, padx = 55, pady = 10)

#Row 1,2
B2.grid(row = 1, column =2)

#Row 2,1 
B3.grid(row = 2, column =1, padx = 55, pady = 10)

#Row 2,2
B4.grid(row = 2, column =2)

#Row 3,1
B5.grid(row = 3, column =1, padx = 55,pady = 10)

#Row 3,2
B6.grid(row = 3, column =2)

#Row 4,1
B7.grid(row = 4, column = 1, columnspan = 2, padx = 200, pady  = 20)

