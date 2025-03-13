from yt_dlp import YoutubeDL
import os

if __name__ == '__main__':
    video_url = input("Please insert the URL: ")
    video_info = YoutubeDL().extract_info(url=video_url, download=False)

    # Tentukan folder keluaran
    output_folder = r"C:\Users\SMK NEGERI 2 MANADO\Music\Avenged Sevenfold LBC"

    # Pastikan folder keluaran ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': os.path.join(output_folder, '%(title)s.mp3'),  # Modifikasi path output
    }

    with YoutubeDL(options) as ydl:
        out = ydl.download([video_info['webpage_url']])

    print("Download completed!")