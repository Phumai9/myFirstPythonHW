#อิมพอทคำสั่งต่างๆ
import time
import random

#เขียนเล่นให้ดูเท่เฉยๆ กับ ตั้งเวลาก่อนเริ่มเกม
name = input("What is your name sir ? : ")
print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
print("Hello: " + name," Time to play Hangman Games!!!")
time.sleep(1)
print("Start this games...")
time.sleep(1)
print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')

#ตัวเเปรสุ่มคำสั่ง
word_1 = ['python','java','kotlin','javascript']
word = random.choice(word_1)

#เขียนเล่นให้ดูเท่เฉยๆ
print("let's get started !")
print("The word has :", len(word), "letters")

#ปริ้นช่องว่าง
question = "_" * len(word)
print(question)

#ดัมมี้
right_word = ['_'] * len(word)
wrong_word = []
lives = 8

#ฟังชั้นเติมคำถูก
def add_letter():
    for i in right_word:
        print(i, ' ', end="")
    print()

#ฟังชั้นบอกคำผิด
def wrong_letter():
    print("Wrong letters : ", end="")
    for i in wrong_word:
        print(i, ' ', end="")
    print()

# Main Loop ที่เเท้ทรู
while True:
    print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
    answer = input(">>> Input a letter : ")
    print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')

#ตรวจคำถูก
    if answer in word:
        print("checking...")
        time.sleep(0.5)
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
        index = 0
        for i in word:
            if i == answer:
                right_word[index] = answer
            index = index + 1

        add_letter()
        print("Result your lives has :", lives)
        wrong_letter()

#ตรวจคำผิดกับคำซ้ำ
    elif answer not in word:
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
        print("checking...")
        time.sleep(0.5)
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')

        if answer in wrong_word:
            print("No improvements :", answer)
            wrong_letter()
            print("Result your lives has :",lives)
        else:
            print(answer," : No such letter in the word ")
            lives -= 1
            wrong_word.append(answer)
            add_letter()
            print("Result your lives has :",lives)
            wrong_letter()

#เเพ้ถ้าคำผิดเยอะเกินไป
   # if len(wrong_word) > 10:
        #print("Game is Over!")
        #print("this answer is : ", word)
        #print("Result your lives has :", lives)
        #break

#ชนะ
    if '_' not in right_word:
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
        print(">>> You guessed the word ! <<<")
        print("The word is :", word ,"☆")
        print("Result your lives has :", lives)
        print(">>> You survived :",name," !!! <<<")
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
        break

#เเพ้
    if lives == 0:
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
        print(">>> You are hanged ! <<<")
        print("Your lives has",lives, "×")
        print(">>> Try again :",name," !!! <<<")
        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
        break

