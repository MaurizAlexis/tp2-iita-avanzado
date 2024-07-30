# Documentación de _Calculadora_ TP2

## Calculadora IMC

Calculadora de Índice de Masa Corporal personal que funciona para propositos personales de medición de mi IMC como hombre, funciona distinto para mujeres por su estructura ocea y carga muscular.

### Diseño de Código

1.  Se establece uso de Lenguaje de Python con POO para establecer una estructura más estable y funcional para el constante mejoramiento en caso de que se quiera desplegar mucho más.
1.  Desarrollo de la formula para calcular el IMC de las personas.

    **imc = peso / (altura \*\* 2)**

En mi código se ve así.

    def formula_imc(self, altura, peso):
        imc = peso / (altura ** 2)
        return imc

1.  Realiza el código el ingreso de datos de la persona como ser altura y peso
1.  Determina un rango de IMC de la persona en base a los datos de altura y peso calculados en el siguiente rango.

            18.5 y 24.9
            Tiene un peso saludable.
            25.0 y 29.9
            Usted tiene sobrepeso.
            30.0 y 34.9
            Usted tiene obesidad grado 1.
            35.0 y 39.9
            Usted tiene obesidad grado 2.
            40.0 en adelante.
            Usted tiene obesidad grado 3.

### Diseño de Software

#### Bloques de código

Se realiza el despliegue de una estructura basada en **Funciones** que se despliegan para dar uso a **POO** y complementar el código usando 2 bloques de código.

. El 1 bloque usa ciclos _While_ para iterar valores de la altura y peso de la persona.

. El 2 bloque utiliza _try_ y _except_ en todo el código para manejos de excepciones en el ingreso de datos y errores principalmente, de esta manera, se asegura el lugar puntual en el que se realiza un error en el código.

. Por último, se aclara que solamente uso **POO** en cada función para comodidad y preferencia de mi persona.

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

                altura = int(altura) / 100  # Convertir altura a metros
                peso = float(peso)

                imc = self.formula_imc(altura, peso)
                print(f"Tu altura es: {altura*100} cm, tu peso es: {peso} kg, tu IMC es: {imc:.2f}.")

                self.guia_imc(imc)  # Llamada a la función guía
                self.preguntar_continuar()
            except Exception as e:
                print(f"Ocurrió un error en la función 'solicita_datos': {e}")
                break

### Recomendaciones.

En caso de que lo prefiera, puede realizar cambios en beneficio de la mejora del código y su proposito principal, una herramineta de control del IMC.
