import time
import  datetime
import random

def counter():
    tsecs = 180
    while True:
        if tsecs == 0:
            print("00:00")
            print("\nTIME OUT")
            break
        else:
            min = tsecs//60
            sec = tsecs%60    
            timer = '{:02d}:{:02d}'.format(min, sec)
            print(timer, end = "\r")
            tsecs-=1

            

l = ["abruptly","avenue","awkward","beekeeper","bookworm","boxcar","boxful","buffalo","buffoon","crypt","cycle","duplex","dwarves","equip","faking","fishhook","fixable",
         "fjord","flapjack","flopping","fluffiness","flyby","foxglove","frizzled","funny","gabby","galaxy","galvanize","gossip","grogginess","haiku",
          "hyphen","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jockey",
            "jogging","joking","jovial","joyful","juicy","jukebox","jumbo","keyhole","khaki","kilobyte","kiwifruit","larynx","lengths","lucky","luxury",
           "lymph","matrix","megahertz","microwave","mystify","nightclub","nowadays","nymph","oxidize","oxygen","pajama","peekaboo",
         "pixel","pneumonia","psyche","puppy","puzzling","quartz","queue","quiz","quizzes","rhythm","rickshaw","scratch","squawk",
          "staff","strength","strengths","stretch","stronghold","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript",
        "transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","walkway",
       "waltz","wave","wavy","waxy","whiskey","whomever","witchcraft","wizard","wristwatch","xylophone","yachtsman","yippee","youthful",
       "yummy","zigzag","zipper","zodiac","zombie"]

alpha = []

tcount = 100
count = 0
realword = random.choice(l)
secretword = len(realword)*["_ "]
foundword = "".join(secretword)
print(foundword)

currentime = datetime.datetime.now()
min = 5
sec = 0
timer = "{:02d}:{:02d}".format(min,sec)

while True:
    letter = input("Enter the letter: ")
    if letter in alpha:
        print(f"Already tried the letter {letter}")                   
    elif tcount == count or tcount-count==0:
        print("You lost. GAME OVER")
        break        
    elif letter not in realword:
        alpha.append(letter)
        count+=1
        print("\n","Try again. You have got only",tcount-count,"chances left")
        print(foundword.count("_"),"letters to go")
        print("".join(secretword))
    else:
        alpha.append(letter)
        for i, p in enumerate(realword):
            if letter == p:
                count+=1
                secretword[i] = letter
                foundword = "".join(secretword)
                print(foundword,"\n")
        if foundword == realword:
            print(f"Congratulations !! \nYou have {tcount-count} chances left.\nYou have used {count} chances")
            break
   
# time
