#pip install pytube3
from pytube import YouTube

videoURL = 'https://www.youtube.com/watch?v=ceiA-6arhPc'
#print(YouTube(videoURL).streams) aca se ve una lista con todos los formatos del video
video = YouTube(videoURL).streams[1] # aca se elije de la lista el indice 1 que corresponde al video en mp4 720 p
video.download()
