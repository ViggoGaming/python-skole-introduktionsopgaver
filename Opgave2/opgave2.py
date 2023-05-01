streng1 = "Der var engang"
streng2 = "en mand som"
streng3 = "boede i en spand. Spanden var af ler"

# Sammenkædning af de 3 strenge
print(streng1 + streng2 + streng3)

# Længden af de 3 strenge
print(f"""
Længde af streng 1: {len(streng1)}
Længde af streng 2: {len(streng2)}
Længde af streng 3: {len(streng3)}
""")

# Andet bogstav i hver streng
print(f"""
Andet bogstav i streng 1: {streng1[1]}
Andet bogstav i streng 2: {streng2[1]}
Andet bogstav i streng 3: {streng3[1]}
""")

# Undersøg om to af variablerne er det samme
if streng1[1] == streng2[1]:
    print("streng1 og streng 2 er ens")
if streng2[1] == streng3[1]:
    print("Streng2 og streng3 er ens")
if streng1[1] == streng3[1]:
    print("Streng1 og streng3 er ens")

print(f"{streng1.upper()} {streng2.upper()} {streng3.upper()}")

# Ny variabel der er en delstreng
delstreng = streng1[1:4]
print(delstreng)

# Sammenflet de tre variabler så det første bog stav er fra den første variable, den anden fra den anden osv.
print(streng1[0] + streng2[1] + streng3[2])

# Undersøg hvor mange forekomster af e der er i teksten.
tekst = streng1 + streng2 + streng3 
print(tekst.count("e"))
