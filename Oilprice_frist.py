# ฟังชันคำนวนค่าน้ำมัน

def x1(i):
    oil = float(input("จำนวนเงิน (บาท) : "))
    print('จำนวนเงิน ', oil, ' บาท เท่ากับ ', '%.2f' % (oil / i), ' ลิตร')


def x2(i):
    oil = float(input("จำนวนลิตร (บาท) : "))
    print('จำนวน ', oil, ' ลิตร เท่ากับ ', '%.2f' % (oil * i), ' บาท')


restart = 'continue'

# ประเภทน้ำมัน

while restart != 'Exit':

    oiltyp = 0
    print(" ---ประเภทน้ำมันและราคา--- ")
    print("1.Gasoline  95       ราคา 29.16 BATH")
    print("2.Gasoline  91       ราคา 25.30 BATH")
    print("3.Gasohol  91        ราคา 21.68 BATH")
    print("4.Gasohol  E20      ราคา 20.2   BATH")
    print("5.Gasohol  95        ราคา 21.2   BATH")
    print("6.Diesel                ราคา 21.1   BATH")
    typ = int(input(">>>เลือกชนิดของน้ำมัน : "))

    print(" ---ฟังก์ชั่นการทำงาน--- ")
    print("1คำนวนจากเงินเป็นลิตร")
    print("2คำนวนจากลิตรเป็นเงิน")
    fc1 = int(input(">>>เลือกฟังชั่นการทำงาน : "))

    # วนลูปการทำงาน

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

    restart = str(input("Continue or Exit : "))