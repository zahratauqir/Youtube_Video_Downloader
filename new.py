from pytube import YouTube
link = "https://youtu.be/0U9-KUx0SD8"
youtube_1 = YouTube(link)

# For printing the title of the youtube video
# print(youtube_1.title)

# for getting the thumbnail of the youtube video
# print(youtube_1.thumbnail_url)


# for downloading the video
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter the quality you need to download from the list: "))
videos[strm].download()
print("Successful")


# Playlist downloading extension
# from pytube import Playlist
# py = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9aiS4rUVp2jXwIvCruo27sG6")
# print(f'Downloading:  {py.title}')
# for video in py.videos:
#     video.streams.first().download();
