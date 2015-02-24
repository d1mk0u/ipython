__author__ = 'dimkou'
def brutto_tootaja(brutto_palk=1000, tootaja_tootukindlustusmaks=0.016, kogumispension=0.02, tulumaks=0.2, tulumaksuvabanimum=154.0):
    tootaja_tootukindlustusmaks = brutto_palk * tootaja_tootukindlustusmaks
    kogumispension = brutto_palk * kogumispension
    tulumaks = (brutto_palk - (tootaja_tootukindlustusmaks+kogumispension+tulumaksuvabanimum)) * tulumaks
    netto = brutto_palk - tootaja_tootukindlustusmaks - kogumispension - tulumaks
    return netto
def brutto_tooandja(brutto_palk=1000, sots_maks = 0.33, tooandja_tootukindlustusmaks = 0.008):
    brutto =brutto_palk + ((brutto_palk * sots_maks) + (brutto_palk * tooandja_tootukindlustusmaks))
    return brutto
x = brutto_tootaja()
y = brutto_tooandja()
print "Netto tootaja:", x
print "Brutto Kogu:", y
