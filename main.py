from logging.handlers import RotatingFileHandler
import sys
from tkinter import Image, Scale
import cv2
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
    QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
    )
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5 import uic
from windowff import Ui_MainWindow
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    #부목 클래스가 이미 show함수 만들어 놓음
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Load_botton.clicked.connect(self.show_file_dialog)
        self.Save_button.clicked.connect(self.saveimage)
        
        #Radio 버튼
        self.flipButton.clicked.connect(self.flip_image)
        self.mozaicButton.clicked.connect(self.mozaic_image)
        self.polarButton.clicked.connect(self.polar_image)
        self.scaleButton.clicked.connect(self.scale_image)
        self.blurButton.clicked.connect(self.blurimage)
        self.paintButton.clicked.connect(self.paint_image)
        self.hsvButton.clicked.connect(self.hsv_image)
        self.plusButton.clicked.connect(self.plus_img)
        
        #메뉴바 기능
        self.plus_images.setShortcut("Ctrl+A")
        self.plus_images.triggered.connect(self.second_image)
        
        self.out_action.triggered.connect(self.clear_label)

        
        #밑은 기존에 만들어놨었던 버튼 틀입니다. UI를 입힐거라서 주석처리 해놨습니다.
        """
        self.setWindowTitle("아주아주 간단한 포토샵")

        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("파일") # 버튼 하나
        exit = QAction("나가기", self, triggered=app.quit)
        self.menu_file.addAction(exit)   
        second = QAction("합칠 이미지 불러오기", self, triggered=self.second_image)
        self.menu_file.addAction(second)     
        
        self.menu_file = self.menu.addMenu("기능")    
        paint = QAction("색 반전", self, triggered=self.paint_image)
        self.menu_file.addAction(paint)   
        Flip = QAction("반전 이미지", self, triggered=self.flip_image)
        self.menu_file.addAction(Flip)
        plus = QAction("사진 합치기", self, triggered=self.plus_image)
        self.menu_file.addAction(plus)    
        mozaic = QAction("모자이크", self, triggered=self.mozaic_image)
        self.menu_file.addAction(mozaic) 
        polar = QAction("볼록렌즈 효과", self, triggered=self.polar_image)
        self.menu_file.addAction(polar)
        Scale = QAction("오목렌즈 효과", self, triggered=self.scale_image)
        self.menu_file.addAction(Scale)
        blure = QAction("이미지 흐림처리", self, triggered=self.blurimage)
        self.menu_file.addAction(blure)
        Save = QAction("사진 저장하기", self, triggered = self.saveimage)
        self.menu_file.addAction(Save)
        Hsv = QAction("HSV 사진", self, triggered = self.hsv_image)
        self.menu_file.addAction(Hsv)
        
        
        #메인화면 레이아웃            
        main_layout = QHBoxLayout()
        
        #사이드바 메뉴 버튼
        sidebar = QVBoxLayout()
        button1 = QPushButton("이미지 열기")
        button3 = QPushButton("새로고침") #버튼을 생성
        button1.clicked.connect(self.show_file_dialog)
        button3.clicked.connect(self.clear_label)
        sidebar.addWidget(button1) #ALT+Shift 방향키 아래
        sidebar.addWidget(button3)


        
        main_layout.addLayout(sidebar)
        
        self.label1 = QLabel(self) #스스로 지정
        self.label1.setFixedSize(640, 480) # 사이즈 지정
        main_layout.addWidget(self.label1)
        
        
        self.label2 = QLabel(self) #스스로 지정
        self.label2.setFixedSize(640, 480) # 사이즈 지정
        main_layout.addWidget(self.label2)
        
        
        self.label3 = QLabel(self) #스스로 지정
        self.label3.setFixedSize(640, 480) # 사이즈 지정
        main_layout.addWidget(self.label3)
        
        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        """
     

    def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./") #file name = 경로
        print(file_name)
        self.image = cv2.imread(file_name[0]) # 기존 이미지
        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image = QImage(self.image.data, w, h, bytes_per_line, QImage.Format_RGB888 ).rgbSwapped()
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label.setPixmap(pixmap)
        
        
             
    def second_image(self):
        file_name = QFileDialog.getOpenFileName(self, "합칠 이미지 열기", "./") #file name = 경로
        print(file_name)
        self.image2 = cv2.imread(file_name[0]) # 불러올 이미지는 이미지 2로 지정.
        h, w, _ = self.image2.shape
        bytes_per_line = 3 * w
        image2 = QImage(self.image2.data, w, h, bytes_per_line, QImage.Format_RGB888 ).rgbSwapped()
        pixmap = QPixmap(image2)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
        
    def flip_image(self):
        image = cv2.flip(self.image, 1)
        h,w,_ = image.shape
        bytes_per_line = 3 * w 
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
        
    def paint_image(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB) 
        h,w = image.shape[:2] #흑백은 2개를 받음
        bytes_per_line = 3 * w 
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
        
    def plus_img(self):
        image1 = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(self.image2, cv2.COLOR_BGR2RGB)
        h, w, _= image1.shape[:3]
        bytes_per_line = 3 * w 
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
        alpha = 0.5
        plus_image= image1 * alpha + image2 * (1-alpha)
        plus_image = plus_image.astype(np.uint8)
        plus_image = QImage(
            plus_image.data, w, h, bytes_per_line, QImage.Format_BGR888).rgbSwapped()
        pixmap = QPixmap(plus_image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_5.setPixmap(pixmap)
        
    def mozaic_image(self):
        ratio = 0.1 #모자이크 정도
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB) 
        h, w, _= image.shape[:3] #사진크기 지정
        bytes_per_line = 3 * w 
        small = cv2.resize(image, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST) #사이즈를 축소 후 사이즈 지정X
        mozaic_image = cv2.resize(small, image.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
        mozaic_image = QImage(
            mozaic_image.data, w, h, bytes_per_line, QImage.Format_BGR888).rgbSwapped() # 데이터를 mozaic_image에 넣어줌
        pixmap = QPixmap(mozaic_image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
    
    def polar_image(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        h, w = image.shape[:2]
         
        exp = 2 #볼록 지수
        scale = 1 #오목 지수
        mapy, mapx = np.indices((h,w), dtype = np.float32)
        bytes_per_line = 3 * w 
        mapx = 2 * mapx / (w-1)-1
        mapy = 2 * mapy / (h-1)-1 
        
        r, theta = cv2.cartToPolar(mapx,mapy)
        r[r < scale] = r[r < scale] ** exp
        
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1) * w -1)/2
        mapy = ((mapy + 1) * h -1)/2
        
        distorted_image = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
        distorted_image = QImage(
            distorted_image.data, w, h, bytes_per_line, QImage.Format_BGR888).rgbSwapped()
        pixmap = QPixmap(distorted_image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
        
    def scale_image(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        h, w = image.shape[:2]
         
        exp = 0.7 
        scale = 1 
        mapy, mapx = np.indices((h,w), dtype = np.float32)
        bytes_per_line = 3 * w 
        mapx = 2 * mapx / (h-1)-1
        mapy = 2 * mapy / (w-1)-1 
        
        r, theta = cv2.cartToPolar(mapx,mapy)
        r[r < scale] = r[r < scale] ** exp
                
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1) * h -1)/2
        mapy = ((mapy + 1) * w -1)/2
        
        distorted_image = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
        distorted_image = QImage(
            distorted_image.data, h, w, bytes_per_line, QImage.Format_BGR888).rgbSwapped()
        pixmap = QPixmap(distorted_image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
    
    def blurimage(self):
        image = self.image[..., :: -1]
        h, w, _= image.shape[:3] #사진크기 지정
        bytes_per_line = 3 * w 
        blure = cv2.medianBlur(image, 5 )
        blured_image = QImage(
            blure.data, h, w, bytes_per_line, QImage.Format_BGR888).rgbSwapped()
        pixmap = QPixmap(blured_image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
    
    def hsv_image(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)
        h, w, _= image.shape[:3] #사진크기 지정
        bytes_per_line = 3 * w 
        hsv_image = QImage(
            image.data, h, w, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(hsv_image)
        pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
        self.label_3.setPixmap(pixmap)
        
        
    def saveimage(self) :
        #Label에서 표시하고 있는 사진 데이터를 QPixmap객체의 형태로 반환받은 후, save함수를 이용해 사진 저장
        self.qPixmapSaveVar = self.label.pixmap()
        self.qPixmapSaveVar.save("SavedImage.jpg")
        
    def clear_label(self):
        self.label.clear()
        self.label_3.clear()
        self.label_5.clear()
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())