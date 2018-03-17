from django import forms


# ERROR PORUKE
power_error_messages = {
    'required': 'Neophodno polje',
    'min_value': 'Mora biti vece od -100',
    'max_value': 'Mora biti manje od 100'
    }

factorial_error_messages = {
    'required': 'Neophodno polje',
    'min_value': 'Mora biti vece ili jednako 0',
    'max_value': 'Mora biti manje ili jednako 50',
    'invalid': 'Mora biti ceo broj'
    }

nzd_error_messages = {
    'required': 'Neophodno polje',
    'min_value': 'Mora biti vece od -1000000000',
    'max_value': 'Mora biti manje od 1000000000',
    'invalid': 'Mora biti ceo broj'
    }


# FORMA ZA UNOS BROJA ZA STEPENOVANJE
class PowerForm(forms.Form):
    base = forms.FloatField(
        min_value = -100.0,
        max_value = 100.0,
        label = 'Osnova',
        error_messages = power_error_messages,
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                            'step': '0.1'}))
    exponent = forms.FloatField(
        min_value = -100.0,
        max_value = 100.0,
        label = 'Izlozilac',
        error_messages = power_error_messages,
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                            'step': '0.1'}))


# FORMA ZA UNOS BROJA ZA IZRACUNAVANJE FAKTORIJELA
class FactForm(forms.Form):
    n = forms.IntegerField(
        min_value = 0,
        max_value = 50,
        label = 'Faktorijel n',
        error_messages = factorial_error_messages,
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                           'step': '1'}))


# FORMA ZA UNOS BROJEVA ZA KOJE SE IZRACUNAVA NAJVECI ZAJEDNICKI DELILAC
class NzdForm(forms.Form):
    a = forms.IntegerField(
        min_value = -1000000000,
        max_value = 1000000000,
        label = 'Broj a',
        error_messages = nzd_error_messages,
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                           'step': '1'}))
    b = forms.IntegerField(
        min_value = -1000000000,
        max_value = 1000000000,
        label = 'Broj b',
        error_messages = nzd_error_messages,
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                           'step': '1'}))


# FORMA ZA UNOS BROJA PRVIH PROSTIH PROJEVA
class PrimesForm(forms.Form):
    num_primes = forms.IntegerField(
        min_value = 1,
        max_value = 10000,
        label = 'Broj prostih',
        error_messages = {'required': 'Neophodno polje',
                          'min_value': 'Mora biti vece od 0',
                          'max_value': 'Mora biti manje ili jednako 10000',
                          'invalid': 'Mora biti ceo broj'},
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                           'step': '1'}))


# FORMA ZA UNOS BROJA NA OSNOVU KOG SE IZRACUNAVA FAKTORIJEL
class FactorsForm(forms.Form):
    n = forms.IntegerField(
        min_value = 2,
        max_value = 50000,
        label = 'Faktorizacija n',
        error_messages = {'required': 'Neophodno polje',
                          'min_value': 'Mora biti vece ili jednako 2',
                          'max_value': 'Mora biti manje ili jednako 50000',
                          'invalid': 'Mora biti ceo broj'},
        widget = forms.NumberInput(attrs = {'class': 'itxt',
                                           'step': '1'}))


# FORMA ZA UNOS  MATEMATICARA
class InputMathemForm(forms.Form):
    fname = forms.CharField(
        max_length = 40,
        label = 'Ime',
        error_messages = {'required': 'Neophodno polje',
                         'max_length': 'Ne sme biti duze od 40 karaktera'},
        widget = forms.TextInput(attrs = {'class': 'itxt',}))
    lname = forms.CharField(
        max_length = 40,
        required = False,
        label = 'Prezime',
        error_messages = {'max_length': 'Ne sme biti duze od 40 karaktera'},
        widget = forms.TextInput(attrs = {'class': 'itxt',}))
