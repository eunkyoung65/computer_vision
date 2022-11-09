
# computer_vision
간단한 포토샵 만들기

기본적으로 UI에서 사이즈를 맞춰주었기때문에 데려오는 사진의 사이즈도 맞췄습니다.
pixmap을 다시 300,300의 사이즈로 Qt에 있는 함수를 사용하여 비율은 그대로 맞췄습니다.
pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)

* 사진반전 (Flip_image) *
  
  cv2를 사용하여 사진을 반전하여 보여줍니다.
  
* 색상 반전 (pain_image) *
  
  cv2에 있는 COLOR_BGR2GRAY 를 사용하여 색을 반전 시켜주었습니다.
  
*  사진 가져오기 show_file_dialog *
  
  자신의 폴더에 있는 사진을 self.image에 넣어서 가져옵니다.

* 두번째 사진 가져오기 second_image *
  
  자신의 폴더에 있는 사진을 가져오며 self.image2에 넣어줍니다.
  Plus_image라는 사진 두장을 합치는 기능을 위해 만들어놓았습니다.
  
* 사진 합치기 Plus_image *
  
  self.image 와 self.image2를 합치는 기능으로 사이즈를 조절한 뒤 alpha를 이용하여 사진을 조정해준 뒤 합쳐 주었습니다.
  
* 모자이크 만들기 Mozaic_image *

  사진을 축소 하고 다시 그 사진을 사진을 사이즈를 지정해주지 않고 다시 조정해주는 식으로 하여 만들었습니다.
  
* 볼록 이미지 Polar_image  *

  exp와 scale 을 이용하여 사진의  극좌표를 변경 했습니다.
  
* 오목 이미지 scale_image *
  반복
 
* 흐린 이미지 Blur_image  *
   
  cv2에 있는 medianBlur을 이용하여 블러처리 했습니다.
  
