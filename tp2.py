class CalculadoraIMC:
  
  # Inicializa el código aplicando atributo self para llamar a funciones a ejecutarse en el código de python.
  
    def __init__(self):
        self.continuar = True
        
    def formula_imc(self, altura, peso):
        imc = peso / (altura ** 2)
        return imc
    
    def solicita_datos(self):
        while True:
            try:
                altura = input("Ingrese la altura que tiene en centímetros: ").strip()
                if not altura.isdigit() or int(altura) <= 0:
                    print("Por favor, ingrese su altura en números positivos.")
                    continue
                peso = input("Ingrese su peso en kilos: ").strip()
                if not peso.replace('.', '', 1).isdigit() or float(peso) <= 0:
                    print("Por favor, ingrese su peso en números positivos.")
                    continue
                
                altura = int(altura) / 100 
                peso = float(peso)
                
                imc = self.formula_imc(altura, peso)
                print(f"Tu altura es: {altura*100} cm, tu peso es: {peso} kg, tu IMC es: {imc:.2f}.")
                
                self.guia_imc(imc)  # Llamada a la función guía
                self.preguntar_continuar()
            except Exception as e:
                print(f"Ocurrió un error en la función 'solicita_datos': {e}")
                break
    
    def guia_imc(self, imc):
        try:
            if imc <= 18.5:
                print("Usted tiene bajo peso.")
            elif 18.5 < imc <= 24.9:
                print("Tiene un peso saludable.")
            elif 25.0 <= imc <= 29.9:
                print("Usted tiene sobrepeso.")
            elif 30.0 <= imc <= 34.9:
                print("Usted tiene obesidad grado 1.")
            elif 35.0 <= imc <= 39.9:
                print("Usted tiene obesidad grado 2.")
            else:
                print("Usted tiene obesidad grado 3.")
        except Exception as e:
            print(f"Ocurrió un error en la función 'guia_imc': {e}")
    
    def preguntar_continuar(self):
        while True:
            try:
                decision = input("¿Deseas continuar? (s/n): ").lower().strip()
                if decision == 'n':
                    print("Programa terminado.")
                    self.continuar = False
                    break
                elif decision == 's':
                    break
                else:
                    print("Opción incorrecta, por favor ingrese 's' para sí o 'n' para no.")
            except Exception as e:
                print(f"Ocurrió un error en la función 'preguntar_continuar': {e}")
                break
        
if __name__ == "__main__":
    calculadora = CalculadoraIMC()
    while calculadora.continuar:
        calculadora.solicita_datos()
    print("Fin del Programa.")
