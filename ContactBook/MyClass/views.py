
from .models import *
from django.shortcuts import *
from django.views import View
from django.http import HttpResponse, HttpRequest


def check_if_int(number):
    try:
        return int(number)
    except Exception:
        return None

def create_person(request):
    person = Person()
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    description = request.POST.get("description")
    person.name = name
    person.surname = surname
    person.description = description
    if name and surname:
        person.save()

def create_phone(request, id):
    phone = Phone()
    phone.number = request.POST.get("number")
    phone.type_number = request.POST.get("type_number")
    phone.person_phone= Person.objects.get(pk=id)
    if phone:
        phone.save()


class AddPerson(View):
    def get(self, request):
        return render(request, "formatki/addPerson.html")

    def post(self, request):
        create_person(request)
        return HttpResponse("Dodano nowy kontakt")


class PersonEdit(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        context = {
            'person': person
        }
        return render(request, "formatki/modifyPerson.html", context)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.name = request.POST.get("name")
        person.surname = request.POST.get("surname")
        person.description = request.POST.get("description")
        person.save()
        return HttpResponse("Wprowadzono zmiany")


class PersonDetails(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)

        context = {
            'person': person

        }
        return render(request, "formatki/dataPerson.html", context)

class AllPerson(View):
    def get(self, request):
        persons = Person.objects.all()

        context = {
            'persons': persons,

        }

        return render(request, "formatki/allPersons.html", context)



class PersonDelete(View):
    def get(self, request, id):
        context = {'person': Person.objects.get(pk=id)}
        return render(request, "formatki/deletePerson.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            person = Person.objects.get(pk=id)
            person.delete()
        return redirect('/')


class AddPhone(View):

    def get(self, request, id):
        return render(request, "formatki/addPhone.html")


    def post(self, request, id):
        create_phone(request, id)
        return HttpResponse("Dodano nowy telefon")

class AddAdress(View):

    def get(self, request, id):
        return render(request, "formatki/addAdress.html")

    def post(self, request, id):

            city = request.POST.get("city")
            street = request.POST.get("street")
            house_number = request.POST.get("house_number")
            apartment_number = request.POST.get("apartment_number")
            person_adress = Person.objects.get(pk=id)
            Adress.objects.create(city = city, street = street, house_number=house_number, apartment_number=apartment_number, person_adress=person_adress)
            return HttpResponse('Dodano nowy adres')

class AddEmail(View):
    def get(self, request, id):
        return render(request, "formatki/addEmail.html")

    def post(self, request, id):
        email = request.POST.get("email")
        email_type = request.POST.get("email_type")
        person_email = Person.objects.get(pk=id)
        Email.objects.create(email=email, email_type=email_type, person_email=person_email)
        return HttpResponse ('Dodano adres email')

class modifyAdress(View):
    def get(self, request, id):
        return render(request, "formatki/modifyAdress.html")

    def post(self, request, id):
        city = request.POST.get("city")
        street = request.POST.get("street")
        house_number = request.POST.get("house_number")
        apartment_number = request.POST.get("apartment_number")
        person_adress = Person.objects.get(pk=id)
        Adress.objects.create(city=city, street=street, house_number=house_number, apartment_number=apartment_number,
                              person_adress=person_adress)
        return HttpResponse('Zmieniono adres')

class modifyPhone(View):
    def get(self, request, id):
        return render(request, "formatki/modifyPhone.html")

    def post(self, request, id):
        create_phone(request, id)
        return HttpResponse('Zmieniono telefon')


class modifyEmail(View):
    def get(self, request, id):
        return render(request, "formatki/modifyEmail.html")

    def post(self, request, id):
        email = request.POST.get("email")
        email_type = request.POST.get("email_type")
        person_email = Person.objects.get(pk=id)
        Email.objects.create(email=email, email_type=email_type, person_email=person_email)
        return HttpResponse ('Zmieniono adres email')


class AddGroup(View):
    def get(self, request):
        return render(request, "formatki/addGroup.html")

    def post(self, request, id):
        name = request.POST.get("name")
        person = Person.objects.get(pk=id)
        Group.objects.create(name=name, person=person)
        return HttpResponse ('Stworzono nową grupę')


