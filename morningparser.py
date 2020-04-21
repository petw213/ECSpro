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


site_list_main = ['https://classroom.google.com/c/NTMyNTYxOTkxNjBa','https://classroom.google.com/c/NTYxMDU1OTA3ODNa','https://classroom.google.com/c/NTM2Njg3MjM3MDFa',
'https://classroom.google.com/c/NTU2OTIwNzMzMjZa', 'https://classroom.google.com/c/NjY5MDMyMzc5NjFa','https://classroom.google.com/c/NjY4NTMyOTc1ODla',
'https://classroom.google.com/c/NTgwNDA5OTkwNTha', 'https://classroom.google.com/c/Njc1MzM0ODcwMjda', 'https://classroom.google.com/c/NTc1MDM5MzUwNDla',
]

site_list_select=['https://classroom.google.com/c/NTYxMDEyMzIxNjRa', 'https://classroom.google.com/c/NTQ3Mzk5NTAxNjZa', 'https://classroom.google.com/c/NTE3MDM2MTAxMzRa',
'https://classroom.google.com/c/NTQ3Mzk5NTAwOTFa', 'https://classroom.google.com/c/NTUyOTQ5NjQ5NjBa', 'https://classroom.google.com/c/NTczNjU4NjE0ODFa',
'https://classroom.google.com/c/NTQwNDI0MTU1OTRa', 'https://classroom.google.com/c/NTUyMzk0NjkxNDNa', 'https://classroom.google.com/c/NTUyMzk0NjkxNTVa',
'https://classroom.google.com/c/NTMyNTU2MjQ1ODZa', 'https://classroom.google.com/c/NTUyNjAxODE4MzFa', 'https://classroom.google.com/c/NTUyMzk0NjkxNjVa',
'https://classroom.google.com/c/NjU5OTI3NTI5MTJa', 'https://classroom.google.com/c/Njc2ODA1NjExNzZa', 'https://classroom.google.com/c/NTYwNjI2MjUyNzla',
'https://classroom.google.com/c/NTY5Mzg1NzM2MzBa', 'https://classroom.google.com/c/NTczNzE4MDkwNzVa', 'https://classroom.google.com/c/NTU3MjE3MjQ0Mjla',
'https://classroom.google.com/c/NTY5MTM4NDI3MzNa', 'https://classroom.google.com/c/NTYwNjc0Njc1NjZa', 'https://classroom.google.com/c/NTc1MTAzNTQ5ODFa', 
'https://classroom.google.com/c/NjU5ODY5MDc3NzFa', 'https://classroom.google.com/c/NTUyMzk0NjkxNzda' ]



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
    writeSubject = soup.find('h1',{'class' : 'tNGpbb uTUgB YVvGBb'}).getText()    
    div = soup.findAll('div', {'class' : 'n4xnA'})

    for post in div:
        temp = post.findAll('span',{'class' : 'PazDv'})
        title= temp[0].getText()        
        write_date = temp[1].getText()

        if(("오전" in write_date) or ("오후" in write_date)):
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
                        postUrl = driver.current_url,
                        postSubject = writeSubject
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
                        postUrl = driver.current_url,
                        postSubject = writeSubject
                    ).save()
        else:
            pass
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

        for b in site_list_select:
            time.sleep(2)
            driver.get(b)
            time.sleep(3)
            get_post_info(driver)
        
        for a in site_list_main:
            time.sleep(2)
            driver.get(a)
            time.sleep(3)
            get_post_info(driver)

        

        driver.close()
        driver.quit()
        return True

    except:
        driver.close()
        driver.quit()
        return False
    
get_class_data()