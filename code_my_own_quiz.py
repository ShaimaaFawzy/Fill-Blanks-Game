#Code my own quiz

#Define the levels as questions and answers

#Easy Level 
easy_question="My name start with ___1___ . my name end with ___2___ . my best anime ___3___ . my fav color ___4___ "

easy_answer=["s","a","hunter","red"]

#Medium Level 
medium_question="the meaning of load out loud ___1___ , the meaning of never mind ___2___ ,take your time ___3___ , no problem ___4___ "
medium_answer=["lool","nvm","tyt","np"]

#Hard Level
hard_uestion= "best anime cahracter  ___1___ ,fav indian film ___2___ , fav english film ___3___ , fav anime ___4___ "
hard_answer=["gon","pk","xmen","hunter"]


#lists
blanks = ["___1___", "___2___", "___3___", "___4___"]
game_levels=["1","2","3"]

    

#Choose the level of the game by writing one of the levels type 
def game_level():
    print ("Welcome to the Guess Quiz\r\nIn this game you have to guess the meaning of the sentences") #Welcome start 
    username = input("Please enter your name : \r\n")# Take the username
    print ( username + " Are You read let's start\r\nPlease choose the level type 'Easy = 1','Medium = 2' ,'Hard =3'\r\n")   
    level_input= input() # Take the level input
    while level_input not in game_levels: #check if the input level in the game levels or not 
          level_input= input("You have choosed wrong level , Choose again 'Easy = 1','Medium = 2' ,'Hard =3'\r\n")# if the input level not in the game level list        
    else :# if the input level in the game level list c
        """Return the question and the answer of the level
           print the question of the level"""
        if level_input=="1":
           print (easy_question)
           return easy_question,easy_answer
        if level_input=="2":
           print (medium_question)
           return medium_question,medium_answer
        if level_input=="3":
           print (hard_question)
           return hard_question,hard_answer
    

def answer_checker():
    question_counter = 0 #counter to count 4 question
    fail = 0 #number of fail
    answers = 4 #number of answers 
    question_ph, answer_list= game_level() #take an object from game level function 
    while question_counter < answers : #loop on the question 
          user_input = input("The meaning of "+ blanks[question_counter] +"?\r\n") #enter the answer 
          if user_input == answer_list[question_counter]: #check if the answer is in answer list 
             question_ph =question_ph.replace(blanks[question_counter],user_input) #replace the answer with the blank area 
             print (question_ph)
             question_counter += 1
             print("Correct :D")
          else:
             fail += 1
             print("The answer isn't right :( try again")  


def fill_blanks(user_input,question_ph ,question_number):
    replaced=[] #new list 
    for answer in question_ph: #check if the answer in the question list 
        if answer == blanks[question_number] : 
             replaced.append(user_input)
    return replaced

def main():
    user_input,question_list, question_number =answer_checker()
    fill_blanks(user_input,question_list , question_number)

print (main()) 
