import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ECS.settings")
import django
django.setup()
from parsed_data.models import Student
import pdb

def get_url(target):
    urldic = {
        '철학김강(3-7)' : 'https://zoom.us/j/5054701384?pwd=MUdFRzdXTExPRTFEMHNtSkY2OXdWQT09',
        '확률과 통계임상익' : 'https://classroom.google.com/u/0/c/NTU2OTIwNzMzMjZa',
        '독서와 문법박태환' : 'https://band.us/n/a2a037J8I5399',
        '확률과 통계정용호' : 'https://classroom.google.com/u/0/c/NTYxMDU1OTA3ODNa',
        '영미문학 읽기우일성(3-3)' : 'https://meet.google.com/iid-bupx-bxt',
        '독서와 문법김민정' : 'https://classroom.google.com/u/0/c/NTgwNDA5OTkwNTha',
        '운동과 건강고은성' : 'https://classroom.google.com/u/0/c/NTc1MDM5MzUwNDla',
        '국어논술최인혁' : 'https://classroom.google.com/u/0/c/NTc1MDM5MzUwNDla',
        '독서와 문법권영해' : 'https://classroom.google.com/u/0/c/Njc1MzM0ODcwMjda',
        '심화영어독해Ⅰ_나D노은란(3-6)' : 'https://classroom.google.com/c/NjU5ODY5MDc3NzFa',
        '운동과 건강임성규' : 'https://classroom.google.com/c/NTc1MDM5MzUwNDla',
        '운동과 건강/무용2명' : 'https://classroom.google.com/c/NTc1MDM5MzUwNDla',
        '지구과학Ⅱ김지수(3-1)' : 'https://classroom.google.com/c/NTc1MTAzNTQ5ODFa',
        '논리학A김강(3-7)' : '',
        '물리학ⅡA구상우(3-4)' : 'https://classroom.google.com/c/NTUyNzc5NTM4NzJa',
        '심화수학Ⅰ_나D한철호(3-1,5,6)' : 'https://classroom.google.com/c/NjU5ODY5MDc3NzFa',
        '심화영어독해Ⅰ_가C이기영(3-5,6)' : 'https://classroom.google.com/c/NTY5MTM4NDI3MzNa',
        '심화수학Ⅰ_가C정태모(3-1,5,6)' : 'https://classroom.google.com/c/NjU5ODY5MDc3NzFa',
        '심화수학Ⅰ_나A한철호(3-1,5,6)' : 'https://classroom.google.com/c/NjU5ODY5MDc3NzFa',
        '고급물리학구상우(3-4)' : 'https://classroom.google.com/c/NTUyNzc5NTM4NzJa'
    }

    if (str(target) in urldic):
        return str(urldic[target])
    else:
        return 'abc'