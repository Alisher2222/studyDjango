from django.shortcuts import render

pets = [
    {'id':1, 'name':'Dosik'},
    {'id':2, 'name':'Pushistic'},
    {'id':3, 'name': 'Avrora'}
]

def home(request):
    return render(request, 'basics/home.html', {'pets': pets})
def dogs(request,pk):
    return render(request, 'basics/dogs.html/')