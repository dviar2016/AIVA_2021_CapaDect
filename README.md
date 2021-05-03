# CapaDect

Se pretende la implementación de un sistema, que mediante visión artificial localice los condensadores en placas de circuitos integrados para su procesamiento separado. De ahora en adelante se va a referir al sistema con el nombre de CapaDect.

El software CapaDect será capaz de reconocer a través de técnicas avanzadas de inteligencia artificial, en concreto Deep Learning, diferentes tipos de condensadores, independientemente de la posición, color, tamaño e iluminación de la placa. Los resultados tras el procesamiento serán transcritos a un documento txt, el cual contendrá información del centroide y el radio de cada condensador localizado en la imagen. Con la idea de proporcionar una supervisión manual al sistema CapaDect, se va a implementar un visor GUI que facilite la operabilidad entre sistema y usuario. CapaDect no busca interaccionar directamente con otras partes del sistema de reciclaje, será tarea de la empresa solicitante leer y procesar el fichero con las coordenadas.

![image](https://user-images.githubusercontent.com/80623121/111328931-fa5f3480-866e-11eb-9369-ae939697a2e0.png)

# Como Instalar CapaDect


CapaDect se ejecuta en la version de python 3.8.5, utiliza una serie de módulos necesarios para su ejecución. Estas dependencias pueden ser encontradas en el fichero requirements.txt de nuestro github.

1. Para instalar pyhton 3.8.5 visitar www.python.org
2. Para instalar las dependecias es suficiente con ejecutar el siguiente comando en el directorio donde se encuentra el archivo requirements.txt
    pip install -r requirements.txt
3. Para descargar el programa a través de GitHub hay dos formas. 
    1) Utilizar git clone https://github.com/dviar2016/AIVA_2021_CapaDect/
    2) Descargar el repositorio a través de github https://github.com/dviar2016/AIVA_2021_CapaDect/

4. Una vez instaladas las dependencias y descargados los ficheros, hay que ejecutar el programa. Para ello sobra con acceder al directorio scripts y lanzar el siguiente comando        python frontend.py (windows) 
     python3 frontend.py (linux).

# Ejecución de los test implementados
Para ser conscientes de la correcta ejecución del programa, se han implementado un test contenido en la carpeta scripts. Este trata de evaluar por separado los diferentes métodos que conforman las clases empleadas, para comprobar el correcto funcionamiento de estas. Su ejecución será con el siguiente comando:
    1) python backend_test.py(windows) 
    2) python3 backend_test.py (linux) 
