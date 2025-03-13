from yt_dlp import YoutubeDL

if __name__=='__main__':
    video_url = input("Please insert the URL : ")
    video_info = YoutubeDL().extract_info(url=video_url, download=False)
    options = {
        'format' : 'bestaudio/best',
        'keepvideo': False,
        'outtmpl' : '%(title)s.mp3',
    }
    with YoutubeDL(options) as ydl:
        out = ydl.download([video_info['webpage_url']])