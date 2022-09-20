import email
from email.mime import message
from urllib import request
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Booked_Ticket

# Create your views here.
def index(request):
    return render(request, 'ticket/index.html',)

def bookTicket(request):
    if request.method == 'POST':
        tp = request.POST['flight-type']
        nm = request.POST['name']
        ph = request.POST['number']
        fm = request.POST['from']
        t = request.POST['to']
        dep = request.POST['departing']
        re = request.POST['returning']
        ad = request.POST['adults']
        ch = request.POST['childrens']
        cl = request.POST['class']
        book = Booked_Ticket(type=tp, name=nm, phone=ph, flying_from=fm, flying_to=t, departing_date=dep, return_date=re, adults=ad, childrens=ch, travel_class=cl)
        book.save()     
        return redirect('/myTicket/')
    return render(request, 'ticket/bookTicket.html')

def myTicket(request):
    booked = Booked_Ticket.objects.order_by('-id')
    return render(request, 'ticket/myTicket.html', {'ticket':booked})

def deletefun(request, id):
    if request.method == 'POST':
        dt = Booked_Ticket.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect('/myTicket/')
