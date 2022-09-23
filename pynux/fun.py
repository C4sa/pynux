from re import A
import time
import vlc

aaa_player = vlc.MediaPlayer('root/lib/aaa.mp3')

def aaa():
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    aaa_player.play()
    time.sleep(1)
    aaa_player.stop()