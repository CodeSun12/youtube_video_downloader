from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=DiJzNNewpXA&list=RDDiJzNNewpXA&start_radio=1")

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
