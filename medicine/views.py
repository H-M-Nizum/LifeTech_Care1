from django.shortcuts import render, redirect
from .forms import MedicinelistForm
from .models import MedicinelistModel

def create_medicine(request):
    if request.method == 'POST':
        form = MedicinelistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = MedicinelistForm()

    return render(request, 'add_medicine.html', {'form': form})
