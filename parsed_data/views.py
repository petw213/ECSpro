from django.shortcuts import render
import os
import sys
import pdb
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import html_parser
from parsed_data.models import Student
from post.models import Post
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from gethref import get_url
from django.contrib import messages

# Create your views here.
def main_view(request, *args, **kwargs):
    return render(request, "main.htm", {})

def sub_view(request, *args, **kwargs):
    id = request.POST.get('id')
    password= request.POST.get('password')
    
    try:
        Student.objects.get(studentId = id,studentPassword = password)
        target = Student.objects.get(studentId = id,studentPassword = password)
        post = Post.objects.all().order_by('-postDate')
        dt = datetime.now()
        weekday = dt.weekday()
        
        if( weekday > 4):
                weekday = 4
        
        my_context = {
            'Id' : id,
            'Name' : target.studentName,
            'firstPeriod' : target.studentTimetable.split('@')[0:5][weekday],
            'firsturl' : get_url(target.studentTimetable.split('@')[0:5][weekday]),

            'secondPeriod' : target.studentTimetable.split('@')[5:10][weekday],
            'secondurl' : get_url(target.studentTimetable.split('@')[5:10][weekday]),

            'thirdPeriod' : target.studentTimetable.split('@')[10:15][weekday],
            'thirdurl' : get_url(target.studentTimetable.split('@')[10:15][weekday]),

            'fourthPeriod' : target.studentTimetable.split('@')[15:20][weekday],
            'fourthurl' : get_url(target.studentTimetable.split('@')[15:20][weekday]),

            'fifthPeriod' : target.studentTimetable.split('@')[20:25][weekday],
            'fifthurl' : get_url(target.studentTimetable.split('@')[20:25][weekday]),

            'sixthPeriod' : target.studentTimetable.split('@')[25:30][weekday],
            'sixthurl' : get_url(target.studentTimetable.split('@')[25:30][weekday]),

            'seventhPeriod' : target.studentTimetable.split('@')[30:35][weekday],
            'seventhurl' : get_url(target.studentTimetable.split('@')[30:35][weekday]),
            
            'eighthPeriod' : target.studentTimetable.split('@')[35:][weekday],
            'eighthurl' : get_url(target.studentTimetable.split('@')[35:][weekday]),
            
            'subject' : target.studentSubject.split('@')[1:][weekday],
            'posts' : post,
        }
        return render(request, "sub2.html", my_context) ## already exist

    except ObjectDoesNotExist: ## does not exist
        if(html_parser.parse_site(id, password)): ## make db
            target = Student.objects.get(studentId = id,studentPassword = password)
            post = Post.objects.all().order_by('-postDate')
            dt = datetime.now()
            weekday = dt.weekday()
            
            if( weekday > 4):
                weekday = 3

            my_context = {
                'Id' : id,
                'Name' : target.studentName,
                'firstPeriod' : target.studentTimetable.split('@')[0:5][weekday],
                'secondPeriod' : target.studentTimetable.split('@')[5:10][weekday],
                'thirdPeriod' : target.studentTimetable.split('@')[10:15][weekday],
                'fourthPeriod' : target.studentTimetable.split('@')[15:20][weekday],
                'fifthPeriod' : target.studentTimetable.split('@')[20:25][weekday],
                'sixthPeriod' : target.studentTimetable.split('@')[25:30][weekday],
                'seventhPeriod' : target.studentTimetable.split('@')[30:35][weekday],
                'eighthPeriod' : target.studentTimetable.split('@')[35:][weekday],
                'subject' : target.studentSubject.split('@')[1:][weekday],
                'posts' : post,
            }
            return render(request, "sub2.html",my_context)
        else:
            messages.info(request, '로그인에 실패했습니다')
            return main_view(request)
