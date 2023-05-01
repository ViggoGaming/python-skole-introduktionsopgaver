def sumTal(tal: list) -> int:
    if len(tal) < 2:
        raise ValueError("Angiv venligst mindst 2 tal")
    return sum(tal)

summen = sumTal([1, 2])

print(summen)
