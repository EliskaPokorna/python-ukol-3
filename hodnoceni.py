import json

with open('body.json', encoding='utf-8') as file:
    hodnoceni = json.load(file)
print(hodnoceni)

with open('bonusy.json', encoding='utf-8') as file:
    body = json.load(file)
print(body)



vysledky = {}

for jmeno, znamka in hodnoceni.items():
    if znamka >= 60:
        vysledky[jmeno] = "Pass"
    else:
       vysledky[jmeno] = "Fail"

print(vysledky)



vysledna_znamka = {}

for jmeno in hodnoceni:
    if jmeno in body:
        vysledna_znamka[jmeno] = hodnoceni[jmeno] + body[jmeno]
    else:
        vysledna_znamka[jmeno] = hodnoceni[jmeno]
print(vysledna_znamka)

for jmeno, body in vysledna_znamka.items():
    if body >= 90:
        vysledna_znamka[jmeno] = "1"
    elif body >= 70:
        vysledna_znamka[jmeno] = "2"
    elif body >= 50:
        vysledna_znamka[jmeno] = "3"
    elif body >= 30:
        vysledna_znamka[jmeno] = "4"
    else:
        vysledna_znamka[jmeno] = "5"
print(vysledna_znamka)



with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(vysledky, file, ensure_ascii=False, indent=4)

with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(vysledna_znamka, file, ensure_ascii=False, indent=4)