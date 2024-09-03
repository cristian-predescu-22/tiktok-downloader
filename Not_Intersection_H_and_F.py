from Read_User_Remove_Dub import *
from TikTokApi import TikTokApi
import time

api = TikTokApi()

def funcH_F():
    with open('History.txt', 'r') as file1:
        with open('Favorites.txt', 'r') as file2:
            same = set(file1).symmetric_difference(file2)

    same.discard('\n')
    sort_List = []
    
    for x in same:
        a = x
        sort_List.append(a)
    sort_List.sort()

    with open('sorted.txt', 'w') as file_out:
        for line in sort_List:
            file_out.write(line)
