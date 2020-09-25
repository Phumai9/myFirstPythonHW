# The Coffe machine has

# Variable
W = 400
M = 540
Cb = 120
D = 9
Mn = 550

re = 1
while True :
    if re == 1:       
        print("#"*120)
        for k in range(3):
            print("#" + (" " * 118) + "#")
        print("#" + (" " * 50) + "> The Coffe machine has " + (" " * 44) + "#")
        print("#" + (" " * 118) + "#")
        print("#" + (" " * 48) + "1.Water 400  Ml" + (" " * 55) + "#")
        print("#" + (" " * 48) + "2.Milk  540  Ml" + (" " * 55) + "#")
        print("#" + (" " * 48) + "3.Coffee Beans 120  G" + (" " * 49) + "#")
        print("#" + (" " * 48) + "4.Disposable 9  pieces" + (" " * 48) + "#")
        print("#" + (" " * 48) + "5.Money 550  BATH" + (" " * 53) + "#")
        for k in range(3):
            print("#" + (" " * 118) + "#")
        print("#"*120)

        ci = str(input(" >>> Press Enter for use :"))

        #ฟังชันในการเลือกฟังชันการคิด

        print("#"*120)
        for k in range(4):
            print("#" + (" " * 118) + "#")
        print("#" + (" " * 47) + " > Choose Funchion  " + (" " * 51) + "#")
        print("#" + (" " * 118) + "#")
        print("#" + (" " * 48) + "1.Buy  this Coffee" + (" " * 52) + "#")
        print("#" + (" " * 48) + "2.Fill this Coffee" + (" " * 52) + "#")
        print("#" + (" " * 48) + "3.Take this Coffee" + (" " * 52) + "#")
        for k in range(4):
            print("#" + (" " * 118) + "#")
        print("#"*120)

        ch = int(input(" >>> Choose number of one for this list /Buy /Fill /Take :"))

        if ch == 1:
            #ฟังชันเมนูเอาไว้เลือกกาเเฟที่ต้องการ

            print("#"*120)
            for k in range(4):
                print("#" + (" " * 118) + "#")
            print("#" + (" " * 47) + " > Menu  " + (" " * 62) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 48) + "1.Espresso" + (" " * 60) + "#")
            print("#" + (" " * 48) + "2.Latte" + (" " * 63) + "#")
            print("#" + (" " * 48) + "3.Cappuccino" + (" " * 58) + "#")
            for k in range(4):
                print("#" + (" " * 118) + "#")
            print("#"*120)

            ch1 = int(input(">>> This menu is number : "))

            if ch1 == 1:
            #คิดคำนวน Buy Espresso

                print("#"*120)
                for k in range(3):
                    print("#" + (" " * 118) + "#")
                print("#" + (" " * 50) + (" > Pay 4$ for recieve  < ") + (" " * 43) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 48) + " > Use water = ",(W - 250), 'Ml' + (" " * 48) + "#")
                print("#" + (" " * 48) + " > Use milk = ",(M), 'Ml' + (" " * 49) + "#")
                print("#" + (" " * 48) + " > Use Coffee beans = ",(Cb - 16), 'G' + (" " * 42) + "#")
                print("#" + (" " * 48) + " > Use Disposable = ",(D - 1), 'Pieces' + (" " * 41) + "#")
                print("#" + (" " * 48) + " > Use money = ",(Mn + 4), 'BATH' + (" " * 46) + "#")
                print("#" + (" " * 118) + "#")
                for k in range(2):
                    print("#" + (" " * 118) + "#")
                print("#"*120)

            elif ch1 == 2:
#คิดคำนวน Buy Latte

                print("#"*120)
                for k in range(3):
                    print("#" + (" " * 118) + "#")
                print("#" + (" " * 50) + " > Pay 7$ for recieve  < " + (" " * 43) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 48) + " > Use water = ",(W - 350), 'Ml' + (" " * 49) + "#")
                print("#" + (" " * 48) + " > Use milk = ",(M - 75), 'Ml' + (" " * 49) + "#")
                print("#" + (" " * 48) + " > Use Coffee beans = ",(Cb - 20), 'G' + (" " * 42) + "#")
                print("#" + (" " * 48) + " > Use Disposable = ",(D - 1), 'Pieces' + (" " * 41) + "#")
                print("#" + (" " * 48) + " > Use money = ",(Mn + 7), 'BATH' + (" " * 46) + "#")
                print("#" + (" " * 118) + "#")
                for k in range(2):
                    print("#" + (" " * 118) + "#")
                print("#"*120)

            elif ch1 == 3:
#คิดคำนวน Buy Cappuccino

                print("#"*120)
                for k in range(2):
                    print("#" + (" " * 118) + "#")
                print("#" + (" " * 50) + " > Pay 6$ for recieve  < " + (" " * 43) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 48) + " > Use water = ",(W - 200), 'Ml' + (" " * 48) + "#")
                print("#" + (" " * 48) + " > Use milk = ",(M - 100), 'Ml' + (" " * 49) + "#")
                print("#" + (" " * 48) + " > Use Coffee beans = ",(Cb - 12), 'G' + (" " * 42) + "#")
                print("#" + (" " * 48) + " > Use Disposable = ",(D - 1), 'Pieces' + (" " * 41) + "#")
                print("#" + (" " * 48) + " > Use money = ",(Mn + 6), 'BATH' + (" " * 46) + "#")
                print("#" + (" " * 118) + "#")
                for k in range(3):
                    print("#" + (" " * 118) + "#")
                print("#"*120)

        elif ch == 2:
# คิดคำนวน Fill 

            Wat = int(input("Fill Water \n : ")) 
            Mil = int(input("Fill Milk \n: "))
            Cof = int(input("Fill Coffeebeans \n: "))
            Dis = int(input("Fill Disaposable \n: "))


            print("#"*120)
            for k in range(3):
                print("#" + (" " * 118) + "#")
            print("#" + (" " * 57) + " > This is your fill ",(" " * 39) + "#")
            print("#" + (" " * 57) + "> Water :",(Wat + W ),'Ml' + (" " * 44) + "#")
            print("#" + (" " * 57) + "> Milk :",(Mil + M ),'Ml' + (" " * 45) + "#")
            print("#" + (" " * 57) + "> Coffee Beans :",(Cof + Cb ),'G' + (" " * 39) + "#")
            print("#" + (" " * 57) + "> Disaposable :",(Dis + D),'Pieces' + (" " * 36) + "#")
            print("#" + (" " * 57) + "> Money :",(Mn),'BATH' + (" " * 43) + "#")
            for k in range(4):
                print("#" + (" " * 118) + "#")
            print("#"*120)

        elif ch == 3:
#คิดคำนวน Take

            print("#"*120)
            for k in range(3):
                print("#" + (" " * 118) + "#")
            print("#" + (" " * 57) + " > I gave you $",(Mn),(" " * 41) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 57 ) + "Use water :",(W),'Ml' + (" " * 42) + " # ")
            print("#" + (" " * 57 ) + "Use milk :",(M),'Ml' + (" " * 43) + " # ")
            print("#" + (" " * 57 ) + "Use coffee beans :",(Cb),'G'+ (" " * 36) + " # ")
            print("#" + (" " * 57 ) + "Use disaposable :",(D),'Pieces'+ (" " * 34) + " # ")
            print("#" + (" " * 57 ) + "Use money :",(Mn - Mn),'BATH' + (" " * 42) + " # ")
            for k in range(4):
                print("#" + (" " * 118) + "#")
            print("#"*120)


    restart = input(str(">>> Continue or Exit : "))
    if "Exit" in restart:
        break
    elif "Continue" in restart:
        re = 1
    else:
        re = 0