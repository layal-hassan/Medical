from django.shortcuts import render
from .models import Services , Make_Order, Doctor , Price , Gallery
from .form import ApplyForm 

# Create your views here.
def service_list(request):
    service_list = Services.objects.all()
    context = {'services' : service_list}
    return render(request,'clinic/services.html',context)

from .models import Make_Order  # استيراد النموذج الذي سنستخدمه لحفظ البيانات

def make_order(request):
    doctor_list = Doctor.objects.all()
    context = {'doctor_list' : doctor_list}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('Email')  # تعديل اسم المتغير ليتطابق مع الأسلوب العام في Python
        comment = request.POST.get('comment')
        
        # إنشاء وحفظ الطلب في قاعدة البيانات
        new_order = Make_Order(name=name, Email=email, comment=comment)
        new_order.save()
        
        # يمكنك إعادة توجيه المستخدم بعد الحفظ إلى صفحة أخرى مثلاً
        return render(request, 'clinic/appointment.html',context)
    else:
        return render(request, 'clinic/appointment.html',context)
    
def appointment(request):
    doctor_list = Doctor.objects.all()
    context = {'doctor_list' : doctor_list}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('Email')  # تعديل اسم المتغير ليتطابق مع الأسلوب العام في Python
        comment = request.POST.get('comment')
        
        # إنشاء وحفظ الطلب في قاعدة البيانات
        new_order = Make_Order(name=name, Email=email, comment=comment)
        new_order.save()
        
        # يمكنك إعادة توجيه المستخدم بعد الحفظ إلى صفحة أخرى مثلاً
        return render(request, 'clinic/make_appointment.html',context)
    else:
        return render(request, 'clinic/make_appointment.html',context)
    



def team(request):
    doctor_list = Doctor.objects.all()
    context = {'doctor_list' : doctor_list}
    return render(request,'clinic/team.html',context)



def price(request):
    price_list = Price.objects.all()
    context = {'price_list' : price_list}
    return render(request,'clinic/prices.html',context)

def gallery(request):
    img_list = Gallery.objects.all()
    context = {'img_list' : img_list}
    return render(request,'clinic/gallery.html',context)


def contact(request):
    return render(request,'clinic/contact.html')


def about_us(request):
    return render(request,'clinic/about.html')