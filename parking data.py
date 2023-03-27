### PARKING DATA



from datetime import datetime

dict_car=list(map(lambda x:"A" + str(x), range(1, 21)))
dict_motor = list(map(lambda x:"B" + str(x), range(1, 21)))
dict_vip = list(map(lambda x:"V" + str(x), range(1, 11)))
dict_staff = list(map(lambda x: "S" + str(x) , range(1, 16)))
id_list = list(range(1200, 1240))

dict_OWNER={}


def print_data(Inout, PLATE):
    list1 = dict_OWNER[PLATE]
    print("_"*30)
    print("♛  Car parKing  ♛".center(30))
    print("Chitkara University".center(30))
    print()
    print("Parking ID:".rjust(12), list1[7])
    print("Name:".rjust(12), list1[0])
    print("Mobile:".rjust(12), list1[1])
    print("Place:".rjust(12), list1[3])
    print("Plate:".rjust(12), PLATE)
    print("Date:".rjust(15), list1[4])
    print("Time:".rjust(15), list1[5])
    print("_"*30)


def CHECK_IN(kind):
    global dict_OWNER
    match kind:
        case "C":
            if len(dict_car) == 0:
                print("Parking is full for cars.")
                return None
            PLACE = dict_car.pop(0)
        case "B":
            if len(dict_motor) == 0:
                print("Parking is full for bikes.")
                return None
            PLACE = dict_motor.pop(0)
        case "V":
            if len(dict_vip) == 0:
                print("VIP parking is full.")
                return None
            PLACE = dict_vip.pop(0)
        case "S":
            if len(dict_staff) == 0:
                print("Parking for staff is full.")
                return None
            PLACE = dict_staff.pop(0)
    NAME = str(input("NAME: "))
    MOBILE = int(input("MOBILE NUMBER: "))
    PLATE = str(input("VEHICLE NUMBER: "))
    PAID = str(input("PARKING FEE PAID: "))
    KIND = kind
    DATE = str(datetime.now().date())
    TIME = str(datetime.now().hour) + ":" + str(datetime.now().minute)
    print("Date :", DATE)
    print("Time :", TIME)
    id_user = id_list.pop(0)
    list1 = [NAME, MOBILE, PAID, PLACE, DATE, TIME, KIND, id_user]   
    dict_OWNER[PLATE] = list1
    print_data("Checkin", PLATE)

    

def CHECK_OUT():
    global dict_OWNER
    PLATE = str(input("VEHICLE NUMBER:"))
    if PLATE not in dict_OWNER.keys():
        print("No such entry found.")
    else:
        print_data("Checkout", PLATE)
        list1 = dict_OWNER[PLATE]
        match list1[6]:
            case "C":
                dict_car.append(list1[4])
            case "B":
                dict_motor.append(list1[4])
            case "V":
                dict_vip.append(list1[4])
            case "S":
                dict_staff.append(list1[4])


while True:
    print("\nEnter I for check in, O for check out and P to print database.")
    what = input()
    if what == "I":
        while True:
            print("TYPE : C for Car, B for bike, V for VIP and S for staff")
            kind = input("Enter vehicle type: ")
            if kind not in {"C", "B", "V", "S"}:
                print("Invalid response!")
                continue
            else:
                break
        CHECK_IN(kind)
    elif what == "O":
        CHECK_OUT()
    elif what == "P":
        print("|{:^12}|{:^12}|{:^12}|{:^15}|{:^12}|{:^12}|{:^12}|{:^12}|".format("Parking ID", "Name", "Mobile No.", "Vehicle No.", "Place", "kind", "Date", "Time"))
        for i in dict_OWNER.keys():
            list1 = dict_OWNER[i]
            print("|{:^12}|{:^12}|{:^12}|{:^15}|{:^12}|{:^12}|{:^12}|{:^12}|".format(list1[7], list1[0], list1[1], i, list1[3], list1[6], list1[4], list1[5]))


    elif what == "exit":
        exit()
    else:
        print("Invalid response!")

