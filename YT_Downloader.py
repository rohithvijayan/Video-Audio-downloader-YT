from pytube import YouTube
from retry import retry
def video_dwnldr():
    while True:
        try:
            url_in=input('ENTER YOUTUBE VIDEO LINK : ')
            url = YouTube(url_in)
            resol = input("Enter Video Resolution : ")
            video = url.streams.get_by_resolution(resolution=resol)
            title=url.title
            video.download()
        except AttributeError:
            print(f'{resol} RESOLUTION NOT FOUND , ENTER DIFFERENT RESOLUTION')
        else:
            break

def audio_dwnldr():
    while True:
        try:
            url_in=input('ENTER YOUTUBE LINK : ')
            url=YouTube(url_in)
            audio=url.streams.get_audio_only(subtype='webm')
            audio.download()
        except:
            print('error')
        else:
            break

# video_dwnldr()
audio_dwnldr()




















