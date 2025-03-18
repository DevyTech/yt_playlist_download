from yt_dlp import YoutubeDL
import os

if __name__ == '__main__':
    video_url = input("Please insert the URL: ")
    video_info = YoutubeDL().extract_info(url=video_url, download=False)

    # Tentukan folder keluaran
    output_folder = r"C:\Users\SMK NEGERI 2 MANADO\Videos\Web Design"

    # Pastikan folder keluaran ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    options = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best[ext=mp4]/best', # Modifikasi format untuk resolusi 1080p
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }

    with YoutubeDL(options) as ydl:
        out = ydl.download([video_info['webpage_url']])

    print("Download completed!")