from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re
import pdb
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ECS.settings")
import django
django.setup()
from post.models import Post

site_list = ['https://classroom.google.com/u/0/c/NTc1MDM5MzUwNDla','https://classroom.google.com/u/0/c/Njc1MzM0ODcwMjda',
'https://classroom.google.com/u/0/c/NTY5MTM4NDI3MzNa', 'https://classroom.google.com/u/0/c/NTYwNjc0Njc1NjZa',
'https://classroom.google.com/u/0/c/NjU5ODY5MDc3NzFa', 'https://classroom.google.com/u/0/c/NTgwNDA5OTkwNTha',
'https://classroom.google.com/u/0/c/NjY4NTMyOTc1ODla', 'https://classroom.google.com/u/0/c/NTUyMzk0NjkxNzda',
'https://classroom.google.com/u/0/c/NTU2OTIwNzMzMjZa', 'https://classroom.google.com/u/0/c/NTM2Njg3MjM3MDFa',
'https://classroom.google.com/u/0/c/NTYxMDU1OTA3ODNa', 'https://classroom.google.com/u/0/c/NTMyNTYxOTkxNjBa',
'https://classroom.google.com/u/0/c/NTc1MTAzNTQ5ODFa', 'https://classroom.google.com/u/0/c/NTU3MjE3MjQ0Mjla',
'https://classroom.google.com/u/0/c/Njc2ODA1NjExNzZa', 'https://classroom.google.com/u/0/c/NjU5OTI3NTI5MTJa',
'https://classroom.google.com/u/0/c/NTczNzE4MDkwNzVa', 'https://classroom.google.com/u/0/c/NTYwNjI2MjUyNzla',
'https://classroom.google.com/u/0/c/NTY5Mzg1NzM2MzBa',
]


def get_post_info(driver):
    #SCROLL_PAUSE_TIME = 1
    #
    # # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.findAll('div', {'class' : 'n4xnA'})
    for post in div:
        temp = post.findAll('span',{'class' : 'PazDv'})
        title= temp[0].getText()        
        write_date = temp[1].getText()
        write_date = ''.join(re.findall("\d+",write_date))

        if(len(write_date) == 2):
            write_date = write_date[0]+ '0' + write_date[1]
        else:
            write_date = ''.join(write_date)
        try:
            writer = post.find('span',{'class' : 'YVvGBb asQXV'}).getText()
            content = post.find('div',{'class' : 'pco8Kc obylVb'}).getText("\n")
            
            if(Post.objects.filter(postDate = write_date, postContent = content)):
                return
            else:
                Post(
                    postWriter = writer,
                    postTitle = title,
                    postDate = write_date,
                    postContent = content,
                    postUrl = driver.current_url
                ).save()
        except:
            content = post.find('div', {'class' : 'JZicYb QRiHXd'}).getText("\n")
            if(Post.objects.filter(postDate = write_date, postContent = content)):
                return
            else:
                Post(
                    postWriter = writer,
                    postTitle = title,
                    postDate = write_date,
                    postContent = content,
                    postUrl = driver.current_url
                ).save()
    return

def get_class_data(): 
    Post.objects.all().delete()
    try:
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        

        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=options)
        driver.implicitly_wait(3)
        driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        driver.find_element_by_xpath("//input[@id = 'Email']").send_keys('1920308@hcu.hs.kr')
        driver.find_element_by_xpath("//input[@id = 'next']").click()

        driver.find_element_by_xpath("//input[@id='password']").send_keys('mood2301')
        driver.find_element_by_xpath("//input[@id = 'submit']").click()

        for a in site_list:
            time.sleep(5)
            driver.get(a)
            time.sleep(5)
            get_post_info(driver)

        driver.close()
        driver.quit()
        return True

    except:
        driver.close()
        driver.quit()
        return False
    
get_class_data()
