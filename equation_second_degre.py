import math

def discriminant(a, b, c):
    return b**2 - 4*a*c

def solutions_equation(a, b, c):
    delta = discriminant(a, b, c)
    print(f"\nDiscriminant (Δ) = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"Deux solutions réelles : x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Une solution réelle (double) : x = {x}")
    else:
        print("Pas de solution réelle (Δ < 0)")

# === Partie interactive ===
print("Résolution de l'équation ax² + bx + c = 0")
try:
    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    c = float(input("Entrez la valeur de c : "))
    
    if a == 0:
        print("Ce n'est pas une équation quadratique (a ne peut pas être 0).")
    else:
        solutions_equation(a, b, c)

except ValueError:
    print("Veuillez entrer uniquement des nombres.")
