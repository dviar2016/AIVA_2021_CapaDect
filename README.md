# CapaDect

Se pretende la implementación de un sistema, que mediante visión artificial localice los condensadores en placas de circuitos integrados para su procesamiento separado. De ahora en adelante se va a referir al sistema con el nombre de CapaDect.

El software CapaDect será capaz de reconocer a través de técnicas avanzadas de inteligencia artificial, en concreto Deep Learning, diferentes tipos de condensadores, independientemente de la posición, color, tamaño e iluminación de la placa. Los resultados tras el procesamiento serán transcritos a un documento txt, el cual contendrá información del centroide y el radio de cada condensador localizado en la imagen. Con la idea de proporcionar una supervisión manual al sistema CapaDect, se va a implementar un visor GUI que facilite la operabilidad entre sistema y usuario. CapaDect no busca interaccionar directamente con otras partes del sistema de reciclaje, será tarea de la empresa solicitante leer y procesar el fichero con las coordenadas.

![esta](https://user-images.githubusercontent.com/80623129/117434283-c4328880-af2c-11eb-9387-67ad3ded6baf.jpg)


# Como Instalar CapaDect
## Instalación Github
1.	Pyhton 3.8.5:
	 1) www.python.org .
2.	Para instalar las dependecias es suficiente con ejecutar el siguiente comando en el directorio donde se encuentra el archivo requirements.txt pip install -r requirements.txt
3.	Para descargar el programa a través de GitHub hay dos formas.
	1) Utilizar git clone:	
	    https://github.com/dviar2016/AIVA_2021_CapaDect/
	2) Descargar el repositorio a través de github
	    https://github.com/dviar2016/AIVA_2021_CapaDect/

4. Una vez instaladas las dependencias y descargados los ficheros, hay que ejecutar el programa. Para ello sobra con acceder al directorio scripts y lanzar el siguiente comando        python frontend.py (windows) 
     python3 frontend.py (linux).

## Instalación Docker (recomendado)

CapaDect ofrece una instalación docker para facilitar a sus clientes un ambiente de trabajo agil, sencillo y multiplataforma. 
1. Para inicializar la descargar de los archivos lanzar el siguiente comando.
	1) docker pull dviar/aiva_2021_capadect:aiva_2021_capadect
2. Este comando inicializará la descarga de todas las dependencias del programa, tanto librerías como código propio. Una vez descargado, comprobarla lista de imágenes en el sistema con:
	1) docker image ls –a
3. Cuando veamos la imagen con el name tag CapaDect, se procede a copiar la id de la imagen. Una vez se lanzaeste comando tenemos un container de nuestra imagen.
	1) docker create -it 52b4f4afdf87
4.Solo quedaría localizar el nombre del container y lanzar los siguientes comandos.
	1)docker container ls –a
	2) docker start d4f9c1734d72
	3) docker attach d4f9c1734d72

7. Únicamente quedaría presente lanzar el archivo. Para ello ir lanzar el siguiente comando:
	1) python3 home/capadect/AIVA_2021_CapaDect/scripts/frontend.py


# Ejecución de los test implementados
Para ser conscientes de la correcta ejecución del programa, se han implementado un test contenido en la carpeta scripts. Este trata de evaluar por separado los diferentes métodos que conforman las clases empleadas, para comprobar el correcto funcionamiento de estas. Su ejecución será con el siguiente comando:
    1) python backend_test.py(windows) 
    2) python3 backend_test.py (linux) 
