from pygame import init, mixer, event
init()
mixer.music.load('happy.mp3')
mixer.music.play()
event.wait()