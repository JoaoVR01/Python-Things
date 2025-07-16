import yt_dlp

save = "D:\Videos"

def download_yt(url, formato):
    if formato.lower() == "mp4":
        options = { #used to pass the download parameters    
            #when you don't specify the library downloads the best video qwuality with audio
            'outtmpl': f'{save}/%(title)s.%(ext)s', #where to save the archive
            'ffmpeg_location': 'D:/Videos/ffmpeg-master-latest-win64-gpl-shared/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe'
        }
        
    elif formato.lower() == "mp3":
        options = {
            'format': 'bestaudio/best', #arquive format
            'outtmpl': f'{save}/%(title)s.%(ext)s', #where to save          
        }
        
    else:
        print("inválid format!")
        return
    
    with yt_dlp.YoutubeDL(options) as ydl: #with is used to open and close the object YoutubeDL
        ydl.download([url])
        
link = input("Enter yhe youyube link: ")
format = input("Enter mp4 for vídeo or mp3 for audio: ")
download_yt(link, format)