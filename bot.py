from datetime import datetime
now=datetime.now()
d=now.strftime("%d:%m:%y")

t=now.strftime("%H:%M:%S")

qna={ 
       "Hii":"Hey User!",
       "What is your name":"I am a Python chatbot 😊!",
       "What do you like to eat":"I dont like to eat as I am a chatbot!",
       "What thing you like the most":"I like to answer as I am a chatbot!",
       "Whats the date of today":d,
       "Whats the time currently":t,
       "When were you born":"I was made by Dev Gaurav Joshi on 05/03/23"
       
    }
while (q:=input("Enter the question:"))!="quit":
    print(qna[q])
       
       