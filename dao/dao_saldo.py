class SaldoDAO:
    def __init__(self):
        self.saldos = {
            "admin": 1000.0,
            "duran": 750.0
        }
        # Inicializar el atributo transacciones como un diccionario vacío
        self.transacciones = {
            "admin": [],
            "duran": []
        }

    def obtener_saldo(self, usuario):
        return self.saldos.get(usuario, None)

    def registrar_transaccion(self, usuario, tipo, monto):
        """Registra una transacción en el historial del usuario."""
        if usuario not in self.transacciones:
            self.transacciones[usuario] = []
        self.transacciones[usuario].append({
            "tipo": tipo,
            "monto": monto,
            "saldo_final": self.saldos[usuario]
        })

    def ingresar(self, usuario, monto):
        if usuario in self.saldos:
            self.saldos[usuario] += monto
            self.registrar_transaccion(usuario, "ingreso", monto)
            return self.saldos[usuario]
        return None

    def retirar(self, usuario, monto):
        if usuario in self.saldos and self.saldos[usuario] >= monto:
            self.saldos[usuario] -= monto
            self.registrar_transaccion(usuario, "retiro", monto)
            return self.saldos[usuario]
        return None

    def ver_transacciones(self, usuario):
        """Muestra el historial de transacciones de un usuario."""
        if usuario not in self.transacciones or not self.transacciones[usuario]:
            print("No hay transacciones registradas para este usuario.")
        else:
            print("\n--- Historial de Transacciones ---")
            for transaccion in self.transacciones[usuario]:
                print(f"Tipo: {transaccion['tipo']}, Monto: ${transaccion['monto']:.2f}, Saldo Final: ${transaccion['saldo_final']:.2f}")