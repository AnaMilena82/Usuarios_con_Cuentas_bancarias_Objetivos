class Usuario:		
    def __init__(self, name):
        self.name = name
        self.cuentas=[]
        # self.cuenta = CuentaBancaria(tasa_interes=0.01, balance=0)

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def hacer_deposito(self, cuenta, amount):
        cuenta.deposito(amount)
 
    def hacer_giro(self,cuenta, amount):
        cuenta.retiro(amount)

    def mostrar_balance_cuenta(self,cuenta):
        cuenta.mostrar_info_cuenta()


class CuentaBancaria:
    # cuentas_bancarias = []
    def __init__(self, num_cta,tasa_interes, balance):
        self.num_cta = num_cta
        self.tasa_interes = tasa_interes
        self.balance = balance
        # CuentaBancaria.cuentas_bancarias.append(self)

    def deposito(self, amount): #methodo deposito
        self.balance += amount
        print(f"Se ha realizado un depósito de {amount} en su cuenta:  {self.num_cta}, su nuevo balance es: {self.balance}")
        return self
    
    def retiro(self, amount): #methodo retiro disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; si no hay suficiente dinero, imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance -= amount
            print(f"Se ha realizado un retiro de {amount}en su cuenta:  {self.num_cta}, su nuevo balance es: {self.balance}")
        else:
            print("Fondos insuficientes se cobrara una tarifa de $5")
            self.balance -= 5 #se cobran 5
        return self
    
    @staticmethod
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
        
    def mostrar_info_cuenta(self): #methodo retiro
        print(f"en la cuenta:  {self.num_cta}, su Nuevo balance: {self.balance} ")
        return self

usuario = Usuario("Ana")

cuenta1 = CuentaBancaria(num_cta="12345",tasa_interes=0.01, balance=100)
cuenta2 = CuentaBancaria(num_cta="6789",tasa_interes=0.01, balance=300)

usuario.agregar_cuenta(cuenta1)
usuario.agregar_cuenta(cuenta2)
usuario.hacer_deposito(cuenta1,300)
usuario.hacer_deposito(cuenta2,100)
usuario.hacer_giro(cuenta1,100)
usuario.mostrar_balance_cuenta(cuenta1)
usuario.mostrar_balance_cuenta(cuenta2)






#     def transferir_dinero(self, destino, amount):
#         self.balance_cuenta -= amount	
#         destino.hacer_deposito(amount)
#         print(f"el Usuario {self.name} transfirio {amount} a {destino.name}")
# # instancias de Usuario
# usuario1 = Usuario("Ana")
# usuario2 = Usuario("Milena")
# usuario3 = Usuario("Isabella")

# # Hacer depósitos y giros para el primer usuario
# usuario1.hacer_deposito(100).hacer_deposito(150).hacer_deposito(75).hacer_giro(100).mostrar_balance_cuenta()

# usuario2.hacer_deposito(100).hacer_deposito(300).hacer_giro(50).hacer_giro(30).mostrar_balance_cuenta()

# usuario3.hacer_deposito(900).hacer_giro(200).hacer_giro(50).hacer_giro(100).mostrar_balance_cuenta()

# usuario1.transferir_dinero(usuario3,100)
# usuario1.mostrar_balance_cuenta()
# usuario3.mostrar_balance_cuenta()
# """  