
# computer_vision
간단한 포토샵 만들기

### 현재 사이즈가 너무 커서 MainWindow.resize(1046, 804) 를 사용하여 1046, 804로 실행했을때 딱 화면에 맞을 수 있게 사이즈를 조정했습니다.
### 그에 맞춰서 label의 크기를 통일하여 작게 줄였습니다.
### pixmap을 다시 300,300의 사이즈로 Qt에 있는 함수를 사용하여 비율은 그대로 맞췄습니다.
### pixmap = pixmap.scaled(QSize(300, 300), aspectMode=Qt.KeepAspectRatioByExpanding)
### 메모장은 빈공간이 맘에 안들어 만들어봤습니다. 전체적으로 글씨꼴은 함초롱바탕으로 맞췄고, 도움말 팝업창은 시도는 했으나 아직 완전히 구현못했습니다. 다음 수업때 구현해볼 생각입니다.

사진 저장은 Label에서 표시하고 있는 사진 데이터를 QPixmap객체의 형태로 반환받은 후 변수에 넣어, save함수를 이용해 사진 저장하는 형식으로 받았습니다.

* 사진반전 (Flip_image) *
  ㄴ
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
  
  볼록과 비슷하지만 범위를 바꾸고, 극좌표 또한 변경했습니다.
 
* 흐린 이미지 Blur_image  *
   
  cv2에 있는 medianBlur을 이용하여 블러처리 했습니다.
  
 * HSV 이미지 Hsv_image *
 
  사진을 RGB형태가 아닌 HSV 형태로 받아오기 위해 cv2를 사용했습니다.
  
