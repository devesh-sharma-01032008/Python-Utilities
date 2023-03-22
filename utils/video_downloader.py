from pytube import YouTube
from threading import Thread

# url : str, quality : str, directory : str, type : str = 'mp4'
def download_video(url : str, quality : str,filename :str, type : str = 'mp4', directory : str='.'):
    youtube_obj = YouTube(url)
    video_title = youtube_obj.title
    file_type = youtube_obj.filter(type)
    youtube_obj.set_filename(filename)
    video = youtube_obj.get(file_type[-1].extension, quality)
    try:
        youtube_obj.register_on_progress_callback(show_status)
        video.download(directory)
    except Exception as e:
        print(e)


# video
def show_status(stream, chunk, bytes_remaining):
    # total_size = 
    print("=",end='')

def main():
    downloader = Thread(target=download_video,args=[])
    # status = Thread(target=show_status,args=[])
    downloader.start()
    # status.start()

main()
