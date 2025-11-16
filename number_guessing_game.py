import random

Hidden_number=random.randint(1,50)
attempts=0
a=5
print("welcome to number guessing game 🤖 vs 🧠")
print("i will think a number between 1 to 50 guess the number")

while True :
    
    try:
      guess = int(input('enter your guessing number here: '))
      attempts+=1
      
      if guess>=1 and guess<=50:
         
          if guess < Hidden_number  :
            print("Guessed number is too low then the hiden number 📉")
            print("try it for one more time😊👍")
            print(f"hint:👉👉👉👉👉the number is between  {Hidden_number-a}  and  {Hidden_number+a}  👈👈👈👈👈")
            a-=1
          elif guess > Hidden_number  :
            print("guessed number is too high then the hiden number📈")
            print("try it for one more time😊👍")
            print(f"hint:👉👉👉👉👉the number is between  {Hidden_number-a}  and  {Hidden_number+a}  👈👈👈👈👈")
            a-=1
          else:
            print("________congratulations😁__________")
            print(f" 🎉🎊you guessed a correct number in {attempts}:attemts🎉🎊")
            break
         
      else: 
         print("the number should be between 1 to 50")
    except ValueError as e:
       print(" the value must be an number 😊")
       print(e)
else:
   print("the game is completed 😊")            
         

      
      
              
         
         
