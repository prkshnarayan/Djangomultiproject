from django.urls import path

from musicapp import views



urlpatterns = [
    path('', views.home_fun, name='music_home'),
    path('shreya_goshal/', views.shreya_artist, name='shreya_goshal'),
    path('geetha_madhuri/', views.geetha_artist, name='geetha_madhuri'),
    path('sid_sriram/', views.sid_sri_ram_artist, name='sid_sri_ram'),
    path('sunitha/', views.sunitha_artist, name='sunitha'),
    path('anurag_kulkarni/', views.anurag_kulkarni_artist, name='anurag_kulkarni'),
    path('ramya_behara/', views.ramya_behara_artist, name='ramya_behara'),
    path('devi_sri_prasad/', views.dsp_artist, name='devi_sri_prasad'),
    path('k_s_chitra/', views.k_s_chitra_artist, name='k_s_chitra'),
    path('prakash/', views.prakash, name='prakash'),
    path('logout/', views.logout_fun, name='logout'),
]
