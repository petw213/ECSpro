from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pdb
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ECS.settings")
import django
django.setup()
from parsed_data.models import Student

start_arr_num = 10

def get_data(target,id,password):
    targetId = int(id)
    temp_targetName = target.find('font',{'color':'blue'}).getText().split(' ')
    targetName = str(temp_targetName[1])
    targetPassword = password

    tempTimetable = []
    td_list = target.find_all('td')
    for i in range(8):
        all_subject_in_nthClass = td_list[11+ 6*i : 16+ 6*i]
        for subject_in_html in all_subject_in_nthClass:
            tempTimetable.append(subject_in_html.getText().replace('\n',''))
    targetTimetable = '@'.join(tempTimetable)
    targetSubject = '@'.join(list(set(tempTimetable)))
    return [targetId, targetName, targetPassword, targetSubject, targetTimetable]

def parse_site(id, password):
    try: # html 긁어오기
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=options)
        driver.implicitly_wait(3)
        driver.get('http://www.hcuhs.kr')

        # 청운네트워크 접속 및 로그인

        driver.find_element_by_name('radio1').click()
        driver.find_element_by_name('text1').send_keys(id)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath("//input[@value = '로그인']").click()

        # 시간표 접속 밑 html 가져오기

        time.sleep(1)
        driver.get('http://hcuhs.sjedu.net/login_check.php?sel=stu&text1='+id)
        time.sleep(1)
        driver.get('http://hcuhs.sjedu.net/edusel/stu_timetable_view.php')
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')

        # 파싱 데이터 크롤링 정보 뽑아내기
        data_list = get_data(soup,id,password)
        Student(studentId = data_list[0],
        studentName = data_list[1],
        studentPassword = data_list[2],
        studentSubject = data_list[3],
        studentTimetable = data_list[4]
        ).save()
        return True
        

    except:
        print("ERROR")
        return False