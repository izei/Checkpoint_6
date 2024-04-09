class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

usuario1 = Usuario("IzeiRodriguez", "Izei1234")

print("Nombre de usuario:", usuario1.username)
print("Contraseña:", usuario1.password)