import os

class Sp3:
    def convert(self):
        size = input("what format do you want the final video to be?\n "
                     "[1280x720, 640×480, 360x240, 160x120]\n"
                     "please enter widthxheight: ")

        command = 'ffmpeg -i BBB.mp4 -s ' + size + ' -c:a copy ' + str(size) + '.mp4'
        os.system(command)
        print("resize successful")

    convert()
