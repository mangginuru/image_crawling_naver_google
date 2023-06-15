from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from urllib.request import urlopen
import os
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def Driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.add_argument("headless")
    options.add_argument('--start-fullscreen')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(options = options)
    return wd

## url
def make_url(word):
    base_url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
    return base_url + word

# 해당하는 폴더가 없을 경우 생성해주는 함수
def makedirs(path): 
   try: 
        if not os.path.exists(path):
            os.makedirs(path) 
   except OSError: 
       if not os.path.isdir(path): 
           raise

# 찾을 목록이 담긴 dictionary
search_dict = ["peperomia indoor plant"]

def save_images(image_url, paths, file_name, i):
    import base64
        
    if 'data:' in str(image_url):
        pass
    else:
        t= urlopen(image_url).read()
        file = open(os.path.join(paths, file_name+'_'+str(i)+".jpg"), 'wb')
        file.write(t)

def naver_crawl(image_numbers):
    wd = Driver()
    wd.implicitly_wait(3)
    for plant in search_dict:
        # 음식에 해당하는 검색어를 입력한 페이지 출력
        wd.get(make_url(plant))
        time.sleep(2)
        for i in range(1,image_numbers+1):
            time.sleep(2)
            # i에 해당하는 이미지가 없을 경우 PASS
            try:
                # image url 추출
                images= wd.find_elements(By.XPATH, '//*[@id="main_pack"]/section[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/img')
                save_path = os.path.dirname(os.path.abspath(os.getcwd()))
                makedirs(save_path)
                src = images[0].get_attribute('src')
                save_images(str(src), save_path, f'{plant}_', i)
                
                # 이미지가 10개가 넘어갈때 마다 PAGE_DOWN
                if i % 10 == 0:
                    body = wd.find_element(By.XPATH,'//body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(3)
            except:
                print(f"No element in {i}")
                continue
    wd.close()
    print("End_crawling")

print(os.path.dirname(os.path.abspath(os.getcwd())))
naver_crawl(300)