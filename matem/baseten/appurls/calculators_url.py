from django.conf.urls import url
from baseten.views import calculators, power, factorial, gcd, primes, primefact


urlpatterns = [
    url(r'^$', calculators),
    url(r'^power/$', power),
    url(r'^factorial/$', factorial),
    url(r'^gcd/$', gcd),
    url(r'^primes/$', primes),
    url(r'^prime-factors/$', primefact),
]
