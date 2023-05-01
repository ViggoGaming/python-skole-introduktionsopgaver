# Undersøg om en tekststreng er et palindrom. Dvs. om tekststrengen læses og skrives på samme måde forfra og bagfra.
string = "den laks skal ned"

if string.lower() == string.lower()[::-1]:
    print(f"Strengen '{string}' er et palindrom")
else:
    print("Den angivet streng er ikke et palindrom")

"""
Ternary operator
value_if_true if condition else value_if_false
"""

# print(f"Strengen '{string}' er et palindrom" if string.lower() == string.lower()[::-1] else "Den angivet streng er ikke et palindrom")
