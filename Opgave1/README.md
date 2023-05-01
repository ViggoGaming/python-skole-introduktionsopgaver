# Opgave 1 (*)
Lixtallet er et udtryk for en teksts læsbarhed. Formlen til at beregne
LIX-tallet er givet ved
$\text{LIX} = \frac{O}{P}+\frac{L\cdot 100}{O}$ hvor $O$ er antal ord
i teksten, $P$ er antal punktummer i teksten og $L$ antal lange ord
(over 6 bogstaver lange).

Formlen kan altså forstås som antal ord per mellem hvert punktum lagt
sammen med procentdelen af de lange ord i teksten. Man har så følgende
skala til at vurdere LIX-tallet med:
-   $\text{LIX}\geq 55$: Meget svær, faglitteratur på akademisk niveau,
    lovtekster.

-   $45\leq\text{LIX}< 55$: Svær, f.eks. saglige bøger,
    populærvidenskabelige værker, akademiske udgivelser.

-   $35\leq\text{LIX}< 45$: Middel, f.eks. dagblade og tidsskrifter.

-   $25\leq\text{LIX}< 35$: Let for øvede læsere, f.eks.
    ugebladslitteratur og skønlitteratur for voksne.

-   $\text{LIX}<25$: Let tekst for alle læsere, f.eks. børnelitteratur.

1.  Lav et program, der bestemmer Lix-tallet af en tekststreng.
    Programmet skal fortælle hvilket niveau teksten ligger på. Antag at
    du får teksten i en string-variable.

2.  Benyt din LIX-beregner på en tekst du skrev i folkeskolen og en
    tekst, du har skrevet i gymnasiet (det kunne f.eks. være en dansk
    stil).
