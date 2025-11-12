from resgister import register_user

# Ejemplo de uso del método de registro
if __name__ == "__main__":
    # Crear la tabla (solo la primera vez)
    # create_register_table()
    
    # Registrar un usuario
    register_user(
        name="Juan Pérez",
        email="juan@example.com",
        password="mi_contraseña_123"
    )
