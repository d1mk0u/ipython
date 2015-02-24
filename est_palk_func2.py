#!/usr/bin/python
# -*- coding: UTF8 -*-
__author__ = 'dimkou'

def tootaja_tootukindlustusmaks(brutto_palk):
    x = brutto_palk * 0.016
    return x
def tootaja_kogumipension(brutto_palk):
    x = brutto_palk * 0.02
    return x
def tulumaks(brutto_palk):
    x = (brutto_palk - tootaja_kogumipension(brutto_palk) - tootaja_tootukindlustusmaks(brutto_palk) - 154.0) * 0.2
    return x

def arvutus():
    brutto_sum = int(raw_input("Kirjua oma brutto palk: "))
    netto = brutto_sum - tootaja_kogumipension(brutto_sum) - tootaja_tootukindlustusmaks(brutto_sum) - tulumaks(brutto_sum)
    return netto
x = arvutus()
print "Netto palk", x
