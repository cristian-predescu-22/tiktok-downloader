from TikTokApi import TikTokApi
import time
api = TikTokApi()


def download_Video():
    f = open("sorted.txt", "r")
    temp = f.read().splitlines()
    counter = 1

    for line in temp:
        a = str(line)

        start = time.process_time()

        try:
            video_bytes = api.video(id=a).bytes()
        except:
            continue


        counter += 1

            
        with open('saved'+str(counter)+'_video.mp4', 'wb') as output:
            output.write(video_bytes)   
            

            output.close()
        print(time.process_time() - start)
        

    f.close()


