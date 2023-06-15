# image_crawling_naver_google

## 1. Google과 Naver
crawling_google폴더에는 여러 사이트 크롤링이 가능하도록 되어있습니다.
google과 Naver의 이미지 크롤링이 가능합니다.

## 2. cawling_naver.py
crawling_google에서 네이버 같은 경우에는 썸네일 이미지는 가져오지만 이미지 클릭 후 높은 화질의 이미지를 가져오지 못합니다.
따로 naver에서 이미지를 크롤링 할수 있는 파일도 남겨두었습니다.

## 크롤링이 안될경우
image URL 같은 경우 google과 naver에서 가끔 바뀌기도 합니다. 크롤링이 안될경우 naver나 google에 들어가서 이미지에 들어가서
아무 이미지에 마우스 오른쪽 클릭을 한 후, 검사를 클릭하여 element가 수정 되었는지 확인해야 합니다.

## 3. 크롤링한 이미지를 이미지 기반 인식 학습을 위해 train과 test로 나눈 후 rename_fold.py를 실행 합니다.
파일명 변경, 폴더 한개 일떄 변경, 폴더가 두개 이상일때 파일명 변경 코드가 있습니다.

## 코드 예제
1) crawling_google 
  python main.py -> 썸네일 이미지를 가져 오기 때문에 화질이 좋지 않음
  python main.py --full -> 높은 화질 이미지 가져오기

  -> download 폴더 아래 google_0001.jpg 또는 naver_0001.jpg 라는 파일 이름으로 저장 됩니다.
\n
2) crawling_naver.py
  python crawling_naver.py
\n
3) rename_fold.py
  python rename_fold.py
