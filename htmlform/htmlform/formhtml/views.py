from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitor

def visitor_list_view(request):
    visitors = Visitor.objects.all()
    return render(request, 'home/visitor_list.html', {'visitors': visitors})

def visitor_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        purpose = request.POST.get('purpose')

        if name and email:
            Visitor.objects.create(name=name, email=email, phone=phone, purpose=purpose)

        return redirect('visitor_list')
    return render(request, 'home/visitor_form.html')

def visitor_edit_view(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.name = request.POST.get('name')
        visitor.email = request.POST.get('email')
        visitor.phone = request.POST.get('number')
        visitor.purpose = request.POST.get('purpose')
        visitor.save()
        return redirect('visitor_list')
    return render(request, 'home/visitor_form.html', {'visitor': visitor, 'edit': True})

def visitor_delete_view(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor_list')
    return render(request, 'home/visitor_delete.html', {'visitor': visitor})
