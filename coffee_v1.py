W = 400
M = 540
Cb = 120
D = 9
Mn = 550

re = 1
while True :
    if re == 1:
        print("The Coffe machine has ")
        print("1.Water 400  Ml")
        print("2.Milk  540  Ml")
        print("3.Coffee Beans 120  G")
        print("4.Disposable 9  pieces")
        print("5.Money 550  BATH")

        ci = str(input(" >>> Press Enter for use :"))

        print("> Choose Funchion  ")
        print("1.Buy  this Coffee")
        print("2.Fill this Coffee")
        print("3.Take this Coffee")


        ch = int(input(" >>> Choose number of one for this list /Buy /Fill /Take :"))

        if ch == 1:

            print("> Menu  ")
            print("1.Espresso")
            print("2.Latte")
            print("3.Cappuccino")

            ch1 = int(input(">>> This menu is number : "))

            if ch1 == 1:

                print("> Pay 4$ for recieve  < ")
                print("> Use water = ",(W - 250), 'Ml')
                print("> Use milk = ",(M), 'Ml')
                print("> Use Coffee beans = ",(Cb - 16), 'G')
                print("> Use Disposable = ",(D - 1), 'Pieces')
                print("> Use money = ",(Mn + 4), 'BATH')

            elif ch1 == 2:

                print("> Pay 7$ for recieve  < ")
                print("> Use water = ",(W - 350), 'Ml')
                print("> Use milk = ",(M - 75), 'Ml')
                print("> Use Coffee beans = ",(Cb - 20), 'G')
                print("> Use Disposable = ",(D - 1), 'Pieces')
                print("> Use money = ",(Mn + 7), 'BATH')

            elif ch1 == 3:

                print("> Pay 6$ for recieve  < ")
                print("> Use water = ",(W - 200), 'Ml')
                print("> Use milk = ",(M - 100), 'Ml')
                print("> Use Coffee beans = ",(Cb - 12), 'G')
                print("> Use Disposable = ",(D - 1), 'Pieces')
                print("> Use money = ",(Mn + 6), 'BATH')

        elif ch == 2:

            Wat = int(input("Fill Water \n : "))
            Mil = int(input("Fill Milk \n: "))
            Cof = int(input("Fill Coffeebeans \n: "))
            Dis = int(input("Fill Disaposable \n: "))

            print("> This is your fill ")
            print("> Water :",(Wat + W ),'Ml')
            print("> Milk :",(Mil + M ),'Ml')
            print("> Coffee Beans :",(Cof + Cb ),'G')
            print("> Disaposable :",(Dis + D),'Pieces')
            print("> Money :",(Mn),'BATH')

        elif ch == 3:

            print("> I gave you $",(Mn))
            print("Use water :",(W),'Ml')
            print("Use milk :",(M),'Ml')
            print("Use coffee beans :",(Cb),'G')
            print("Use disaposable :",(D),'Pieces')
            print("Use money :",(Mn - Mn),'BATH')

    restart = input(str(">>> Continue or Exit : "))
    if "Exit" in restart:
        break
    elif "Continue" in restart:
        re = 1
    else:
        re = 0