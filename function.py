from math import degrees, radians, sin, cos, sqrt, acos


def calc(a, b, c, al, be, ce):
    try:
        if al and be and not ce:
            ce = 180 - (al + be)
        if al and ce and not be:
            be = 180 - (al + ce)
        if be and ce and not al:
            al = 180 - (ce + be)
        if al and be and not ce:
            ce = 180 - (al + be)
        if al and ce and not be:
            be = 180 - (al + ce)
        if be and ce and not al:
            al = 180 - (ce + be)
        ####
        cosce = cos(radians(ce))
        since = sin(radians(ce))
        cosal = cos(radians(al))
        sinal = sin(radians(al))
        cosbe = cos(radians(be))
        sinbe = sin(radians(be))
        ####
        if c and a and not b and be:
            d = (a ** 2 + c ** 2 - 2 * a * c * cosbe)
            b = sqrt(d)
        if a and b and ce and not c:
            d = a ** 2 + b ** 2 - 2 * a * b * cosce
            c = sqrt(d)

        if b and c and al and not a:
            d = b ** 2 + c ** 2 - 2 * c * b * cosal
            a = sqrt(d)

        if a and c and be and not b:
            d = a ** 2 + c ** 2 - 2 * a * c * cosbe
            a = sqrt(d)
        ####
        if not a and be and b and al:
            a = b * sinal / sinbe
        elif not a and ce and c and al:
            a = c * sinal / since

        if not b and al and a and be:
            b = a * sinbe / sinal
        elif not be and ce and c and be:
            b = c * sinbe / since

        if not c and al and a and ce:
            c = a * since / sinal
        elif not c and ce and b and be:
            c = b * since / sinbe
        ####
        if a and b and ce and not c:
            d = a ** 2 + b ** 2 - 2 * a * b * cosce
            c = sqrt(d)

        if b and c and al and not a:
            d = b ** 2 + c ** 2 - 2 * c * b * cosal
            a = sqrt(d)

        if not a and c and be and not b:
            d = a ** 2 + c ** 2 - 2 * a * c * cosbe
            a = sqrt(d)
        ####
        if a and b and c and not al:
            cosal = -(a ** 2 - b ** 2 - c ** 2) / (2 * c * b)
            al = acos(cosal)
            al = degrees(al)
        if a and b and c and not be:
            cosbe = -(b ** 2 - c ** 2 - a ** 2) / (2 * a * c)
            be = acos(cosbe)
            be = degrees(be)
        if a and b and c and not ce:
            cosce = -(c ** 2 - b ** 2 - a ** 2) / (2 * a * b)
            ce = acos(cosce)
            ce = degrees(ce)
        ####
        if a and b and c and not al:
            cosal = -(a ** 2 - b ** 2 - c ** 2) / (2 * c * b)
            al = acos(cosal)
            al = degrees(al)
        if a and b and c and not be:
            cosbe = -(b ** 2 - c ** 2 - a ** 2) / (2 * a * c)
            be = acos(cosbe)
            be = degrees(be)
        if a and b and c and not ce:
            cosce = -(c ** 2 - b ** 2 - a ** 2) / (2 * a * b)
            ce = acos(cosce)
            ce = degrees(ce)
        if c and a and not b and be:
            d = (a ** 2 + c ** 2 - 2 * a * c * cosbe)
            b = sqrt(d)
        ####   
        ce = radians(ce)
        al = radians(al)
        be = radians(be)
        since = sin(ce)
        sinal = sin(al)
        sinbe = sin(be)
        p = (a + b + c) * 0.5
        s = p * (p - a) * (p - b) * (p - c)
        sal = ((c * b * sinal) / 2) ** 2
        sce = ((a * b * since) / 2) ** 2
        sbe = ((a * c * sinbe) / 2) ** 2
        ####
        if not (1 >= sal - s >= -1) \
                or not (1 >= sce - s >= -1) or not (1 >= sbe - s >= -1):
            a = 0
            b = 0
            c = 0
            al = 0
            be = 0
            ce = 0
        al = degrees(al)
        be = degrees(be)
        ce = degrees(ce)
        if a + b <= c or a + c <= b or b + c <= a:
            a = 0
            b = 0
            c = 0
            al = 0
            be = 0
            ce = 0
            
    except ValueError:
        a = 0
        b = 0
        c = 0
        al = 0
        be = 0
        ce = 0
    return c, ce, a, al, b, be
