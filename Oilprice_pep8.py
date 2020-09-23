restart = 'continue'
# ฟังชันการคำนวนค่าน้ำมัน


def x1(i):
    print("#" * 120)
    for k in range(6):
        print("#" + (" " * 118) + "#")
    oil = float(
        input("#                              PRICE (BAHT):"))
    for k in range(5):
        print("#" + (" " * 118) + "#")
    print("#" * 120)

    print("#"*120)
    for k in range(6):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + " BAHT = ", ' %.2f ' %
          (oil / i), 'LITER' + (" " * 52) + "#")
    for k in range(5):
        print("#" + (" " * 118) + "#")
    print("#" * 120)


def x2(i):
    print("#" * 120)
    for k in range(6):
        print("#" + (" " * 118) + "#")
    oil = float(
        input("#                              LITER (BATH) : "))
    for k in range(5):
        print("#" + (" " * 118) + "#")
    print("#" * 120)

    print("#" * 120)
    for k in range(6):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + " LITER = ", ' %.2f ' %
          (oil * i), 'BATH' + (" " * 48) + "#")
    for k in range(5):
        print("#" + (" " * 118) + "#")
    print("#" * 120)


# วนลูปการทำงาน
while restart != 'Exit':
# หน้าหลัก

    print("#"*120)
    for k in range(5):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + "HELLO THIS IS GAS STATION" + (" " * 48) + "#")
    for k in range(6):
        print("#" + (" " * 118) + "#")
    print("#"*120)

    re = str(input(">>>Enter  :"))

# รายการน้ำมัน    

    print("#"*120)
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 57) + "list" + (" " * 57) + "#")
    print("#" + (" " * 40) + "1.Gasoline 95  ราคา 29.16 BATH" + (" " * 48) +
          "#")
    print("#" + (" " * 40) + "2.Gasoline 91  ราคา 25.30 BATH" + (" " * 48) +
          "#")
    print("#" + (" " * 40) + "3.Gasohol  91  ราคา 21.68 BATH" + (" " * 48) +
          "#")
    print("#" + (" " * 40) + "4.Gasohol  E20 ราคา 20.2  BATH" + (" " * 48) +
          "#")
    print("#" + (" " * 40) + "5.Gasohol  95  ราคา 21.2  BATH" + (" " * 48) +
          "#")
    print("#" + (" " * 40) + "6.Diesel       ราคา 21.1  BATH" + (" " * 48) +
          "#")
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)

# เลือกรายการลิสต์

    typ = int(input(">>>Choose list : "))

# หน้าลิสต์ให้เลือก

    print("#"*120)
    for k in range(5):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 55) + "Function" + (" " * 55) + "#")
    print("#" + (" " * 47) + "1.Price  ------>   Liter" + (" " * 47) + "#")
    print("#" + (" " * 47) + "2.Liter   ------>  Price" + (" " * 47) + "#")
    for k in range(4):
        print("#" + (" " * 118) + "#")
    print("#"*120)

    fc1 = int(input(">>>Choose function : "))

# ลูปอีฟการคำนวนค่าน้ำมัน

    if typ == 1:
        if fc1 == 1:
            x1(29.16)
        else:
            x2(29.16)
    elif typ == 2:
        if fc1 == 1:
            x1(25.30)
        else:
            x2(25.30)
    elif typ == 3:
        if fc1 == 1:
            x1(21.68)
        else:
            x2(21.68)
    elif typ == 4:
        if fc1 == 1:
            x1(20.2)
        else:
            x2(20.2)
    elif typ == 5:
        if fc1 == 1:
            x1(21.2)
        else:
            x2(21.2)
    else:
        if fc1 == 1:
            x1(21.1)
        else:
            x2(21.1)

# หน้าถามออกหรือจะเริ่มใหม่

    gu = ("#"*120)
    print(gu)
    for k in range(5):
        print("#" + (" " * 118) + "#")
    restart = str(input("#                               Continue or Exit : "))
    for k in range(6):
        print("#" + (" " * 118) + "#")
    print("#"*120)
