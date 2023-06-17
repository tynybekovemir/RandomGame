import random 

words = ['ветер', 'собака', 'мышь', 'олень', 'кот', 'голем', 'утка', 'рыба', 'корова', 'коза']

secret_word = random.choice(words) 
 
attempts = 3 
 
while attempts > 0: 
    print("Осталось попыток:", attempts) 
     
    guess = input("я загадал ведите слово из списка ветер, собака, мышь, олень, кот, голем, утка, рыба, корова, коза : ") 
     
    if guess == secret_word: 
        print("Вы угадали! Загаданное слово:", secret_word) 
        break 
    else: 
        print("Неправильно.") 
        attempts -= 1 
  
if attempts == 0: 
    print("Вы проиграли. Загаданное слово было:", secret_word)
   
