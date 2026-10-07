from tkinter import *#packages are  imported
from PIL import Image, ImageTk
#import mysql.connector
import sqlite3
#import tkMessageBox
#import tkFileDialog
import tkinter.filedialog
from tkinter import messagebox
import numpy as nm  

def main():
    window = Tk()
    window.geometry('900x600')
    window.title("Hotel Fake Reviews")
    #adding image to gui
    '''
    image = Image.open('hotel2.jpg')
    image = image.resize((900, 600))
    photo_image = ImageTk.PhotoImage(image)
    label = Label(window, image = photo_image)
    label.place(x=0,y=0)
    '''  
    #creating labels
    lbl = Label(window, text="Detection of Fake Online Review",font=('algerian',25,'bold'),fg="black",bg="violet")
    lbl.place(x=0, y=50)
    lbl = Label(window, text="REGISTER HERE",font=('algerian',25,'bold'),fg="black",bg="violet")
    lbl.place(x=100, y=120)

    btn = Button(window, text="REGISTER", width=8, height=2,fg="black",font=('algerian',20,'bold'),bg="violet",justify='center',command=register)
    btn.place(x=400, y=180)

    btn1 = Button(window, text="LOGIN", width=8, height=2,fg="black",font=('algerian',20,'bold'),bg="violet",justify='center',command=login)
    btn1.place(x=400, y=340)
    
    window.mainloop()
def register():
    
    def registerinto():
        usernames = username.get()
        passwords = password.get()
        emails = email.get()
        phonenos = phoneno.get()
        conn = sqlite3.connect('bbc.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS patient (Username TEXT,Password TEXT,Email TEXT,Phoneno TEXT)')
        cursor.execute('INSERT INTO patient (Username,Password ,Email,Phoneno) VALUES(?,?,?,?)',
                  (usernames,passwords,emails,phonenos,))
        conn.commit()
        if username.get() == "" or password.get() == "":
           messagebox.showinfo("sorry", "Pease fill the required information")
        else:
           messagebox.showinfo("Welcome to %s" % usernames, "Let Login")
           login()
        

        #reg()
    global R1
    R1 = Toplevel()

    R1.geometry('900x600')
    R1.title('REGISTER NOW')
    '''
    image = Image.open('3db.jpg')
    image = image.resize((900, 600))
    photo_image = ImageTk.PhotoImage(image)
    label = Label(R1, image = photo_image)
    label.place(x=0,y=0)
    '''
    lbl = Label(R1, text="Dtection of Fake Online Review",font=('algerian',25,'bold'),fg="black",bg="violet")
    lbl.place(x=100, y=50)

    lbl = Label(R1, text="FIRST REGESTER NOW",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lbl.place(x=80, y=120)

    lb2 = Label(R1, text="USERNAME", font=("bold", 11))
    lb2.place(x=150, y=170)
    username = Entry(R1, width=20, font=("bold", 15), highlightthickness=2, bg="white", relief=SUNKEN)
    username.place(x=272, y=170)

    lb3 = Label(R1, text="PASSWORD", font=("bold", 11))
    lb3.place(x=150, y=230)
    password = Entry(R1, width=20,show="**", font=("bold", 15), highlightthickness=2, bg="white", relief=SUNKEN)
    password.place(x=272, y=230)

    lb4 = Label(R1, text="EMAIL", font=("bold", 11))
    lb4.place(x=150, y=270)
    email = Entry(R1, width=20, font=("bold", 15), highlightthickness=2, bg="white", relief=SUNKEN)
    email.place(x=272, y=270)

    lb3 = Label(R1, text="PHONENUMBER", font=("bold", 11))
    lb3.place(x=150, y=330)
    phoneno = Entry(R1, width=20, font=("bold", 15), highlightthickness=2, bg="white", relief=SUNKEN)
    phoneno.place(x=300, y=330)

    btn = Button(R1, text="REGISTER", width=8, height=2,fg="black",font=('algerian',20,'bold'),bg="violet",justify='center',command=registerinto)
    btn.place(x=300, y=470)
     
    R1.mainloop()
        

        #reg()
    #global R1

    #registerinto()

    #creating login page   

def login():
    def loginto():
        #aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="breast")
        #mm = aa.cursor()
        usernames = e1.get()
        passwords = e2.get()
        conn = sqlite3.connect('bbc.db')
        with conn:
          cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS patient (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        conn.commit()
        if usernames == "" and passwords == "" :
            messagebox.showinfo("sorry", "Please complete the required field")
        else:
            cursor.execute('SELECT * FROM patient WHERE Username = "%s" and Password = "%s"'%(usernames,passwords))
            for i in usernames:
                if cursor.fetchall():
                    messagebox.showinfo("Welcome %s" % usernames, "Logged in successfully")
                    pred()
                
                else:
                    messagebox.showinfo("Sorry", "Wrong Password")


    #global window1        
    window1 = Toplevel()
    window1.geometry('900x600')
    window1.title("LOGIN NOW")
    '''
    image = Image.open('2db.jpg')
    image = image.resize((900, 600))
    photo_image = ImageTk.PhotoImage(image)
    label = Label(window1, image = photo_image)
    label.place(x=0,y=0)
    '''
    lbl = Label(window1, text=" Detection of Fake Online Review",font=('algerian',25,'bold'),fg="black",bg="violet")
    lbl.place(x=150, y=50)

    lb2 = Label(window1, text="USERNAME",font=('algerian',25,'bold'),fg="BLACK",anchor='w')
    lb2.place(x=150, y=200)

    lb3 = Label(window1, text="PASSWORD",font=('algerian',25,'bold'),fg="BLACK",anchor='w')
    lb3.place(x=150, y=270)

    e1= Entry(window1,width=15,font=("bold",14),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=380, y=200)

    e2= Entry(window1,width=15,font=("bold",14),show="*",highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=380, y=270)

    btn = Button(window1, text="LOGIN", width=8, height=2,fg="black",font=('algerian',20,'bold'),bg="SKYBLUE",justify='center',command=loginto)
    btn.place(x=350, y=350)

    window1.mainloop()
def pred():
    def b():
        fb=E.get()
        if (fb==""):
            messagebox.showinfo("sorry", "Please complete the required field")
        else:
            
            result = text_clf.predict([fb])
            print(result)
            message.configure(text= acc)
            message1.configure(text=result)

            
    R4 =Toplevel()
    R4.geometry('900x600')
    R4.title("Review Prediction")

    lbl = Label(R4, text="Detection of Fake Online Review",font=('algerian',25,'bold'),fg="black",bg="violet")
    lbl.place(x=100, y=100)
    lblIn=Label(R4,text="FeedBack",fg="black",font=("bold",15))
    lblIn.place(x=200,y=200)
    E=StringVar()
    e1=Entry(R4,width=20,textvariable=E,font=("bold",15),highlightthickness=2)
    e1.place(x=360,y= 200 )

    lblIn=Label(R4,text="Accuracy",fg="black",font=("bold",15))
    lblIn.place(x=150,y=420)

    lblIn=Label(R4,text="Status",fg="black",font=("bold",15))
    lblIn.place(x=480,y=420)
    
    message =Label(R4, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message.place(x=100, y=480)
    
    message1 =Label(R4, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message1.place(x=400, y=480)

    bt = Button(R4,text = "Get",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=b)
    bt.place(x =300 ,y=350)
    bt = Button(R4,text = "<--",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=main)
    bt.place(x =0 ,y=0)
    #message1.configure(text= res)
    R4.mainloop()
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split #split data into train and test sets
from sklearn.feature_extraction.text import CountVectorizer #convert text comment into a numeric vector
from sklearn.feature_extraction.text import TfidfTransformer #use TF IDF transformer to change text vector created by count vectorizer
#With Tfidftransformer you will compute word counts using CountVectorizer and then compute the IDF values and only then compute the Tf-idf scores.
#With Tfidfvectorizer you will do all three steps at once.
from sklearn.svm import SVC# Support Vector Machine
from sklearn.pipeline import Pipeline #pipeline to implement steps in series
#from gensim import parsing # To stem data
#Gensim is an open-source library for unsupervised topic modeling and natural language processing, using modern statistical machine learning.
#from joblib import dump, load #save or load model
#from pdftotext import convert_pdf_to_string #converts pdf_to_string
from sklearn.metrics import accuracy_score  #accuracy
import pickle
#Read the dataset
df = pd.read_csv("dataset.csv", encoding='latin1')

#Split the dataset in x and y
#X, y = df['word'], df['taxonomy']
X, y = df['text'], df['deceptive']   

#Split data in train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


#Use pipeline to carry out steps in sequence with a single object
#SVM's rbf kernel gives highest accuracy in this classification problem.
from sklearn.svm import SVC# Support Vector Machine
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SVC(kernel='rbf'))])

#Train the model
text_clf.fit(X_train, y_train)
'''
#print(X_test)
predicted = text_clf.predict(X_test)
acc=accuracy_score(y_test, predicted)
print('Accuracy:',acc)
'''
y_pred= text_clf.predict(X_test)  
x_pred= text_clf.predict(X_train)
#Y_pred=y_pred.astype(int)
print("Printing Y_prediction","\n",y_pred)
print('Train Score: ', text_clf.score(X_train, y_train))  
print('Test Score: ', text_clf.score(X_test, y_test))
#Creating the Confusion matrix  
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as mtp  
cm= confusion_matrix(y_test, y_pred)
print("Printing Confusion matrix","\n",cm)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test, y_pred)
print("Printing Accuracy","\n",acc)
X_train=nm.arange(0,len(y_train),1)
y_train=nm.arange(0,len(y_train),1)
X_test=nm.arange(0,len(y_train),1)
y_test=nm.arange(0,len(y_train),1)

mtp.scatter(X_train, y_train, color="green")   
mtp.plot(X_train, x_pred, color="red")    
mtp.title("feedback vs status (Training Dataset)")  
mtp.xlabel("feedback")

mtp.ylabel("Status")  
mtp.show()

#visualizing the Test set results  
mtp.scatter(X_test, y_test, color="blue")   
mtp.plot(X_train, x_pred, color="red")    
mtp.title("feedback vs status (Test Dataset)")  
mtp.xlabel("feedback")  
mtp.ylabel("Status")  
mtp.show()

main()

