from Read_User_Remove_Dub import *
from Not_Intersection_All_Three import *
from Not_Intersection_H_and_F import *
from Not_Intersection_H_and_L import *
from Not_Intersection_F_and_L import *
from Program import *


from TikTokApi import TikTokApi
import time

api = TikTokApi()

H = 0
F = 0
L = 0

while True:
    
    print("")
    print("")
    print("What data would you like to extract form user file?")
    print("You select more then 1 and it will return all videos and no dublicates")
    print("")
    print("Please select one of the options: or press 0 to end")
    print("1. History")
    print("2. Favorites")
    print("3. Liked")
    print("")

    user_input = input("Enter selection number: ")

    if user_input == "1":
        H = H+1
        history_use()
    elif user_input == "2":
        F = F+1
        favorites_use()
    elif user_input == "3":
        L = L+1
        liked_use()
    elif user_input == "0":
        break


while True:
    print(H)
    print(F)
    print(L)
    
    if H>0 and F>0 and L>0:
        funcAll()
        break
    elif H>0 and F>0:
        funcH_F()
        break
    elif H>0 and L>0:
        funcH_L()
        break
    elif F>0 and L>0:
        funcF_L()
        break
    else:
        break

    
    
download_Video()
