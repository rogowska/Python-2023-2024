import math
#dodac obsluge bledow

def add_frac(frac1, frac2):
    gcd = math.gcd(frac1[1], frac2[1])
    if gcd == 1:
        frac3 = [frac1[0]*frac2[1] - frac2[0]*frac1[1], frac1[1]*frac2[1]]
    else:
        frac3 = []
    ###
    return frac3


def sub_frac(frac1, frac2): pass  # frac1 - frac2
    ###

def mul_frac(frac1, frac2):
    frac3 = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return frac3


def div_frac(frac1, frac2):
    frac3 = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
    return frac3


def is_positive(frac):
    if frac[0] == 0 or (frac[0] > 0 and frac[1] > 0):
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    float(frac1[0]/frac2[0])
    ###ddd


def frac2float(frac):
    return float(frac[0]/frac[1])
