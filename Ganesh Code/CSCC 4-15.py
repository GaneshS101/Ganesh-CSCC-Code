highway_number = int(input())
G = str(highway_number)
I = 'I-'
a = I + G
import math 
x = math.fmod(highway_number, 100)
if (x == 0):
    print(highway_number, 'is not a valid interstate highway number.')

elif (highway_number>=1 and highway_number <= 99):
    if highway_number == 200:
        print(str(highway_number) + ' is not a valid interstate highway number.')   
    elif highway_number % 2 == 0:
        print("I-" + str(highway_number) + " is primary, going east/west.")
    else:
        print("I-" + str(highway_number) + " is primary, going north/south.")
elif (highway_number>= 100 and highway_number<=999):
    Serving_number = math.fmod(highway_number, 100)
    Serving_number1 = int(Serving_number)
    S = str(Serving_number1)
    if highway_number % 2 == 0:
        print(a, "is auxiliary, serving I-" + S + ", going east/west.")
    else:
        print(a,'is auxiliary, serving I-' + S + ', going north/south.')
