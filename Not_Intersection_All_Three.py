from Read_User_Remove_Dub import *
from TikTokApi import TikTokApi
import time

api = TikTokApi()

def funcAll():
    with open('History.txt', 'r') as file1:
        with open('Favorites.txt', 'r') as file2:
            with open('Liked.txt', 'r') as file3:
                same_old = set(file1).symmetric_difference(file2)
                same = set(same_old).symmetric_difference(file3)
                
    
    same.discard('\n')
    sort_List = []
    
    for x in same:
        a = x
        sort_List.append(a)
    sort_List.sort(reverse=True)
    
    with open('sorted.txt', 'w') as file_out:
        for line in sort_List:
            file_out.write(line)
            
