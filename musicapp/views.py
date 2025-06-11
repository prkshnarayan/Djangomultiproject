from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from musicapp.models import Song


@login_required
# Create your views here.
def home_fun(request):
    return render(request, 'music.html')


@login_required
def shreya_artist(request):
    return render(request, 'shreya_goshal.html')


@login_required
def geetha_artist(request):
    return render(request, 'geethamadhuri.html')


@login_required
def sid_sri_ram_artist(request):
    return render(request, 'sid_sriram.html')


@login_required
def sunitha_artist(request):
    return render(request, 'sunitha.html')


@login_required
def anurag_kulkarni_artist(request):
    return render(request, 'anurag_kulkarni.html')


@login_required
def ramya_behara_artist(request):
    return render(request, 'ramya_behara.html')


@login_required
def dsp_artist(request):
    return render(request, 'dsp.html')


@login_required
def k_s_chitra_artist(request):
    return render(request, 'ks_chitra.html')


def logout_fun(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")


def prakash(request):
    songs = Song.objects.all()
    return render(request,  'prakash.html', {"songs": songs})
