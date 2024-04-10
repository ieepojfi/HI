#create the Easy Editor photo editor here!
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import *
from PyQt5.QtGui import *
from PIL import *

def saveimg():
    savedir = QFileDialog.getExistingDirectory()
    #########IMPORTANT TO FILL OUT LATER###############

class image_processor():
    def __init__(self):
        self.filename = ''
        self.image = ''
    def loadImage(self, filenameo):
        self.image = filenameo
        self.filename = filenameo
    def showImage(self,path):
        lb_image.hide()
        lb_image.setFixedSize(500 , 500)
        pixmapimage = QPixmap(path)
        w,h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()




    def bw(self):
        self.image.convert('L')
    def sharpen(self):
        epifohi=0
    def mirrorr(self):
        efiohi=0
    def leftt(self):
        lb_image.transpose(Image.ROTATE_90)
    def rightt(self):
        epfoji=0

        
workdir = ''
result = list()

def chooseWorkdir():
    global workdir
    workdir =  QFileDialog.getExistingDirectory() #(HWAT TGIS DO?!?)
    showfilenameslist()
def filter(files,extensions):
    global result
 
    result = list()
    for name in files:
        if name.endswith(extensions):
            result.append(name)
    for a in result:
        lw_files.addItem(a) 
   
            
            
            
def dhowchosenimaage():
    if lw_files.currentRow() >= 0:
        
        filename = lw_files.currentItem().text()
        workimage.loadImage(filename)
        image_path = path.join(workdir, workimage.filename)
        workimage.showImage(image_path)

def showfilenameslist():
    filenames = listdir(workdir)
    filter(filenames, ('.png', '.jpg'))


workimage = image_processor()
app = QApplication([])
main_win=QWidget()
main_win.resize(400 ,300)
main_win.setWindowTitle('EASY EDITOR')

blackwhitepush = QPushButton('B/W')
sharpnesspush = QPushButton('Sharpness')
mirrorpush = QPushButton('Mirror')
leftpush = QPushButton('Left')
rightpush = QPushButton('Right')
folder = QPushButton('Folder')
lw_files = QListWidget()
lb_image = QLabel('Image')


#folderslist.resize(10,10) #WHY NO WORK ;( )


H = QHBoxLayout()
H2 = QHBoxLayout()
V = QVBoxLayout()
HMAIN = QHBoxLayout()
V2 = QVBoxLayout()
#LIST+LABEL
V2.addWidget(folder , alignment = Qt.AlignTop)
V.addWidget(lb_image , alignment=Qt.AlignCenter)
H.addWidget(leftpush , alignment = Qt.AlignBottom)
H.addWidget(rightpush, alignment = Qt.AlignBottom)
H.addWidget(mirrorpush, alignment = Qt.AlignBottom)
H.addWidget(sharpnesspush, alignment = Qt.AlignBottom)
H.addWidget(blackwhitepush, alignment = Qt.AlignBottom)
V2.addWidget(lw_files)
folder.clicked.connect(chooseWorkdir) 
lw_files.clicked.connect(dhowchosenimaage)

blackwhitepush.clicked.connect(image_processor.bw) 
sharpnesspush.clicked.connect(image_processor.sharpen) 
mirrorpush.clicked.connect(image_processor.mirrorr) 
rightpush.clicked.connect(image_processor.rightt) 
leftpush.clicked.connect(image_processor.leftt) 
V.addLayout(H)
HMAIN.addLayout(V2)

HMAIN.addLayout(V)

main_win.setLayout(HMAIN)
main_win.show()

app.exec_()


