<h1 align="center"> Laboratorio 5 Robótica </h1>

## Universidad Nacional de Colombia
-------------------------------------------------------------
> ## Autores

  > - Carlos Mario Jiménez Novoa. [cajimn](https://github.com/cajimn)
  > - Ivanna Lisette Medina Cruz. [IvannaMedinac](https://github.com/IvannaMedinaC)
  > - Juan Sebastian Rangel Araque. [juanBananin](https://github.com/juanBananin)


## Procedimiento

> ## Cinemática directa
Debido a problemas con el robot, se debió usar un robot diferente al que se uso en la anterior práctica de laboratorio, por lo tanto la cinemática directa cambia. Se determina la tabla de parámetros DH del robot



> ## Cinemática inversa
Se determina la cinemática inversa del robot:



![image](https://user-images.githubusercontent.com/51938754/199286921-473f9334-708a-4875-b833-a008dd02b2fe.png)
![image](https://user-images.githubusercontent.com/51938754/199299068-8083cb97-0b4f-46a0-8c2c-408d91a1ad80.png)

Se determina la expresión para cada uno de los parámetros articulares:

![image](https://user-images.githubusercontent.com/51938754/199287092-8b832403-7df1-438d-b329-453251a35676.png)

![image](https://user-images.githubusercontent.com/51938754/199299893-32b2221f-c5ea-46e7-9594-eae604f0a85d.png)
![image](https://user-images.githubusercontent.com/51938754/199300026-8efedf23-0846-4c69-ba5a-517c3723f338.png)


> ## Programa Python.

Se lee desde el programa de Python un archivo excel que contiene las coordenadas de todos los puntos de las correspondiente trayectorias (HOME, Recoger herramienta, Dibujar triángulo, Dibujar círculo, Dibujar líneas, Dibujar figura y Dibujar letras).

Como se realizó en el laboratorio anterior, se realiza la conexión con el robot desde la terminal y se ejecuta desde VS Code el código xxxx que se encuentra en la carpeta scripts del workspace.

Este código calcula la cinemática inversa del robot, de acuerdo a las ecuaciones que se hallaron anteriormente, dadas unas coordenadas x, y y z del gripper que sujeta la herramienta. Estas coordenadas se leen del archivo de excel y se encuentran los valores articulares correspondientes a ese punto dado.

Se usa el tópico joint_trajectory y se crea su respectivo Publisher para actualizar las posiciones de las articulaciones del robot. El programa permite que el robot realice las rutinas deseadas presionando una tecla determinada, cada tecla dibuja una figura o realiza una trayectoria distinta. 

> ## Resultado 

En este primer video se observa la rutina donde se dibuja el arco interior:

https://user-images.githubusercontent.com/51938754/199373413-74f3de17-c9c1-4e06-bd0b-d6616e0f6d17.mp4

Luego se observa la rutina donde dibuja el arco exterior:

https://user-images.githubusercontent.com/51938754/199373669-35b49364-7ce9-48cf-a89f-e8f7db9a2c91.mp4






