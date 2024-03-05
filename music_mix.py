from pytube import YouTube
from pytube import Search
import sys
import moviepy.editor as mp
import numpy as np
import os
def Download(singer,number,duration,output):
    if not os.path.exists(singer):
        os.makedirs(singer)
    query=singer + ' music videos'
    s = Search(query)
    
  

    i=0
    
    # for i in range(0,number):
    for v in s.results:
     if i < number and v.length < 600:
        
        try:
            youtubeObject = YouTube(v.watch_url)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download(singer,filename=f"{i}.mp4")
            print(f"Download of video {i} completed")
            i=i+1
        except:
            print("An error has occurred")
            
        

    for k in range(0, number):
        try:
            clip = mp.VideoFileClip(f"{singer}/{k}.mp4").subclip(0, duration)
            clip.audio.write_audiofile(f"{singer}/{k}.mp3")
        except:
            print("Too less videos")
            sys.exit(0)

    audio_clips = [mp.AudioFileClip(f"{singer}/{j}.mp3") for j in range(0, number)]
    final_clip = mp.concatenate_audioclips(audio_clips)
    final_clip.write_audiofile(output)

    

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python prog.py <singer> <number_of_videos> <audioduration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    try:
     number_of_videos =int(sys.argv[2])

    except:
        sys.stdout.write("Number of videos must be integer")
        sys.exit(0)
    
    
    
    if(number_of_videos<10):
        print("Number of videos must be greater 10")
        sys.exit(0)
    
    duration=sys.argv[3]
    try:
     duration=int(sys.argv[3])

    except:
        sys.stdout.write("Duration must be integer")
        sys.exit(0)
    
    if(duration<20):
        print("Duration must be greater than 20")
        sys.exit(0)
    
    output=sys.argv[4]
    Download(singer, number_of_videos,duration,output)
