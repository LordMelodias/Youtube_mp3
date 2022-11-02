import youtube_dl
def run():   
    video_url = input("Enter youtube video url: ")     

    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False   
    )
    filename = f"{video_info['title']}.mp3"    
    options={            
        'format':'bestaudio/best',
        'keepvideo':False,   
        'outtmpl':filename,  
    }

    with youtube_dl.YoutubeDL(options) as ydl:   
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))   


run()   # to run the function