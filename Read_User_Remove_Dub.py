import json


Video_Links_List = []
Video_Links_List_Fav = []
Video_Links_List_Like = []

def history_use():

    with open('user_data.json', encoding="utf8") as f:
        data = json.load(f)

        lol = data["Activity"]

        lol_lol = lol["Video Browsing History"]

        lol_lol_lol = lol_lol["VideoList"]

        for x in lol_lol_lol:
            a = x["VideoLink"][36:55]
            Video_Links_List.append(a)
        Video_Links_List.sort()
        

    f.close()


    lines_seen = set()
    output_file_H = open('History.txt', 'w')
    for month in Video_Links_List:
        if month not in lines_seen:
            output_file_H.write(month + '\n')
            lines_seen.add(month)

    output_file_H.close()



def favorites_use():

    with open('user_data.json', encoding="utf8") as f:
        data = json.load(f)

        lol = data["Activity"]

        lol_lol = lol["Favorite Videos"]

        lol_lol_lol = lol_lol["FavoriteVideoList"]

        for x in lol_lol_lol:
            a = x["Link"][36:55]
            Video_Links_List_Fav.append(a)
        Video_Links_List_Fav.sort()
        

    f.close()


    lines_seen = set()
    output_file_F = open('Favorites.txt', 'w')
    for month in Video_Links_List_Fav:
        if month not in lines_seen:
            output_file_F.write(month + '\n')
            lines_seen.add(month)

    output_file_F.close()



def liked_use():

    with open('user_data.json', encoding="utf8") as f:
        data = json.load(f)

        lol = data["Activity"]

        lol_lol = lol["Like List"]

        lol_lol_lol = lol_lol["ItemFavoriteList"]

        for x in lol_lol_lol:
            a = x["VideoLink"][36:55]
            Video_Links_List_Like.append(a)
        Video_Links_List_Like.sort()
        

    f.close()


    lines_seen = set()
    output_file_L = open('Liked.txt', 'w')
    for month in Video_Links_List_Like:
        if month not in lines_seen:
            output_file_L.write(month + '\n')
            lines_seen.add(month)
            

    output_file_L.close()


#history_use()
#favorites_use()
#liked_use()
