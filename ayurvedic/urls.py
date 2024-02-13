

from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('signup',views.signup,name='signup'),
    path('doctorsregister',views.doctorsregister,name='doctorsregister'),
    path('patientregister',views.patientregister,name='patientregister'),
    path('staffregister',views.staffregister,name='staffregister'),
    path('dctrg', views.dctrg, name='dctrg'),
    path('patreg',views.patreg,name='patreg'),
    path('staffreg',views.staffreg,name='staffreg'),
    path('login2',views.login2,name='login2'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('doctorshome',views.doctorshome,name='doctorshome'),
    path('staffhome',views.staffhome,name='staffhome'),
    path('patienthome',views.patienthome,name='patienthome'),
    path('patienthome',views.patienthome,name='patienthome'),
    path('Verifydoctors',views.Verifydoctors,name='Verifydoctors'),
    path('viewpatients',views.viewpatients,name='viewpatients'),
    path('viewdoctorshedule',views.viewdoctorshedule,name='viewdoctorshedule'),
    path('book',views.book,name='book'),
    path('viewbookingstatus',views.viewbookingstatus,name='viewbookingstatus'),
    path('addmedicine',views.addmedicine,name='addmedicine'),
    path('addshedule',views.addshedule,name='addshedule'),
    path('blockunblock',views.blockunblock,name='blockunblock'),
    path('managemedicine',views.managemedicine,name='managemedicine'),
    path('manageshedule',views.manageshedule,name='manageshedule'),
    path('sendcomplaints',views.sendcomplaints,name='sendcomplaints'),
    path('sendreply',views.sendreply,name='sendreply'),
    path('verifybookingdetails',views.verifybookingdetails,name='verifybookingdetails'),
    path('viewcomplaints',views.viewcomplaints,name='viewcomplaints'),
    path('viewcomplaintsreply',views.viewcomplaintsreply,name='viewcomplaintsreply'),
    path('viewdoctorshedule',views.viewdoctorshedule,name='viewdoctorshedule'),
    path('booking3/<int:id>',views.booking3,name='booking3'),
    path('shedule4',views.shedule4,name='shedule4'),
    path('book2/<int:id>',views.book2,name='book2'),
    path('complaintpat',views.complaintpat,name='complaintpat'),
    path('block1/<int:id>',views.block1,name='block1'),
    path('unblock1/<int:id>',views.unblock1,name='unblock1'),
    path('accept1/<int:id>',views.accept1,name='accept1'),
    path('reject1/<int:id>',views.reject1,name='reject1'),
    path('shedule1',views.shedule1,name='shedule1'),
    path('editshedule',views.editshedule,name='editshedule'),
    path('updatetime/<int:id>',views.updatetime,name='updatetime'),
    path('shedule2/<int:id>',views.shedule2,name='shedule2'),
    path('deleteshedule/<int:id>',views.deleteshedule,name='deleteshedule'),
    path('viewpatientbookingdetails',views.viewpatientbookingdetails, name='viewpatientbookingdetails'),
    path('viewdoctorshedule',views.viewdoctorshedule,name='viewdoctorshedule'),
    path('addmedicine1',views.addmedicine1,name='addmedicine1'),
    path('shedule/<int:id>',views.shedule3,name='shedule'),
    path('accept/<int:id>',views.accept,name='accept'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('editmedicine/<int:id>',views.editmedicine,name='editmedicine'),
    path('deletemedicine/<int:id>',views.deletemedicine,name='deletemedicine'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('docchangepswrd',views.docchangepswrd,name='docchangepswrd'),
    path('home',views.home,name='home'),
    # path('docchangepswrd',views.docchangepswrd,name='docchangepswrd'),
    # path('docchangepswrd',views.docchangepswrd,name='docchangepswrd'),
    # path('docchangepswrd',views.docchangepswrd,name='docchangepswrd'),
    # path('docchangepswrd',views.docchangepswrd,name='docchangepswrd'),
    # path('docchangepswrd',views.docchangepswrd,name='docchangepswrd'),






]