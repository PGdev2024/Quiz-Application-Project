import colorama  #importing colorama library to add visual effects to the console
from colorama import Fore,Back,Style,init
init()
qno,score=0,0 #global variables
def questiondata(s): #This function manages the response by the user for each question of the quiz
    global qno,score
    qno+=1
    print("Question "+str(qno)+" "+s[0])
    print("A. "+s[1])
    print("B. "+s[2])
    print("C. "+s[3])
    print("D. "+s[4])
    ans=input()
    if(ans==s[5].strip()):
        print("Your Answer: "+ans)
        print(Style.BRIGHT+Fore.GREEN+"Correct!")
        print(Style.RESET_ALL+"")
        score+=1
    else:
        print("Your Answer: "+ans)
        print(Style.BRIGHT+Fore.RED+"Incorrect!")
        print(Style.RESET_ALL+"")   
def quizpresentation(): #This function reads the questions from questions.txt and calls the function which is in control of managing the response by the user
    with open("questions.txt","r") as f: 
        for line in f:
            s1=line.split(",")
            questiondata(s1)
    userscore()
def userscore(): #This function displays the score of the user and stores it along with the user's name in scores.txt
    global name 
    n1=" "+name.strip()+","
    print("Quiz Complete!")
    print("Your Score: "+str(score)+"/"+str(qno))
    finalscore=str(score)+"/"+str(qno)
    with open("scores.txt","a") as f1:
        f1.write(n1)
        f1.write(finalscore)
name=input(Style.DIM+"Enter your name to attempt the quiz"+Style.RESET_ALL)
if(name!=""):
    print(Style.BRIGHT+Fore.WHITE+"Welcome to The Quiz Application!"+Style.RESET_ALL) #The instructions of the quiz which are displayed on the console before the user starts the quiz
    print(Style.BRIGHT+Fore.WHITE+"Rules:"+Style.RESET_ALL)
    print(Style.BRIGHT+Fore.WHITE+"- Each question has 4 options"+Style.RESET_ALL)
    print(Style.BRIGHT+Fore.WHITE+"- Enter the option (A,B,C,D) to enter"+Style.RESET_ALL)
    print(Style.BRIGHT+Fore.WHITE+"Press Enter to start!"+Style.RESET_ALL)
key=input() #Records keyboard input from user for enter key
if key=="":
    quizpresentation()







