from django.shortcuts import render
from baseten.forms import *
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from baseten.models import *
from baseten.models import *
from django.forms import formset_factory


# OVO SU OSNOVNE STATICNE STRANE GDE SE SAMO RENDERUJU TEMPLEJTI
def homepage(request):
    return render(request, 'baseten/home_page.djt')

def about_science(request):
    return render(request, 'baseten/o_nauci.djt')

def about_math(request):
    return render(request, 'baseten/o_matematici.djt')

def applications(request):
    return render(request, 'baseten/primene_matematike.djt')

def calculators(request):
    return render(request, 'baseten/kalkulatori.djt')

def mathematicians(request):
    return render(request, 'baseten/matematicari.djt')


# STEPEN
def power(request):
    if request.method == 'POST':
        form = PowerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = data['base']**data['exponent']
            return render(request, 'baseten/stepen_result.djt',
                         {'base': data['base'],
                          'exponent': data['exponent'],
                          'pow': result})
    else:
        form = PowerForm()
    return render(request, 'baseten/stepen_form.djt', {'form': form})


# FAKTORIJEL
def factorial(request):
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            n = data['n']
            fct = 1
            while n > 1:
                fct *= n
                n -= 1
            return render(request, 'baseten/faktorijel_result.djt',
                         {'data': data,
                          'fct': fct})
    else:
        form = FactForm()
    return render(request, 'baseten/faktorijel_form.djt',
                  {'form': form})


# NAJVECI ZAJEDNICKI DELILAC
def gcd(request):
    if request.method == 'POST':
        form = NzdForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            a = data['a']
            b = data['b']
            while b:
                tmp = b
                b = a % b
                a = tmp
            nzd = a
            return render(request, 'baseten/nzd_result.djt',
                          {'data': data,
                           'nzd': nzd})
    else:
        form = NzdForm()
    return render(request, 'baseten/nzd_form.djt',
                  {'form': form})


# DEF PROSTI BROJEVI
def primes(request):
    if request.method == 'POST':
        form = PrimesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['num_primes'] // 4
            prms = nprimes(data['num_primes'])
            return render(request, 'baseten/prosti_result.djt',
                          {'data': data,
                           'primes': prms})
    else:
        form = PrimesForm()
    return render(request, 'baseten/prosti_form.djt',
                  {'form': form})


# PROSTI CINIOCI
def primefact(request):
    if request.method == 'POST':
        form = FactorsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            factors = prime_factors(data['n'])
            return render(request, 'baseten/prosticinioci_result.djt',
                          {'data': data,
                           'factors': factors})
    else:
        form = FactorsForm()
    return render(request, 'baseten/prosticinioci_form.djt',
                  {'form': form})


# FUNKCIJA KOJA PRAVI LISTU ON PRVIH n PROSTIH BROJEVA
def nprimes(n):
    primelist = [2, 3, 5]
    cnt = n
    totest = primelist[-1]
    while cnt > 3:
        totest += 2
        limit = int(totest**0.5) + 1
        isprime = True
        for i in range(2, limit + 1):
            if totest % i == 0:
                isprime = False
                break
        if isprime:
            primelist.append(totest)
            cnt -= 1
    return primelist[:n]


# FUNKCIJA KOJA VRACA DICT KOJI SADRZI PROSTE CINIOCE BROJA PROSLEDJENOG
# KAO ARGUMENT
def prime_factors(n):
    prim = nprimes(n)
    factors = {}
    i = 0
    while n != 1:
        if n % prim[i] == 0:
            if prim[i] in factors:
                factors[prim[i]] += 1
            else:
                factors[prim[i]] = 1
            n = n // prim[i]
        else:
            i += 1
    return factors


# UNOS MATEMATICARA U BAZU
def input_mat(request):
    unesen = False
    message = ''
    if request.method == 'POST':
        form = InputMathemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fname = data['fname']
            if data['lname'] == '':
                lname = 'Nepoznato'
            else:
                lname = data['lname']
            if len(Mathematician.objects.filter(fname = fname, lname = lname)) == 0:
                message = 'Matematicar %s %s je uspesno unet u bazu podataka.' % (fname, lname)
                Mathematician.objects.create(fname = fname, lname = lname)
            else:
                message = 'Matematicar %s %s vec postoji u bazi.' % (fname, lname)
            form = InputMathemForm()
    else:
        form = InputMathemForm()
    return render(request, 'baseten/matematicari_input_form.djt',
                  {'form': form,
                   'unesen': unesen,
                   'message': message})


# LISTANJE MATEMATICARA IZ BAZE
def output_mat(request):
    matematicari = Mathematician.objects.all()
    return render(request, 'baseten/matematicari_listing.djt',
                  {'matematicari': matematicari})


# BRISANJE MATEMATICARA IZ BAZE
def delete_mat(request):
    obrisan = False
    message = ''
    if request.method == 'POST':
        form = InputMathemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fname = data['fname']
            if data['lname'] == '':
                lname = 'Nepoznato'
            else:
                lname = data['lname']
            try:
                Mathematician.objects.get(fname = fname, lname = lname).delete()
                obrisan = True
                message = "Matematicar %s %s je uspesno obrisan." % (fname, lname)
            except:
                message = "Matematicar %s %s ne postoji u bazi." % (fname, lname)
            form = InputMathemForm()
    else:
        form = InputMathemForm()
    return render(request, 'baseten/matematicari_brisanje.djt',
                  {'form': form,
                   'message': message})
