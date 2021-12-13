import os


class Sp3:

    def convert(self):

        format = input("what format do you want the final video to be?\n "
                     "[VP8, VP9, h.265, AV1]\n"
                     "please enter format: ")
        files = ["160x120.mp4", "360x240.mp4", "640x480.mp4", "1280x720.mp4"]
        if format == "VP8":
            for file in files:
                command = 'ffmpeg -i '+ file +' -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis VP8/'+ file[:-4]+'.webm'
                os.system(command)
        if format == "VP9":
            for file in files:
                command = 'ffmpeg -i '+ file +' -c:v libvpx-vp9 -crf 10 -b:v 1M -c:a libvorbis -b:a 64k -f webm VP9/'+ file[:-4]+'_VP9.webm'
                os.system(command)
        if format == "h.265":
            for file in files:
                command = 'ffmpeg -i '+ file +' -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k H265/'+ file[:-4]+'_H265.webm'
                os.system(command)
        if format == "AV1":
            for file in files:
                command = 'ffmpeg -i '+ file +' -c:v libaom-av1 -crf 30 -b:v 0 AV1/'+ file[:-4]+'_AV1.webm'
                os.system(command)
        print("conversion successful")

    def comparison(self):
        os.system("ffmpeg -i VP8/360x240.webm -i VP9/360x240_VP9.webm -filter_complex hstack VP8_VP9_compare.mp4")
        print("that")
    '''
    to be honest, I can't really tell a difference...
    '''
    def livestream(self):
        pass

sp3 = Sp3()
#Sp3.convert(sp3)
Sp3.comparison(sp3)
Sp3.livestream(sp3)
