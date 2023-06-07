from django.shortcuts import render
from .models import FamilyMember
from .forms import FamilyForm, RawFamilyForm
from django.http import JsonResponse

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
    return render(request, "member.html", {"obj1": obj1})

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
def images(request, *args, **kwagrs):
    print(request.user)
    members = FamilyMember.objects.all()
    return render(request, "images.html", {"members": members})
    # return HttpResponse("<h1>Hello Nugus</h1>")

def tree(request):
    return render(request, "tree.html")

def check_family_member(request):
    name = request.GET.get('name', '').strip()
    print("Current Name:", name)  # Print the current name to the console

    response_data = {'exists': False, 'parent': '', 'siblings': ''}

    siblings = FamilyMember.objects.filter(siblings__icontains=name)
    if siblings.exists():
        response_data['exists'] = True

        sibling = siblings.first()

        response_data['parent'] = sibling.parent

        siblings_names = sibling.siblings.split(',')
        siblings_names = [s.strip() for s in siblings_names if s.strip().lower() != name.lower()]
        response_data['siblings'] = ', '.join(siblings_names)

    else:
        children = FamilyMember.objects.filter(children__icontains=name)
        if children.exists():
            response_data['exists'] = True

            child = children.first()

            response_data['parent'] = child.name

            children_names = child.children.split(',')
            children_names = [s.strip() for s in children_names if s.strip().lower() != name.lower()]
            response_data['siblings'] = ', '.join(children_names)

    return JsonResponse(response_data)

# the database will likely be changed after deployment -> proposed mongodb