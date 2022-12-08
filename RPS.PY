from tkinter import 
import random
Comp_dict={
         "0":"Rock",
         "1":"Paper",
         "2":"Scissor"
      }
     #defining Global Variables
     your_choice=""
     Comp_choice=""
     computer_score=0
     your_score=0
     #function to clear the text area where choices are displayed 
def Playagain():
    text_to_display.delete("1.0","end")

#function to update points after every game 
def points():
    text_to_scores.delete("1.0","end")
    text_to_scores.insert(END,f"  {your_score}                   {computer_score}")
    

#function to define what happens when user select Rock 
def rock():
    global computer_score
    global your_score
    your_choice="Rock"
#choosing random variable from the above defined dictionary 
    Comp_choice=Comp_dict[str(random.randint(0,2))]
#to display choices 
    text_to_display.insert(END,f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}"
                           
)
#to increase the scores accordingly 
    if Comp_choice=="Paper":
        computer_score+=1
    if Comp_choice=="Scissor":
        your_score+=1
    points()

#same as the above function   
def paper():
    global computer_score
    global your_score
    your_choice="Paper"
    Comp_choice=Comp_dict[str(random.randint(0,2))]
    text_to_display.insert(END,f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}"
)
    if Comp_choice=="Scissor":
        computer_score+=1
    if Comp_choice=="Rock":
        your_score+=1
    points()
def scissor():
    global computer_score
    global your_score
    your_choice="Scissor"
    Comp_choice=Comp_dict[str(random.randint(0,2))]
    text_to_display.insert(END,f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}"
)
    if Comp_choice=="Rock":
        computer_score+=1
    if Comp_choice=="Paper":
        your_score+=1
    points()