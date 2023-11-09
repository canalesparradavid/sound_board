# Sound Board
Este proyecto consiste en un programa python que facilita la reproducción de sonidos almacenados en el sistema.

La idea de este programa es que se pueda utilizar en juegos de rol como ayuda para los sonidos de ambiente para sus campañas.

### Dependencias
Este proyecto depende de algunas librerias de python; los comandos para instalarlas se listan aqui abajo.

```cmd
pip install PyQt5
pip install pygame
```

### Configuración
Este programa se puede configurar modificando el fichero `config.json` en el que se establece el directorio donde iran los sonidos con el nombre de `directory` y en forma de matriz el nombre de sonido y fichero de los sonidos con el nombre de `sounds`.
Puede consultar [aquí](config.json) un ejemplo de configuración de este fichero. 

### Uso del programa
Para abir el programa en Windows es tan simple como hacer doble click sobre el fichero `tabla.py` o ejecutar el siguiente comando en la terminal.

    python tabla.py

Una vez arrancado se puede reproducir los sonidos almacenados en la carpeta sounds vinculados en el programa a cada botón de la matriz. Tambien se pueden reproducir mediante el atajo de teclado `CTRL+NUM` para <ins>**reproducir los sonidos**</ins> de la tabla y `ALT+NUM` para <ins>**cambiar entre las matrices**</ins> almacenadas.
