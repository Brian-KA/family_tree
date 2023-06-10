from django.contrib.auth import authenticate, login
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

def login_view(request):
    family_members = FamilyMember.objects.all()
    total_members = family_members.count()
    deceased_members = family_members.filter(dead=True).count()
    query = request.GET.get('search')
    if query:
        family_members = family_members.filter(name__icontains=query)

    usernames = []
    passwords = []
    for member in family_members:
        member_username = member.name
        member_password = member.password
        usernames.append(member_username)
        passwords.append(member_password)
    authentication_data = zip(usernames, passwords)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        for (uname, passd) in authentication_data:
            
            if username == uname and password == passd:
                return render(request, 'home.html', {"members": family_members,
                                         'total_members': total_members,
                                         'deceased_members': deceased_members
                                         })
            else:
                error_message = 'Invalid username or password'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def home_base_view(request):
    family_members = FamilyMember.objects.all()[:3]
    context = {'family_members': family_members}
    return render(request, "homy.html", context)

def family_member_view(request):
    # members = FamilyMember.objects.get()
    members = FamilyMember.objects.all()
    current_user = request.user
    member_objects = []
    for member in members:
        if member.name == current_user:
            return member
            # member_objects.append(member)
    # member = [member for member in member_objects]
    print(member)
    # context = {"members": member}
    context = {
        "name": member.name,
        "parents": member.parent,
        "siblings": member.siblings,
        "dob": member.dob,
        "phone": member.phone,
        "email": member.email,
    }
    return render(request, "member.html", context)

# first view on the page -> to be done TODO
def home_view(request):
    print(request.user)
    members = FamilyMember.objects.all()
    total_members = members.count()
    deceased_members = members.filter(dead=True).count()
    query = request.GET.get('search')
    if query:
        members = members.filter(name__icontains=query)

    return render(request, "home.html", {"members": members,
                                         'total_members': total_members,
                                         'deceased_members': deceased_members
                                         })

# gallery view. fething all data from the database, pick
# images and display with a lil data
def images(request, *args, **kwagrs):
    print(request.user)
    members = FamilyMember.objects.all()

    query = request.GET.get('search')
    if query:
        members = members.filter(name__icontains=query)

    return render(request, "images.html", {"members": members})

def tree(request):
    family_members = FamilyMember.objects.all()
    context = {'family_members': family_members}
    return render(request, "tree.html", context)

def check_family_member(request):
    name = request.GET.get('name', '').strip()
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