class TrianguloInterno:
    def __init__(self, lado_x, lado_y, lado_z):
        self.lado_x = lado_x
        self.lado_y = lado_y
        self.lado_z = lado_z

    def obter_razao_bissetriz_interna(self):
        # Calcula a razão das partes criadas pela bissetriz interna no lado oposto
        razao_interna = self.lado_x / self.lado_y
        return razao_interna

# Exemplo de uso para bissetriz interna
lado_x = float(input("Informe o comprimento do lado X: "))
lado_y = float(input("Informe o comprimento do lado Y: "))
lado_z = float(input("Informe o comprimento do lado Z: "))

triangulo_interno = TrianguloInterno(lado_x, lado_y, lado_z)
print("Razão das partes geradas pela bissetriz interna:", triangulo_interno.obter_razao_bissetriz_interna())

class TrianguloExterno:
    def __init__(self, lado_p, lado_q, lado_r):
        self.lado_p = lado_p
        self.lado_q = lado_q
        self.lado_r = lado_r

    def obter_razao_bissetriz_externa(self):
        # Calcula a razão das partes criadas pela bissetriz externa no lado oposto
        razao_externa = self.lado_p / self.lado_q
        return razao_externa

# Exemplo de uso para bissetriz externa
lado_p = float(input("Informe o comprimento do lado P: "))
lado_q = float(input("Informe o comprimento do lado Q: "))
lado_r = float(input("Informe o comprimento do lado R: "))

triangulo_externo = TrianguloExterno(lado_p, lado_q, lado_r)
print("Razão das partes geradas pela bissetriz externa:", triangulo_externo.obter_razao_bissetriz_externa())
