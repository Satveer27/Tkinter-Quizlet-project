# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:08:29 2022

@author: dabis
"""
#imports so we can use the features
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import time
window = tk.Toplevel() #the whole window here is assigned to tkinter





#function for username tab
def tab1():
    label1.destroy() #destroy() enables us to destroy labels or antyhing placed down in tkinter
    btn.destroy()
    btn2.destroy()
    window.configure(bg="#A44CD3")
    label2 = tk.Label(window,text="KAHOOD!",fg="white",bg="#A44CD3") # This is a label that is being configurated and placed down. 
    label2.config(font=('Comic Sans MS','100','underline',"bold")) 
    label2.pack() # pack() allows the program to choose where to place your label or any variable it is assigned to place down.
    def fake_text(e): # The following 4 lines of code was taken from https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
        entrybox.delete(0,"end")
    entrybox = Entry(window, bg="white", width=20,font=('Arial 50'), borderwidth=10) #This is a entrybox, where we must input data.
    entrybox.insert(0, "enter your username") 
    entrybox.pack(pady=200) 

    entrybox.bind("<FocusIn>", fake_text) # This is basically a fake text, once the entrybox is clicked the text will dissapear
     
     
    btn_back = Button(window,text="quit",command=window.destroy,fg="white",bg="black",) # This is a button which has a command to end the whole program if clicked
    btn_back.config(font=('Comic Sans MS','60'))
    btn_back.pack(side=LEFT,pady=3)
    
    correction = Label(window,text='',bg="#A44CD3",fg="yellow") # This label is for future references, we will need to use it in the next function.
    correction.pack(pady=20)
    
   


    
    
    #function for checking the username tab
    def tab2():
      entrybox1  = entrybox.get() # This allows us to get the input from the entrybox, basically what username the user has entered     
      allowed_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','(',')','$','%','_','/']
      if any(x not in allowed_characters for x in entrybox1) or len(entrybox1)==0 or len(entrybox1)>16: # This will check what has inputted in the entrybox to see weather or not its valid, if the length of the data is 0, or more than 16 or a character is not in the list above then a error message is shown.
         correction.config(text="Please enter a username with valid characters or a username which doesnt exceed 16 characters.") #The correction from before has been configurated from before to show a error message.
     
          
      else: #this block is follows if the users input doesnt match the validations listed above, this then would make a whole new page to display for the user. The page displayed here is the category page.
              window.configure(bg="white")  
              btn_back.destroy()
              label2.destroy()
              btn_next.destroy()
              correction.destroy()
              entrybox.destroy()
              label_check = Label(window,text=entrybox1,bg="#A44CD3",fg="white",width=50,height=5)
              label_check.place(x=0, y=0)#the place() block enables you to exactly place down where you would want the label to be
              Label_brand = Label(window,text="KAHOOD",bg="#A44CD3",fg="white",width=50,height=5)
              Label_brand.place(x=1400,y=0)
              Label3 = Label(window,text="",bg="#A44CD3",fg="white",width=160,height=5).place(x=300,y=0)
              Label_cat = Label(window,text="Categories",fg="blue",bg="white")
              Label_cat.config(font=('Comic Sans MS','100','underline'))
              Label_cat.pack(padx=90,pady=90)
              global photo1 #global basically enables to use photo1 here in other functions or outside the else statement.
              global resized_photo2
              global new_image2
              global photomath
              global resized_photomath
              global new_imagemath
              photo1 = (Image.open("anime.jpg")) # This block opens a image to use further in the program, the following 5 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
              resized_photo2 = photo1.resize((500,300),Image. ANTIALIAS) # This block is to resize the image
              new_image2= ImageTk.PhotoImage(resized_photo2) 
              photomath = (Image.open("factorial.jpg"))
              resized_photomath = photomath.resize((500,300),Image. ANTIALIAS)
              new_imagemath= ImageTk.PhotoImage(resized_photomath)
              
              
              
              #This is the factorial page, first comes the rule page. The rules will be explained here. Using labels
              def factorial_page():
                     window.config(bg = "white")
                     btn_factorial.destroy()
                     btn_math.destroy()
                     Label_cat.destroy()
                     Label_rule = Label(window,text="Rules",fg="Red",bg="white")
                     Label_rule.config(font=('Comic Sans MS','100','underline'))
                     Label_rule.pack(padx=90,pady=90)
                     label_rule1 = Label(window,text="-Type in a factorial of your choice",bg="white")
                     label_rule1.config(font=('Comic Sans MS','30'))
                     label_rule1.pack(padx=0,pady=0)
                     label_rule2=Label(window,text="-Calculate it and then place the answer in the box",bg="white")
                     label_rule2.config(font=('Comic Sans MS','30'))
                     label_rule2.pack(padx=0,pady=0)
                     label_rule4=Label(window,text="-You will have unlimited time to answer.",bg="white")
                     label_rule4.config(font=('Comic Sans MS','30'))
                     label_rule4.pack(padx=0,pady=0)
                  
                    
                     #Next part is where the user gets to choose any number they would like to get factorial. Only numbers or else a exception will be raised. 
                     def factorial_page2():
                         label_rule4.destroy()
                         Label_rule.destroy()
                         label_rule1.destroy()
                         label_rule2.destroy()
                         start_quiz_btn.destroy()
                         Label_question1= Label(window,text="Whats your factorial?",bg="white")
                         Label_question1.config(font=('Comic Sans MS','40'))
                         Label_question1.pack(padx=100,pady=100)
                         def fake_text(e):
                                 answer.delete(0,"end")
                         answer = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                         answer.pack(padx=100,pady=100)
                         answer.insert(0, "enter your number here!")
                         answer.bind("<FocusIn>", fake_text)
                         Label_error= Label(window,text="Sorry please enter a number, not a alphabet or don't leave it blank",bg="white",font=('Arial 20'))
                         
                         
                         # This part the calculation will be done to collect the results of the factorial, it will also as the user to answer the factorial of the number he inputted.
                         def check_ansfact():
                             answer.destroy()
                             Label_question1.destroy()
                             Label_error.destroy()
                             btn_checkfact.destroy()
                             
                             
                             #This part takes the input of the user and if its 1 then the result would be 1. However if its not 1, a recursive loop will happen. Where the input would multiply with its own self and minus 1 each loop.
                             def factorial(r):
                               if r == 1:
                                   return r
                               else:
                                   return r*factorial(r-1)
                               
                             #The results will then be collected here. The user here will input the answer to his input factorial. A exception will be raised if the user doesnt input a number.   
                             global result
                             result = factorial(r)
                             Label_question2= Label(window,text="Whats your answer?",bg="white")
                             Label_question2.config(font=('Comic Sans MS','40'))
                             Label_question2.pack(padx=100,pady=100)
                             def fake_text(e):
                                     answer1.delete(0,"end")
                             answer1 = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                             answer1.pack(padx=100,pady=100)
                             answer1.insert(0, "enter your answer here!")
                             answer1.bind("<FocusIn>", fake_text)
                             Label_error1= Label(window,text="Sorry please enter a number, not a alphabet or don't leave it blank",bg="white",font=('Arial 20'))
                             
                             
                             #This part of the function checks his result and displays the correct or wrong page.
                             def check_ansfact1():
                                 answer1.destroy()
                                 Label_question2.destroy()
                                 Label_error1.destroy()
                                 btn_checkfact1.destroy()
                                 if x == result:
                                     window.configure(bg="green")
                                     Label_sign_fact = Label(window, text = "Congrats!you are correct! answer is:", fg="yellow",bg="green",font=('Arial 50'))
                                     Label_sign_fact.place(x=450,y=300)
                                     Label_correct_sign = Label(window, text = result, fg="yellow",bg="green",font=('Arial 50'))
                                     Label_correct_sign.place(x=450,y=500)
                                     
                                 else:
                                     window.configure(bg="red")
                                     Label_sign_fact = Label(window, text = "SORRY!you are wrong! answer is :", fg="black",bg="red",font=('Arial 50'))
                                     Label_sign_fact.place(x=450,y=300)
                                     Label_correct_sign = Label(window, text = result, fg="yellow",bg="red",font=('Arial 50'))
                                     Label_correct_sign.place(x=450,y=500)
                                   
                                    
                                   
                                 #This function basically goes back to the factorial function to retry the factorial if he gets it wrong.  
                                 def retry1():
                                     Label_sign_fact.destroy()
                                     Label_correct_sign.destroy()
                                     btn_retry.destroy()
                                     btn_return.destroy()
                                     factorial_page()
                                     
                                   
                                     
                                   
                                  #This function basically goes back to username section if the user wants to try other categories.  
                                 def return1():
                                     Label_sign_fact.destroy()
                                     Label_correct_sign.destroy()
                                     btn_retry.destroy()
                                     btn_return.destroy()
                                     label_check.destroy()
                                     Label_brand.destroy()
                                     tab1()
                                 
                                    
                                 
                                    
                                 #This is the retry button which connects to the retry function
                                 btn_retry = Button(window,text="retry",command=retry1,fg="white",bg="black",width=40,height=5)
                                 btn_retry.place(x=1400,y=800)
                                 
                                 
                                 
                                 #This is the return button which connects to the return function
                                 btn_return = Button(window,text="exit",command=return1,fg="white",bg="black",width=40,height=5)
                                 btn_return.place(x=1400,y=600)
                         
                            
                         
                            
                             #This is exception function to get the answer to the user own factorial. If the user inputs a value other than integer data type a error will be raised. 
                             def exceptionqfact1():
                                 try:
                                     int(answer1.get())
                                     global x
                                     x = int(answer1.get())
                                     check_ansfact1()
                                 except ValueError:
                                     Label_error1.place(x=300,y=800)
                             
                                     
                             
                                
                             #This button is after the user types his answer, it will lead to do some exception checks at the exception function.
                             btn_checkfact1 = Button(window,text="next",command=exceptionqfact1,fg="white",bg="black",width=40,height=5)
                             btn_checkfact1.place(x=1400,y=800) 
                         
                         
                         
                         
                         #This is exception function to get the input of the factorial. If the user inputs a value other than integer data type a error will be raised. 
                         def exceptionqfact():
                             try:
                                 int(answer.get())
                                 global r
                                 r = int(answer.get())
                                 check_ansfact()
                             except ValueError:
                                 Label_error.place(x=300,y=800)
                        
                                 


                         #This button is after the user types his input, it will lead to do some exception checks at the exception function.
                         btn_checkfact = Button(window,text="next",command=exceptionqfact,fg="white",bg="black",width=40,height=5)
                         btn_checkfact.place(x=1400,y=800)    
                         
                         
                     
                        
                        
                     #This button is to start the factorial small quiz
                     start_quiz_btn= Button(window,text="START",bg="black",fg="white",command = factorial_page2)
                     start_quiz_btn.config(font=('Comic Sans MS','60'))
                     start_quiz_btn.pack(side= RIGHT, padx =700,pady=50)
            
              # This function is to display the rules in the anime quiz.
              def tab4():
                    window.configure(bg="white")
                    btn_factorial.destroy()
                    btn_math.destroy()
                    Label_cat.destroy()
                    Label_rule = Label(window,text="Rules",fg="Red",bg="white")
                    Label_rule.config(font=('Comic Sans MS','100','underline'))
                    Label_rule.pack(padx=90,pady=90)
                    label_rule1 = Label(window,text="-You have a 15 second time limit for each question.",bg="white")
                    label_rule1.config(font=('Comic Sans MS','30'))
                    label_rule1.pack(padx=0,pady=0)
                    label_rule2=Label(window,text="-There are 5 questions, the moment you start the question the timer will also start.",bg="white")
                    label_rule2.config(font=('Comic Sans MS','30'))
                    label_rule2.pack(padx=0,pady=0)
                    label_rule3=Label(window,text="-If the timer runs out and you have typed the answer in the box,",bg="white")
                    label_rule3.config(font=('Comic Sans MS','30'))
                    label_rule3.pack(padx=0,pady=0)
                    label_rule4=Label(window,text="the answer will be checked",bg="white")
                    label_rule4.config(font=('Comic Sans MS','30'))
                    label_rule4.pack(padx=0,pady=0)
                    
                    
                    #This function is the loading screen, for 5 seconds. It also shows the question in the process. The question is picked from the txt.file and placed in a list dictionary.
                    def loading():
                        label_rule4.destroy()
                        label_rule3.destroy()
                        Label_rule.destroy()
                        label_rule1.destroy()
                        label_rule2.destroy()
                        start_quiz_btn.destroy()
                        with open('animequestions.txt') as f: # This opens the file 
                          a = dict(i.rstrip().split(None, 1) for i in f) # This takes each item in the file as if the item in the file has a space. For example if my item in txt.file is "Q1 BLA BLA", the dictionary key will be Q1 and values are "BLA BLA".
                          Label_question= Label(window,text=a['Q1'],bg="white")
                          Label_question.config(font=('Comic Sans MS','40'))
                          Label_question.pack(padx=300,pady=300)
                          global amount_of_points2
                          amount_of_points2 = 0
                          point = Label(window,text=amount_of_points2,fg="white",bg="black",width=10,height=2)
                          point.place(x=800,y=30)
                          point_label = Label(window,text="Points gained:",fg="white",bg="black",width=10,height=2).place(x=700,y=30)
                          sign_label = Label(window,text = "Loading please wait....",bg="white")
                          sign_label.config(font=('Comic Sans MS','20'))
                          sign_label.pack(padx=100,pady=50)
                          
                          
                          
                          
                          # This is the first question. A photo is placed down and a entrybox witha fake text will appear. The user will be required to guess the correct answer for question 1. The question is taken from dictionary as a label.
                          def q1():
                              sign_label.destroy()
                              Label_question.destroy()
                              
                              Label_question1= Label(window,text=a['Q1'],bg="white")
                              Label_question1.config(font=('Comic Sans MS','40'))
                              Label_question1.pack(padx=100,pady=100)
                              global photo_q1
                              global new_image_q1
                              global new_image_q1#the following 5 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
                              photo_q1 = (Image.open("manga anime.jpg"))
                              resized_photo_q1 = photo_q1.resize((500,300),Image. ANTIALIAS) 
                              new_image_q1= ImageTk.PhotoImage(resized_photo_q1) 
                              image_label_q1= Label(window,image = new_image_q1)
                              image_label_q1.pack() 
                              def fake_text(e):#The following 4 lines of code was taken from https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
                                 answer_q1.delete(0,"end")
                              answer_q1 = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                              answer_q1.pack(padx=100,pady=100)
                              answer_q1.insert(0, "enter your answer here!")
                              answer_q1.bind("<FocusIn>", fake_text)
                              correction1 = Label(window,text='',fg="black")
                              correction2 = Label(window,text='',fg="black")
                              correction1.place(x=100,y=850)
                              correction2.place(x=800,y=850)
                              with open('answer.txt') as f:
                                  ans = dict(i.rstrip().split(None, 1) for i in f)
                                  answer_to_1 = ans['Ans1']
                                  alternate_1 = ans['Alt_ans'] # There are 2 awnswers, therefore the dictionary contains 2 answers collected from the file.
                                  
                             
                              
                             
                                
                             
                              def check1(): # here the answer to question1 will be checked. Two tabs are made, correctab and  wrongtab. The correctab displays a window that answer is correct if the users answer is exactly the answer provided. or else it will go to a wrongtab. The answers are taken from the function above in another text file and placed as dictionary.
                                  check_answer_1=answer_q1.get()
                                  
                                  global correctab
                                  def correctab():
                                   window.configure(bg="green")
                                   global Label_sign_q1
                                   Label_sign_q1 = Label(window, text = "Congrats!you are correct!", fg="yellow",bg="green",font=('Arial 50'))
                                   Label_sign_q1.place(x=450,y=300)
                                   global Label_correct_sign
                                   Label_correct_sign = Label(window, text = "100 points have been awarded!", fg="yellow",bg="green",font=('Arial 50'))
                                   Label_correct_sign.place(x=450,y=500)
                                   
                                  global wrongtab
                                  def wrongtab():
                                    window.configure(bg="red")
                                    global Label_sign_q1
                                    Label_sign_q1 = Label(window, text = "SORRY!you are wrong", fg="black",bg="red",font=('Arial 50'))
                                    Label_sign_q1.place(x=450,y=300)
                                    global Label_correct_sign
                                    Label_correct_sign = Label(window, text = "0 points have been awarded...", fg="black",bg="red",font=('Arial 50'))
                                    Label_correct_sign.place(x=450,y=500)
                                   
                                  if check_answer_1 == answer_to_1 or check_answer_1 == alternate_1:
                                      window.after_cancel(time3)
                                      answer_q1.destroy()
                                      image_label_q1.destroy()
                                      correction1.destroy()
                                      correction2.destroy()
                                      Label_question1.destroy()
                                      btn_next2.destroy()
                                      point.destroy()
                                      global amount_of_points
                                      amount_of_points = amount_of_points2 + 100 # each time the user gets correct, the amount of points will increment by a 100, if wrong then it increments by none.
                                      global point_after
                                      point_after = Label(window,text=amount_of_points,fg="white",bg="black",width=10,height=2)
                                      point_after.place(x=800,y=30)
                                      correctab()
                                      
                            
                                     
                                  else:
                                      window.after_cancel(time3)
                                      btn_next2.destroy()
                                      answer_q1.destroy()
                                      correction1.destroy()
                                      correction2.destroy()
                                      Label_question1.destroy()
                                      image_label_q1.destroy()
                                      point.destroy()
                                      amount_of_points = amount_of_points2 + 0
                                      point_after = Label(window,text=amount_of_points,fg="white",bg="black",width=10,height=2)
                                      point_after.place(x=800,y=30)
                                      wrongtab()
                                      #at the end of each tab there is always a button to go next. It has to be placed all the way below to go next page or else an error will occur.
                                      
                               
                                
                                    # Once the button is pressed, the user will be led to the second loading page before question2.
                              def loading1():
                                     window.config(bg="white")
                                     btn_nextq2.destroy()
                                     Label_correct_sign.destroy()
                                     Label_sign_q1.destroy()
                                     Label_question= Label(window,text=a['Q2'],bg="white")
                                     Label_question.config(font=('Comic Sans MS','40'))
                                     Label_question.pack(padx=100,pady=100)
                                     sign_label = Label(window,text = "Loading please wait....",bg="white")
                                     sign_label.config(font=('Comic Sans MS','20'))
                                     sign_label.pack(padx=100,pady=50)  
                                     
                                     
                                     
                                     # In question 2 a similar approach will occur, except this time there will be a error raised. That is if the user types nothing or a wrong data type which isnt integer. The exception is all the way below however the label error is assigned in here.
                                     def q2():
                                          sign_label.destroy()
                                          global photo_q2
                                          global new_image_q2
                                          global new_image_q2#the following 5 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
                                          photo_q2 = (Image.open("naruto1.jpg"))
                                          resized_photo_q2 = photo_q2.resize((500,300),Image. ANTIALIAS) 
                                          new_image_q2= ImageTk.PhotoImage(resized_photo_q2) 
                                          image_label_q2= Label(window,image = new_image_q2)
                                          image_label_q2.pack() 
                                          def fake_text(e):#The following 4 lines of code was taken from https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
                                             answer_q2.delete(0,"end")
                                          answer_q2 = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                                          answer_q2.pack(padx=100,pady=100)
                                          answer_q2.insert(0, "enter your answer here!")
                                          answer_q2.bind("<FocusIn>", fake_text)  
                                          answer_to_2 = ans['Ans2']
                                          global Label_error
                                          Label_error= Label(window,text="Sorry please enter a number, not a alphabet or don't leave it blank",bg="white",font=('Arial 20'))
                                          
                                          
                                          
                                          
                                          def check_ans2(): # here the answer inputted to question 2 will be checked.
                                              ans_q2 = answer_q2.get()
                                              if ans_q2 == answer_to_2:
                                                  window.after_cancel(time4)
                                                  Label_error.destroy()
                                                  btn_checkq2.destroy()
                                                  point_after.destroy()
                                                  answer_q2.destroy()
                                                  image_label_q2.destroy()
                                                  Label_question.destroy()
                                                  amount_of_points3 = amount_of_points + 100
                                                  point_afterq2 = Label(window,text=amount_of_points3,fg="white",bg="black",width=10,height=2)
                                                  point_afterq2.place(x=800,y=30)
                                                  correctab()
                                              else:
                                                  window.after_cancel(time4)
                                                  Label_error.destroy()
                                                  btn_checkq2.destroy()
                                                  point_after.destroy()
                                                  answer_q2.destroy()
                                                  image_label_q2.destroy()
                                                  Label_question.destroy()
                                                  amount_of_points3 = amount_of_points + 0
                                                  point_afterq2 = Label(window,text=amount_of_points3,fg="white",bg="black",width=10,height=2)
                                                  point_afterq2.place(x=800,y=30)
                                                  wrongtab()
                                              
                                                
                                              
                                               # This is the loading tab before question 3. 
                                              def loading3():
                                                 window.config(bg="white")
                                                 btn_nextq3.destroy()
                                                 Label_correct_sign.destroy()
                                                 Label_sign_q1.destroy()
                                                 Label_question= Label(window,text=a['Q3'],bg="white")
                                                 Label_question.config(font=('Comic Sans MS','40'))
                                                 Label_question.pack(padx=100,pady=100)
                                                 sign_label = Label(window,text = "Loading please wait....",bg="white")
                                                 sign_label.config(font=('Comic Sans MS','20'))
                                                 sign_label.pack(padx=100,pady=50) 
                                                 
                                                 
                                                 
                                                 # Question 3 here is placed, exactly like question 2 however this time there isn't any exceptions.
                                                 def q3():
                                                     sign_label.destroy()
                                                     global photo_q3
                                                     global new_image_q3
                                                     global new_image_q3
                                                     photo_q3 = (Image.open("emiya.jpg"))#the following 5 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
                                                     resized_photo_q3 = photo_q3.resize((500,300),Image. ANTIALIAS) 
                                                     new_image_q3= ImageTk.PhotoImage(resized_photo_q3) 
                                                     image_label_q3= Label(window,image = new_image_q3)
                                                     image_label_q3.pack() 
                                                     def fake_text(e):#The following 4 lines of code was taken from https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
                                                        answer_q3.delete(0,"end")
                                                     answer_q3 = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                                                     answer_q3.pack(padx=100,pady=100)
                                                     answer_q3.insert(0, "enter your answer here!")
                                                     answer_q3.bind("<FocusIn>", fake_text)  
                                                     answer_to_3 = ans['Ans3']
                                                     alt_ans_3 = ans['Alt_ans3']
                                                     
                                                     
                                                     
                                                     # This is to check question3 just like all the other questions
                                                     def check_q3():
                                                         ans3 = answer_q3.get()
                                                         if ans3 == answer_to_3 or ans3 == alt_ans_3:
                                                             window.after_cancel(time5)
                                                             Label_question.destroy()
                                                             answer_q3.destroy()
                                                             image_label_q3.destroy()
                                                             btn_next_q3.destroy()
                                                             amount_of_points4 = amount_of_points3 + 100
                                                             point_afterq3 = Label(window,text=amount_of_points4,fg="white",bg="black",width=10,height=2)
                                                             point_afterq3.place(x=800,y=30)
                                                             correctab()
                                                         else:
                                                             window.after_cancel(time5)
                                                             Label_question.destroy()
                                                             answer_q3.destroy()
                                                             image_label_q3.destroy()
                                                             btn_next_q3.destroy()
                                                             amount_of_points4 = amount_of_points3 + 0
                                                             point_afterq3 = Label(window,text=amount_of_points4,fg="white",bg="black",width=10,height=2)
                                                             point_afterq3.place(x=800,y=30)
                                                             wrongtab()
                                                          
                                                             
                                                          
                                                            
                                                          # This is the loading screen before question4
                                                         def loading4():
                                                             window.config(bg="white")
                                                             btn_nextq4.destroy()
                                                             Label_correct_sign.destroy()
                                                             Label_sign_q1.destroy()
                                                             Label_question= Label(window,text=a['Q4'],bg="white")
                                                             Label_question.config(font=('Comic Sans MS','40'))
                                                             Label_question.pack(padx=100,pady=100)
                                                             sign_label = Label(window,text = "Loading please wait....",bg="white")
                                                             sign_label.config(font=('Comic Sans MS','20'))
                                                             sign_label.pack(padx=100,pady=50) 
                                                             
                                                             
                                                             
                                                             # This is to make the window to answer question4, this time a exception is raised, just like in question2.
                                                             def q4():
                                                                 sign_label.destroy()
                                                                 global photo_q4
                                                                 global new_image_q4
                                                                 global new_image_q4#the following 5 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
                                                                 photo_q4 = (Image.open("senku3.jpg"))
                                                                 resized_photo_q4 = photo_q4.resize((500,300),Image. ANTIALIAS) 
                                                                 new_image_q4= ImageTk.PhotoImage(resized_photo_q4) 
                                                                 image_label_q4= Label(window,image = new_image_q4)
                                                                 image_label_q4.pack() 
                                                                 def fake_text(e):#The following 4 lines of code was taken from https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
                                                                    answer_q4.delete(0,"end")
                                                                 answer_q4 = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                                                                 answer_q4.pack(padx=100,pady=100)
                                                                 answer_q4.insert(0, "enter your answer here!")
                                                                 answer_q4.bind("<FocusIn>", fake_text)  
                                                                 answer_to_4 = ans['Ans4']
                                                                 global Label_error4
                                                                 Label_error4= Label(window,text="Sorry please enter a number, not a alphabet or try not to leave it blank",bg="white",font=('Arial 20'))
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 #This is to check question 4.
                                                                 def check_ans4():
                                                                   ans_q4 = answer_q4.get()
                                                                   if ans_q4 == answer_to_4:
                                                                       window.after_cancel(time6)
                                                                       Label_error4.destroy()
                                                                       btn_checkq4.destroy()
                                                                       point_afterq3.destroy()
                                                                       answer_q4.destroy()
                                                                       image_label_q4.destroy()
                                                                       Label_question.destroy()
                                                                       amount_of_points5 = amount_of_points4 + 100
                                                                       point_afterq4 = Label(window,text=amount_of_points5,fg="white",bg="black",width=10,height=2)
                                                                       point_afterq4.place(x=800,y=30)
                                                                       correctab()
                                                                   else:
                                                                       window.after_cancel(time6)
                                                                       Label_error4.destroy()
                                                                       btn_checkq4.destroy()
                                                                       point_afterq3.destroy()
                                                                       answer_q4.destroy()
                                                                       image_label_q4.destroy()
                                                                       Label_question.destroy()
                                                                       amount_of_points5 = amount_of_points4 + 0
                                                                       point_afterq4 = Label(window,text=amount_of_points5,fg="white",bg="black",width=10,height=2)
                                                                       point_afterq4.place(x=800,y=30)
                                                                       wrongtab()
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   # This is the loading screen before question5
                                                                   def loading5():
                                                                       window.config(bg="white")
                                                                       btn_nextq5.destroy()
                                                                       Label_correct_sign.destroy()
                                                                       Label_sign_q1.destroy()
                                                                       Label_question= Label(window,text=a['Q5'],bg="white")
                                                                       Label_question.config(font=('Comic Sans MS','40'))
                                                                       Label_question.pack(padx=100,pady=100)
                                                                       sign_label = Label(window,text = "Loading please wait....",bg="white")
                                                                       sign_label.config(font=('Comic Sans MS','20'))
                                                                       sign_label.pack(padx=100,pady=50) 
                                                                       
                                                                       
                                                                       
                                                                       
                                                                       #This is to display question5 in a window, however no exception is made here.
                                                                       def q5():
                                                                           sign_label.destroy()
                                                                           global photo_q5
                                                                           global new_image_q5
                                                                           global new_image_q5#the following 5 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
                                                                           photo_q5 = (Image.open("hunter.jpg"))
                                                                           resized_photo_q5 = photo_q5.resize((500,300),Image. ANTIALIAS) 
                                                                           new_image_q5= ImageTk.PhotoImage(resized_photo_q5) 
                                                                           image_label_q5= Label(window,image = new_image_q5)
                                                                           image_label_q5.pack() 
                                                                           def fake_text(e):#The following 4 lines of code was taken from https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
                                                                              answer_q5.delete(0,"end")
                                                                           answer_q5 = Entry(window,width=30,fg="red",bg="yellow",font=('Arial 50'))
                                                                           answer_q5.pack(padx=100,pady=100)
                                                                           answer_q5.insert(0, "enter your answer here!")
                                                                           answer_q5.bind("<FocusIn>", fake_text)  
                                                                           answer_to_5 = ans['Ans5']
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           # This is to check question 5 which is the final question. The button will then lead to the leaderboard page.
                                                                           def check_ans5():
                                                                             ans_q5 = answer_q5.get()
                                                                             if ans_q5 == answer_to_5:
                                                                                 window.after_cancel(time7)
                                                                                 btn_checkq5.destroy()
                                                                                 point_afterq4.destroy()
                                                                                 answer_q5.destroy()
                                                                                 image_label_q5.destroy()
                                                                                 Label_question.destroy()
                                                                                 amount_of_points6 = amount_of_points5 + 100
                                                                                 point_afterq5 = Label(window,text=amount_of_points6,fg="white",bg="black",width=10,height=2)
                                                                                 point_afterq5.place(x=800,y=30)
                                                                                 correctab()
                                                                             else:
                                                                                 window.after_cancel(time7)
                                                                                 btn_checkq5.destroy()
                                                                                 point_afterq4.destroy()
                                                                                 answer_q5.destroy()
                                                                                 image_label_q5.destroy()
                                                                                 Label_question.destroy()
                                                                                 amount_of_points6 = amount_of_points5 + 0
                                                                                 point_afterq5 = Label(window,text=amount_of_points6,fg="white",bg="black",width=10,height=2)
                                                                                 point_afterq5.place(x=800,y=30)
                                                                                 wrongtab()
                                                                                 
                                                                                 
                                                                             
                                                                                 
                                                                             #The leaderboard page where the leaderboard is displayed.
                                                                             def leaderboard():
                                                                                 window.config(bg="black")
                                                                                 btn_leaderboard.destroy()
                                                                                 Label_correct_sign.destroy()
                                                                                 Label_sign_q1.destroy()
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 def points(): # The points are taken and stored in a text file as string.
                                                                                     with open("amount of point.txt", "a") as a_file:
                                                                                      a_file.write("\n")
                                                                                      a_file.write(str(amount_of_points6))
                                                                                          
                                                                                 points()
                                                                                    
                                                                                    
                                                                                    
                                                                                 f = open("amount of point.txt","r")
                                                                                    
                                                                                 # The file is then open again and the program will take the content and append them into a list. The list will then be sorted out. The labels will then display top 5 items in the list.   
                                                                                 with open('amount of point.txt') as f:
                                                                                     my_list = [ int(x) for x in f.read().split()]
                                                                                     my_list1 = [0,0,0,0,0]
                                                                                     final_list = my_list1 + my_list
                                                                                     final_list.sort(reverse=True) 
                                                                                     Label_leaderboard = Label(window,text="leaderboard",fg='red',bg="black")
                                                                                     Label_leaderboard.config(font = ('Arial','60','underline'))
                                                                                     Label_leaderboard.pack(padx =100,pady=100)
                                                                                     Label_name1= Label(window,text="username:",bg="black", fg="red",font = 'Arial 50')
                                                                                     Label_name1.place(x =0,y=200)
                                                                                     Label_name= Label(window,text=entrybox1,bg="black",fg='red',font = 'Arial 50')
                                                                                     Label_name.place(x =500,y=200)
                                                                                     Label_first1= Label(window,text="1st:",bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_first1.place(x =50,y=400)
                                                                                     Label_first= Label(window,text=final_list[0],bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_first.place(x =500,y=400)
                        
                                                                                     Label_2nd= Label(window,text="2nd:",bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_2nd.place(x =50,y=500)
                                                                                     Label_second= Label(window,text=final_list[1],bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_second.place(x =500,y=500)
                                                                                     
                                                                                     Label_3rd= Label(window,text="3rd:",bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_3rd.place(x =50,y=600)
                                                                                     Label_third= Label(window,text=final_list[2],bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_third.place(x =500,y=600)
                                                                                     
                                                                                     Label_4th= Label(window,text="4th:",bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_4th.place(x =50,y=700)
                                                                                     Label_fourth= Label(window,text=final_list[3],bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_fourth.place(x =500,y=700)
                                                                                     
                                                                                     Label_5th= Label(window,text="5th:",bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_5th.place(x =50,y=800)
                                                                                     Label_fifth= Label(window,text=final_list[4],bg="black",fg="red",font = 'Arial 50')
                                                                                     Label_fifth.place(x =500,y=800)
                                                                                     
                                                                                     
                                                                                     #This is a retry function. If the retry button is pressed, the retry function appears and will reset the tab to tab4(). The rule page.
                                                                                     def retry():
                                                                                         Label_leaderboard.destroy()
                                                                                         Label_name1.destroy()
                                                                                         Label_name.destroy()
                                                                                         Label_first1.destroy()
                                                                                         Label_first.destroy()
                                                                                         Label_2nd.destroy()
                                                                                         Label_second.destroy()
                                                                                         Label_3rd.destroy()
                                                                                         Label_third.destroy()
                                                                                         Label_4th.destroy()
                                                                                         Label_fourth.destroy()
                                                                                         Label_5th.destroy()
                                                                                         Label_fifth.destroy()
                                                                                         btn_retry.destroy()
                                                                                         btn_end.destroy()
                                                                                         tab4()
                                                                                     
                                                                                         
                                                                                     
                                                                                     # However if user decides to quit, the text file will be erased of all data and the window will fully close.
                                                                                     def theend():
                                                                                         file = open("amount of point.txt","r+")
                                                                                         file.truncate(0)
                                                                                         file.close()
                                                                                         window.destroy()  
                                                                                 



                                                                                 # The button which leads to retry function              
                                                                                 btn_retry = Button(window,text="retry",command=retry,fg="black",bg="white",width=40,height=5)
                                                                                 btn_retry.place(x=1400,y=800)
                                                                                 
                                                                                 # The button which leads to thend function where everything is erased and destroyed
                                                                                 btn_end = Button(window,text="exit game",command=theend,fg="black",bg="white",width=40,height=5)
                                                                                 btn_end.place(x=1400,y=300)
                                                                                                                                                                     
                                                                                          
                                                                             
                                                                              # The button which leads to leaderboard function                  
                                                                             btn_leaderboard = Button(window,text="next",command=leaderboard,fg="white",bg="black",width=40,height=5)
                                                                             btn_leaderboard.place(x=1400,y=800)
                                                                        
                                                                       
                                                                        
                                                                           # This is a time block, where the page will only be displayed for 15 seconds and then it will go to checkans5() function
                                                                           time7=window.after(15000,check_ans5)
                                                                        
                                                                       
                                                                           # The button which leads to checking of answer for question5 function         
                                                                           btn_checkq5 = Button(window,text="next",command=check_ans5,fg="white",bg="black",width=40,height=5)
                                                                           btn_checkq5.place(x=1400,y=800)
                                                                    
                                                                   
                                                                    
                                                                   
                                                                       # The timer is for 5 seconds before question 5, this is loading screen.
                                                                       window.after(5000,q5)
                                                                   
                                                                       
                                                                   
                                                                    
                                                                   
                                                                   #This button is to follow up to the loading screen before question5
                                                                   btn_nextq5 = Button(window,text="continue",command=loading5,fg="white",bg="black",width=40,height=5)
                                                                   btn_nextq5.place(x=1400,y=800)
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 # This is timer for question 4. after timer is done it will go to check_ans4() function.
                                                                 time6=window.after(15000,check_ans4)
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 #exception raise block for question4
                                                                 def exceptionq4():
                                                                    try:
                                                                        int(answer_q4.get())
                                                                        check_ans4()
                                                                    except ValueError:
                                                                        Label_error4.place(x=300,y=800) 
                                                                 
                                                                    
                                                                 
                                                                    
                                                                 
                                                                 # This is button to go to the exception to check answer in question4
                                                                 btn_checkq4 = Button(window,text="next",command=exceptionq4,fg="white",bg="black",width=40,height=5)
                                                                 btn_checkq4.place(x=1400,y=800)
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             # The timer is for 5 seconds before question 4, this is loading screen.
                                                             window.after(5000,q4)
                                                         
                                                            
                                                         
                                                            
                                                          #This button is to follow up to the loading screen before question4  
                                                         btn_nextq4 = Button(window,text="continue",command=loading4,fg="white",bg="black",width=40,height=5)
                                                         btn_nextq4.place(x=1400,y=800)
                                                         
                                                      
                                                         
                                                      
                                                     # This is timer for question 3. after timer is done it will go to check_ans3() function.    
                                                     time5=window.after(15000,check_q3)
                                                    
                                                    
                                                    
                                                     # This is button to go  to check answer in question3
                                                     btn_next_q3 = Button(window,text="continue",command=check_q3,fg="white",bg="black",width=40,height=5)
                                                     btn_next_q3.place(x=1400,y=800)  
                                                 
                                                   
                                                 
                                                  # The timer is for 5 seconds before question 3, this is loading screen.   
                                                 window.after(5000,q3)
                                             
                                         
                                            
                                             # This is button to go to loading before question3
                                              btn_nextq3 = Button(window,text="continue",command=loading3,fg="white",bg="black",width=40,height=5)
                                              btn_nextq3.place(x=1400,y=800)
                                          
                                            
                                          
                                          # This is timer for question 2. after timer is done it will go to check_ans2() function.  
                                          time4=window.after(15000,check_ans2) 
                                          
                                          
                                          #This is a exception block to check answer 2, if the answer is other than a integere data type an error will be raised. or else it will move forward to the next function
                                          def exceptionq2():
                                              try:
                                                  int(answer_q2.get())
                                                  check_ans2()
                                              except ValueError:
                                                  Label_error.place(x=300,y=800)
                                         
                                                  
                                                  
                                                      
                                                  
                                          #This button is to take the users awnser and go to the exception function to check weather it is integer.                  
                                          btn_checkq2 = Button(window,text="next",command=exceptionq2,fg="white",bg="black",width=40,height=5)
                                          btn_checkq2.place(x=1400,y=800)     
                              
                                    
                        
                                     # The timer is for 5 seconds before question 2, this is loading screen.
                                     window.after(5000,q2)
                              
                               # This is button to go to loading before question2  
                              btn_nextq2 = Button(window,text="next",command=loading1,fg="white",bg="black",width=40,height=5)
                              btn_nextq2.place(x=1400,y=800)
                                      
                                  
                             
                                  
                                  
                                 
                                      
                                      
                                      
                                     
                                      
                                       
                                      
                                      
                                      
                              
                              # This is button to go  to check answer in question1        
                              btn_next2 = Button(window,text="next",command=check1,fg="white",bg="black",width=50,height=5)
                              btn_next2.place(x=1400,y=800)
                            
                            
                              # This is timer for question 1. after timer is done it will go to check1() function.  
                              time3=window.after(15000,check1)    
                          
                         
                         #This is timer for the first loading screen, before question 1
                        window.after(5000,q1)
                      
                    
                      
                      
                      
                     
                
                
                
                
                
                    #This is the start quiz button to start quiz from rule pagee, it leads to the loading screen function
                    start_quiz_btn= Button(window,text="START",bg="black",fg="white",command = loading)
                    start_quiz_btn.config(font=('Comic Sans MS','60'))
                    start_quiz_btn.pack(side= RIGHT, padx =700,pady=50)
                        
                
                
                
                
                
                
                
                
                
              #This button takes a factorial image and acts as a button, when pressed will lead to the factorial_page function(Do note this is from the category page)
              btn_factorial = Button(window, image=new_imagemath,command=factorial_page,bg="black")
              btn_factorial.place(x=100,y=450)

              #This button takes a anime image and acts as a button, when pressed will lead to the tab4 function(Do note this is from the category page)
              btn_math = Button(window, image=new_image2,command=tab4,bg="black")
              btn_math.place(x=800,y=450)
             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
         
    #btn next to go after username for specifically tab 1
    btn_next = Button(window,text="next",command=tab2,fg="white",bg="black",)
    btn_next.config(font=('Comic Sans MS','50'))
    btn_next.pack(side=RIGHT,pady=5)


   



#main menu screen
window.configure(bg="black")
label1 = tk.Label(window,text="KAHOOD!",fg="white",bg="black")
label1.config(font=('Comic Sans MS','200','underline'))
label1.pack()#the following 7 lines of code has been taken from https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
photo = (Image.open("startbutton2.png"))
resized_photo = photo.resize((600,300),Image. ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_photo)
photo2 = (Image.open("exit2.jpg"))
resized_photo1 = photo2.resize((800,300),Image. ANTIALIAS) 
new_image1= ImageTk.PhotoImage(resized_photo1)   
btn = Button(window, image =new_image,command=tab1,bg="black")#When startbutton pressed it will lead to function tab1()
btn.pack(side = LEFT, padx =25,pady=20)
btn2 = Button(window, image=new_image1,command = window.destroy,bg="black")#When exit button pressed(or picture) the whole window will be destroyed
btn2.pack(side = RIGHT, padx =25,pady=20)




    
    
window.mainloop() # The mainloop waits for events from the user and executes the program until the user exits the window.   