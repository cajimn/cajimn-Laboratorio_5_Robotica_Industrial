<h1 align="center"> Laboratorio 5 Robótica </h1>

## Universidad Nacional de Colombia
-------------------------------------------------------------
> ## Autores

  > - Carlos Mario Jiménez Novoa. [cajimn](https://github.com/cajimn)
  > - Ivanna Lisette Medina Cruz. [IvannaMedinac](https://github.com/IvannaMedinaC)
  > - Juan Sebastian Rangel Araque. [juanBananin](https://github.com/juanBananin)


## Procedimiento

> ## Determinar parámetros DH
Se determina los TCP de todas lasartivulaciones de robot, como se ve en la imagen acontinuación
![WhatsApp Image 2022-10-14 at 4 14 28 PM](https://user-images.githubusercontent.com/68668422/196011269-9272b426-2255-4be2-a015-2875ad0d804b.jpeg)
 se obtienen las siguientes gráficas en matlab para las posicones:
 ![image](https://user-images.githubusercontent.com/52113892/196318127-a16b69b4-9ba3-4afc-86ff-d3ce5ddeb895.png)
![image](https://user-images.githubusercontent.com/52113892/196318174-95260471-9424-4c69-a7e2-2b637bef7977.png)
![image](https://user-images.githubusercontent.com/52113892/196318229-b8997ad2-596f-48c0-ac6d-cf6179339836.png)
![image](https://user-images.githubusercontent.com/52113892/196318265-7e46e7af-076d-4350-832b-42d2df2d41dc.png)
![image](https://user-images.githubusercontent.com/52113892/196318302-408174c1-ff77-4374-b1e4-ecdb24dd2dcb.png)
> ## Programa Python.
Se realiza la conexión entre dinamyxel y el programa creado en python, el cuál ejecuta con teclas, cada una de las posiciones establecidas en la guía de laboratorio. 

Para la conexión con Python se debe realizar la siguiente configuración en la terminal:

Primero se crea el paquete de catkin, en este caso la carpeta ctakin_ws

```shell
cd ~
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin build
```

Luego se clona el repositorio de px.robot, para tener una guía de los scrpits que se usan para mover el robot.
```shell
cd ~/catwin_ws/src
git clone https://github.com/felipeg17/px_robot
cd ..
source devel/setup.bash
```

Se debe verificar el puerto al que está conectado el robot:
```shell
lsusb
```
Luego, se dan los permisos respectivos al puerto USB0
```shell
ls /dev/tty*
sudo chmod 777 /dev/ttyUSB0
```
Antes de ejecutar el launch se corren las siguientes líneas de código:
```shell
catkin build px_motor
source devel/setup.bash
```
Se procede a ejcutar el launch
```shell
roslaunch px_robot px_controllers.launch
```
Por último se abre la aplicación vs Code para ejecutar el programa de Python [jointPub](scripts/jointPub.py). En esta se usa el tópico `joint_trajectory` y se crea su respectivo Publisher para actualizar las posiciones de las articulaciones del robot. El programa permite que el robot se dirija a las posiciones deseadas presionando una tecla determinada, indicandole el valor de cada articulación. Se tienen 5 teclas (a,s,d,f,h) para las 5 posiciones dadas en la guía de laboratorio y la tecla q para ir a HOME; además de unas teclas programadas (g,j,k,l,p) que dirigen el robot desde HOME (0,0,0,0,0) hasta una posición (30°,-30°,30°,-30°,10°) articulación por articulación.  

> ## Resultado 




En este primer video se observa la rutina que al presionar las teclas q, a, s, d y f el robot se dirige a HOME y luego a las posiciones que se piden en la guía de laboratorio. Se puede observar que la posición del robot (sobre todo el HOME) puede no estar totalmente calibrada o ser tan exacta, ya que no está totalmente horizontal, tiene un pequeño ángulo de desfase con respecto a la horizontal.

https://user-images.githubusercontent.com/68668422/196011297-8d86ad41-814a-4f38-b1d9-553ff0dfab27.mp4

Se realiza el movimiento hasta una posición deseada desde HOME articulación por articulación. Se sigue observando el desfase que tiene el robot.

https://user-images.githubusercontent.com/68668422/196011293-479089bc-00ba-41f3-8f41-30927088b858.mp4


Se puede ver que las posicones en la vida real se asemejan bastante a lo obtenido en las gráficas de matlab, los errores obtenidos pueden ser principalmente por errores de medición de los parámetros del robot. 
