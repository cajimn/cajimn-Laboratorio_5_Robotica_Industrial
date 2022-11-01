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


> ## Resultado 

En este primer video se observa la rutina donde se dibuja el arco interior 

https://user-images.githubusercontent.com/68668422/196011297-8d86ad41-814a-4f38-b1d9-553ff0dfab27.mp4

Se realiza el movimiento hasta una posición deseada desde HOME articulación por articulación. Se sigue observando el desfase que tiene el robot.

https://user-images.githubusercontent.com/68668422/196011293-479089bc-00ba-41f3-8f41-30927088b858.mp4


Se puede ver que las posicones en la vida real se asemejan bastante a lo obtenido en las gráficas de matlab, los errores obtenidos pueden ser principalmente por errores de medición de los parámetros del robot. 
