from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Booking,Center,District,Authority
from .forms import BookingForm

from django.views.generic.detail import DetailView
# Create your views here.

def home(request):
    bookings = Booking.objects.all()
    authority = Authority.objects.all()
    return render(request,'book/home.html',{'bookings':bookings,'authority':authority})
login_required()
def dashboard(request):
    print(request.user)
    dash = Booking.objects.filter(user=request.user)
    print("das",dash)
    return render(request,'book/dashboard.html',{'dash':dash})
def expert(request,pk):

    exp = Authority.objects.get(pk=pk)

    return render(request,'book/experts.html',{'exp':exp})
def contact(request):
    return render(request,'book/contact.html')
@login_required()
def booking(request):

    form = BookingForm()
    context ={}
    initial_dict = {
        'user':request.user,
    }
    form = BookingForm(request.POST or None,initial=initial_dict)
    context['form'] = form
    if request.method == 'POST':

        form = BookingForm(request.POST or None, initial=initial_dict)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('book:dashboard')
    return render(request,'book/booking.html',context)
#ajax
def load_center(request):

    district_id = request.GET.get('district_id')
    centers = Center.objects.filter(district_id=district_id)

    return render(request,'book/center_dropdown.html',{'centers':centers})
