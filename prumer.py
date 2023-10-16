import sys

cisla = sys.argv[1:]
total = 0
print(cisla)
pocetcisel = 0

for x in cisla:
    try:
        print(x)
        total += int(x)
        pocetcisel = pocetcisel + 1
    except:
        print(f' {e} neni cele cislo!!!!!')


print(f'Prumer je {total/pocetcisel}')\


