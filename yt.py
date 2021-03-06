from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
caption = yt.captions.get_by_language_code('en')
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()
print(caption.generate_srt_captions())
f = open(str("captions.txt"), "w")
f.write(caption.generate_srt_captions())
f.close()


#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")