from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FB
import ftplib
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})
	
def crm(request):
    return render(request, 'blog/crm.html', {})  
	
def crm_insert(request): 
    a =  FB(email = request.POST['email_fb'], text = request.POST['text_fb'])
    a.save()
    return HttpResponseRedirect(reverse('post_list'))

def download(request): 
    #return HttpResponse('Hello my friend')
    ftp = ftplib.FTP()
    HOST = 'localhost'
    PORT = 21
    ftp.connect(HOST, PORT)
    out = (r"C:\Users\sveta\Desktop\ы\ы\setup.exe")
    try:
        with open(out, 'wb') as f:
            ftp.retrbinary('RETR ' + 'setup.exe', f.write)
    except ftplib.error_perm:
        pass
    return HttpResponseRedirect(reverse('post_list'))