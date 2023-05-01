"""
O er antal ord i teksten
P er antal punktummer i teksten
L antal lange ord (over 6 bogstaver lange)
"""

tekst = "På et netsted bør man målrette sit sprog mod en meget bred målgruppe, og man skal tænke over, at det man s elv tror, man udtrykker meget klart, ikke nødvendigvis opfattes sådan. Man skal altid tænke over, at mange mennesker har problemer med at læse og opfatte. Man kan diskutere, hvorvidt meget faglige tekster kan gøres letlæselige, men generelle ikke-faglige tekster skal altid skrives i korte klare sætninger med et lavt lixtal."

ord = tekst.replace(".", "").replace(",", "").split()
ord_antal = len(ord)
punktummer = tekst.count('.')
lange_ord = 0

for words in ord:
	if len(ord) > 6:
		lange_ord += 1

LIX = round((ord_antal/punktummer)+((lange_ord*100)/ord_antal), 2)

print(f"Ord: {ord_antal}")
print(f"Punktummer: {punktummer}")
print(f"Lange ord: {lange_ord}")
print(f"LIX = {LIX}")

if LIX >= 55:
    print("Meget svær, faglitteratur på akademisk niveau, lovtekster.")
elif LIX >= 45:
    print("Svær, f.eks. saglige bøger, populærvidenskabelige værker, akademiske udgivelser.")
elif LIX >= 35:
    print("Middel, f.eks. dagblade og tidsskrifter.")
elif LIX >= 25:
    print("Let for øvede læsere, f.eks. ugebladslitteratur og skønlitteratur for voksne.")
elif LIX < 25:
    print("Let tekst for alle læsere, f.eks. børnelitteratur.")
