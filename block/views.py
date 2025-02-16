from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse ("""<html>
    <title>Стоматологічна клініка</title>
    <h1>Studio Vita</h1>                     
    </html>""")
