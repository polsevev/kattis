def tilFahrenheit(celsius):
    return int((celsius*1.800) +32)
print("Celsius   Fahrenheit   Status")
for n in range(0, 101, 10):     #sjeker om tempraturen jeg startet med er over 60 grader

    if n >= 60:

        print("%-9d %-12d %s" % (n, tilFahrenheit(n),"Jeg svetter ihjel!"))
    else:
        print("%-9d %-12d %s" % (n, tilFahrenheit(n),"Jeg har det bra!"))

