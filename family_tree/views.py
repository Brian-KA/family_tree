from django.shortcuts import render
from .models import FamilyMember
from .forms import FamilyForm, RawFamilyForm

# this view takes data from the user and updates the database
def family_form_view(request):
    form = RawFamilyForm()
    if request.method == 'POST':
        form = RawFamilyForm(request.POST)
    context = {
        "form": form
    }
    return render(request, "member/member_form.html", context)


# def family_form_view(request):
#     form = FamilyForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = FamilyForm()
#     context = {
#         "form": form
#     }
#     return render(request, "member/member_form.html", context)

def family_member_view(request):
    # test -> pick a specific member by id and display
#     obj = FamilyMember.objects.get(id=2)
    # context = {
    #     "name": obj.name,
    #     "parent": obj.parent,
    #     "siblings": obj.siblings,
    # }
    # pick all member details for display
    obj1 = FamilyMember.objects.all()
    
    # return render(request, "member/member.html", context)
    return render(request, "member/member.html", {"obj1": obj1})

# first view on the page -> to be done TODO
def home_view(request, *args, **kwagrs):
    print(request.user)
    nasty = {
        "niii": "shit",
        "alafu": 12,
        "null": ["q", "e", "e", "r"]
    }
    return render(request, "home.html", nasty)
    # return HttpResponse("<h1>Hello Nigga</h1>")

# gallery view. fething all data from the database, pick
# images and display with a lil data
def images_view(request, *args, **kwagrs):
    print(request.user)
    obj1 = FamilyMember.objects.all()
    return render(request, "images.html", {"obj1": obj1})
    # return HttpResponse("<h1>Hello Nugus</h1>") 
     

# the database will likely be changed after deployment -> proposed mongodb