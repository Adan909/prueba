
import os

class UsuarioDAO:
    def agregar_usuario(self, usuario, clave_ingresada):
        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{usuario},{clave_ingresada}\n")
        
            
    def cargar_usuarios(self):
        usuarios = {} 
        if os.path.exists('usuarios.txt'):
            with open("usuarios.txt", "w") as archivo:
                for linea in archivo:
                    try:
                        usuario, clave = linea.strip().split(',')
                        usuarios[usuario.strip()] = clave.strip()
                    except ValueError:
                        continue  # Saltar líneas mal formateadas
        return usuarios 

    def inicio(self, usuario, clave_ingresada):
        usuarios = self.cargar_usuarios()
        if usuario in usuarios and usuarios[usuario] == clave_ingresada:
            print("Acceso permitido")
            return True
        else:
            print("Usuario o contraseña incorrectos.\n")
            return False
if __name__ == "__main__":
    dao = UsuarioDAO()
    dao.agregar_usuario("admin", "admin456")
    dao.agregar_usuario("duran", "duran456")