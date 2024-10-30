class Triangulo:
    def __init__(self, a, b, c, ang1=None, ang2=None, ang3=None):
        self.a = a
        self.b = b
        self.c = c
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3

def compara_lados_e_angulo(t1, t2):
    return (
        (t1.a / t2.a == t1.b / t2.b and t1.ang1 == t2.ang1) or
        (t1.b / t2.b == t1.c / t2.c and t1.ang2 == t2.ang2) or
        (t1.a / t2.a == t1.c / t2.c and t1.ang3 == t2.ang3)
    )

def compara_angulos(t1, t2):
    conjunto_ang_t1 = {t1.ang1, t1.ang2, t1.ang3}
    conjunto_ang_t2 = {t2.ang1, t2.ang2, t2.ang3}
    return len(conjunto_ang_t1.intersection(conjunto_ang_t2)) >= 2

def compara_todos_os_lados(t1, t2):
    return (
        t1.a / t2.a == t1.b / t2.b == t1.c / t2.c
    )

def verifica_seme(t1, t2):
    if compara_todos_os_lados(t1, t2):
        return "Semelhança pelo critério LLL."
    elif compara_angulos(t1, t2):
        return "Semelhança pelo critério AA."
    elif compara_lados_e_angulo(t1, t2):
        return "Semelhança pelo critério LAL."
    else:
        return "Os triângulos não são semelhantes."

# Testes para cada critério

# Exemplo para LLL: Triângulos com lados proporcionais
t1 = Triangulo(3, 4, 5)
t2 = Triangulo(6, 8, 10)
print(verifica_seme(t1, t2))

# Exemplo para LAL: Triângulos com dois lados proporcionais e o ângulo entre eles congruente
t3 = Triangulo(2, 4, 5, 60, 60, 60)
t4 = Triangulo(3, 6, 7, 60, 60, 60)
print(verifica_seme(t3, t4))

# Exemplo para AA: Triângulos com dois ângulos congruentes
t5 = Triangulo(3, 5, 7, 45, 60, 75)
t6 = Triangulo(5, 7, 9, 45, 60, 75)
print(verifica_seme(t5, t6))
