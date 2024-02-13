import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from ayurvedic.models import *
from . forms import *

# Create your views here.

def login(request):
    return render(request,'login.html')



# def login(request):
#     if request.POST:
#         frm=LoginForm(request.POST)
#         if frm.is_valid():
#             frm.save()
#     else:
#         frm=LoginForm()
#     return render(request,'login.html',{'frm':frm})


def signup(request):
    return render(request,'signup.html')

def doctorsregister(request):
    return render(request,'doctorsregister.html')

def dctrg(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    age=request.POST['textfield3']
    gender=request.POST['gender']
    place=request.POST['textfield5']
    post=request.POST['textfield7']
    pin=request.POST['textfield8']
    phone=request.POST['textfield9']
    email=request.POST['textfield10']
    username=request.POST['textfield11']
    password=request.POST['textfield12']

    obb=login1()
    obb.username=username
    obb.password=password
    obb.type="doctor"
    obb.save()

    ob=doctereg()
    ob.place=place
    ob.fname=fname
    ob.lname=lname
    ob.age=age
    ob.gender=gender
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.email=email
    ob.lid=obb
    ob.save()
    return HttpResponse('''<script>alert("successful");window.location="/"</script>''')


def patientregister(request):
    return render(request,'patientregister.html')


def patreg(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    age=request.POST['textfield3']
    gender=request.POST['gender']
    place=request.POST['textfield5']
    post=request.POST['textfield7']
    pin=request.POST['textfield8']
    phone=request.POST['textfield9']
    email=request.POST['textfield10']
    username=request.POST['textfield11']
    password=request.POST['textfield12']

    obb=login1()
    obb.username=username
    obb.password=password
    obb.type="patient"
    obb.save()

    ob=patientsreg()
    ob.fname=fname
    ob.lname=lname
    ob.age=age
    ob.gender=gender
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.email=email
    ob.lid=obb
    ob.save()
    return HttpResponse('''<script>alert("successful");window.location="/"</script>''')




def staffregister(request):
    return render(request,'staffregister.html')


def staffreg(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    age=request.POST['textfield3']
    gender=request.POST['gender']
    place=request.POST['textfield5']
    post=request.POST['textfield7']
    pin=request.POST['textfield8']
    phone=request.POST['textfield9']
    email=request.POST['textfield10']
    username=request.POST['textfield11']
    password=request.POST['textfield12']

    obb=login1()
    obb.username=username
    obb.password=password
    obb.type="staff"
    obb.save()

    ob=stafftreg()
    ob.fname=fname
    ob.lname=lname
    ob.age=age
    ob.gender=gender
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.email=email
    ob.lid=obb
    ob.save()
    return HttpResponse('''<script>alert("successful");window.location="/"</script>''')



def login2(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        ob=login1.objects.get(username=username,password=password)
        if(ob.type == "doctor"):
            request.session['did']=ob.id
            return redirect('/doctorshome')
        elif (ob.type=="patient"):
            request.session['pid']=ob.id
            return redirect("/patienthome")
        elif(ob.type == "staff"):
            request.session['sid']=ob.id
            return redirect("/staffhome")
        else:
            (ob.type == "admin")
            request.session['aid']=ob.id
            return redirect("/adminhome")
    except:
        return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')

def adminhome(request):
    return render(request,'adminhome.html')

def doctorshome(request):
    return render(request,'doctorshome.html')

def staffhome(request):
    return render(request,'staffhome.html')

def patienthome(request):
    return render(request,'patienthome.html')

def Verifydoctors(request):
    ob=doctereg.objects.all()
    return render(request,'Verifydoctors.html',{"data":ob})


def viewpatients(request):
    ob=patientsreg.objects.all()
    return render(request,'viewpatients.html',{"data":ob})

def viewdoctorshedule(request):
    ob=doctereg.objects.all()
    return render(request,'viewdoctorshedule.html',{"data":ob})

def book(request):
    ob=doctereg.objects.all()
    return render(request,'book.html',{"data":ob})

def viewbookingstatus(request):
    ob=booking.objects.filter(userid__lid__id=request.session['pid'])
    return render(request,'viewbookingstatus.html',{"data":ob})

def addmedicine(request):
    return render(request,'addmedicine.html')

def addshedule(request):
    return render(request,'addshedule.html')

def blockunblock(request):
    ob=stafftreg.objects.all()
    return render(request,'blockunblockstaff.html',{"data":ob})

def managemedicine(request):
    ob=medicine.objects.all()
    return render(request,'managemedicine.html',{"data":ob})
def manageshedule(request):
    ob=shedule.objects.filter(did__lid=request.session['did'])
    return render(request,'manageshedule.html',{"data":ob})

def sendcomplaints(request):
    return render(request,'sendcomplaints.html')
def sendreply(request,id):
    ob=sendcomplaints1.objects.filter(userid__lid_id=request.session['pid'])
    request.session['rid']=id
    return render(request,'sendreply.html',{"data":ob})

def verifybookingdetails(request):
    ob=booking.objects.all()
    return render(request,'verifybookingdetails.html',{"data":ob})


def viewbookingstatus(request):
    ob=booking.objects.filter(userid__lid__id=request.session['pid'])
    return render(request,'viewbookingstatus.html',{"data":ob})
def viewcomplaints(request):
    ob=sendcomplaints1.objects.filter(userid__lid_id=request.session['pid'])
    return render(request,'viewcomplaints.html',{"data":ob})
def viewcomplaintsreply(request):
    ob=sendcomplaints1.objects.all()
    return render(request,'viewcomplaintsreply.html',{"data":ob})
def viewdoctorshedule(request):
    ob=doctereg.objects.all()
    return render(request,'viewdoctorshedule.html',{"data":ob})


def viewpatientbookingdetails(request):
    # ob=booking.objects.filter(sid__did__id=request.session['did'])
    ob=booking.objects.all()
    return render(request,'viewpatientbookingdetails.html',{"data":ob})



def booking3(request,id):
    ob=shedule.objects.filter(did__id=id)
    return render(request,'booking.html',{"data":ob})

def book2(request,id):
    sid=shedule.objects.get(id=id)
    userid=patientsreg.objects.get(lid__id=request.session['pid'])
    ob=booking()
    ob.sid=sid
    ob.userid=userid
    ob.status='pending'
    ob.date=datetime.date.today()
    ob.save()
    return HttpResponse('''<script>alert("booked");window.location="/patienthome"</script>''')




def shedule4(request,id):
    ob=shedule.objects.filter(did__lid__id=id)
    return render(request,'shedule.html',{"data":ob})


def complaintpat(request):
    lob=patientsreg.objects.get(lid__id=request.session['pid'])
    complaint=request.POST['textarea']
    ob=sendcomplaints1()
    ob.complaint=complaint
    ob.date=datetime.today()
    ob.reply='pending'
    ob.userid=lob
    ob.save()
    return HttpResponse('''<script>alert("success");window.location="/patienthome"</script>''')

def blockunblock(request):
    ob=stafftreg.objects.all()
    return render(request,'blockunblockstaff.html',{"data":ob})


def block1(request,id):
    ob=login1.objects.get(id=id)
    ob.type= 'blocked'
    ob.save()
    return HttpResponse('''<script>alert("blocked");window.location="/blockunblock"</script>''')

def unblock1(request,id):
    ob=login1.objects.get(id=id)
    ob.type= 'staff'
    ob.save()
    return HttpResponse('''<script>alert("unblocked");window.location="/blockunblock"</script>''')


def accept1(request,id):
    request.session['aid']=id
    ob=login1.objects.get(id=id)
    ob.type='doctor'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location="/adminhome"</script>''')

def reject1(request,id):
    request.session['aid']=id
    ob=login1.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location="/adminhome"</script>''')

def shedule1(request):
    day=request.POST['day']
    ft=request.POST['time1']
    totime=request.POST['time2']
    sob=doctereg.objects.get(lid__id=request.session['did'])
    sh=shedule()
    sh.day=day
    sh.fromtime=ft
    sh.totime=totime
    sh.did=sob
    sh.save()
    return HttpResponse('''<script>alert("success");window.location="/doctorshome"</script>''')


def shedule3(request,id):
    ob=shedule.objects.filter(did__lid__id=id)
    return render(request,'shedule.html',{"data":ob})

def editshedule(request):
    day = request.POST['day']
    ft = request.POST['time1']
    totime = request.POST['time2']
    ob=shedule.objects.get(id=request.session['sid'])
    ob.day = day
    ob.fromtime = ft
    ob.totime = totime
    ob.save()
    return HttpResponse('''<script>alert("updated");window.location="/manageshedule"</script>''')

def deleteshedule(request,id):
    shedule.objects.get(id=id).delete()
    
    # ob=shedule.objects.get(id=id)
    # ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/doctorshome"</script>''')



def updatetime(request,id):
    request.session['sid']=id
    ob=shedule.objects.get(id=id)
    return render(request,'updatetime.html',{"data":ob})


def shedule2(request,id):
    did=shedule.objects.get(id=id)
    ob=shedule()
    ob.did=did
    ob.save()

def accept(request,id):
    ob=booking.objects.get(id=id)
    ob.status='accepted'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location="/staffhome"</script>''')

def reject(request,id):
    ob=booking.objects.get(id=id)
    ob.status='rejected'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location="/staffhome"</script>''')

def addmedicine1(request):
    med=request.POST['textfield1']
    use=request.POST['textfield2']
    discr=request.POST['textarea']
    price=request.POST['textfield5']

    ob=medicine()

    ob.medicine2=med
    ob.usage=use
    ob.discription=discr
    ob.price=price
    ob.save()
    return HttpResponse('''<script>alert("added");window.location="/adminhome"</script>''')

def editmedicine(request,id):
    request.session['id']=id
    ob=medicine.objects.get(id=id)
    return render(request,'editmedicine.html',{"id":ob})


def deletemedicine(request,id):
    ob=medicine.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/managemedicine"</script>''')


def changepassword(request):
    return render(request,'changepasswrd.html')

def docchangepswrd(request):
    currentpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    ob=login1.objects.get(password=currentpassword,id=request.session['did'])

    if (ob is not None):
        if(newpassword == confirmpassword):
            ob.password=newpassword
            ob.save()
            return HttpResponse('''<script>alert("password changed");window.location="/doctorshome"</script>''')
        else:
            return HttpResponse('''<script>alert("password not match");window.location=""</script>''')
    else:
        return HttpResponse('''<script>alert("invalid");window.location="/doctorshome"</script>''')
    


def home(request):
    return render(request,'home.html')
