import rospy
import pandas as pd
import math as m
import numpy as np
from pynput import keyboard
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher(tabla):
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    for fila in tabla:
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = fila 
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1.5)

excelName = 'Puntos_XYZ_JO.xlsx'
name = 'AJ'


arriba = 5  # altura herramienta no está escribiendo
abajo = 10.5  # altura herramienta está escribiendo
base = 6  # altura tomar la herramienta de la base
apertura = 0  # valor de articulación 5 abierta
cierre = 1.3  # valor de articulación 5 cerrada


def invKine(y, x, z, o):
	if z > 19.5 and z < 20.5:
		z = arriba
	if z > 3.5 and z < 4.5:
		z = abajo
	if o > 0.9 and o < 1.1:
		th5 = apertura
	else:
		th5 = cierre
	if x == 0:
		x = 0.01
	h = 14
	l1 = 10.6
	l2 = 10.6
	l3 = 11
	R1 = m.sqrt(pow(x, 2) + pow(y, 2))
	th1 = m.atan(y/x)
	zm = z - h
	R2 = R1 - l3
	th3 = m.acos((pow(R2, 2) + pow(zm, 2) - pow(l1, 2) - pow(l2, 2)) / (2*l1*l2))
	th2 = m.atan(R2 / zm)
	th4 = -(m.pi / 2) + abs(th2) + abs(th3)
	#if th2 > 1:
	#	th2 = 0
	return [-th1, th2, -th3, th4, th5]


arcoInt = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='ArcoInt'))
arcoIntInv = []
for fila in arcoInt:
	fila = np.append(fila, [0])
	arcoIntInv.append(invKine(fila[0], fila[1], fila[2], 0))

arcoExt = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='ArcoExt'))
arcoExtInv = []
for fila in arcoExt:
	fila = np.append(fila, [0])
	arcoExtInv.append(invKine(fila[0], fila[1], fila[2], 0))

names = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name=name))
namesInv = []
for fila in names:
	fila = np.append(fila, [0])
	namesInv.append(invKine(fila[0], fila[1], fila[2], 0))

triangulo = pd.DataFrame.to_numpy(
    pd.read_excel(excelName, sheet_name='Triangulo'))
trianguloInv = []
for fila in triangulo:
	fila = np.append(fila, [0])
	trianguloInv.append(invKine(fila[0], fila[1], fila[2], 0))

circulo = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Circulo'))
circuloInv = []
for fila in circulo:
	fila = np.append(fila, [0])
	circuloInv.append(invKine(fila[0], fila[1], fila[2], 0))

lineas = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Lineas'))
lineasInv = []
for fila in lineas:
	fila = np.append(fila, [0])
	lineasInv.append(invKine(fila[0], fila[1], fila[2], 0))

puntos = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Puntos'))
puntosInv = []
for fila in puntos:
	fila = np.append(fila, [0])
	puntosInv.append(invKine(fila[0], fila[1], fila[2], 0))

figura = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Figura'))
figuraInv = []
for fila in figura:
	fila = np.append(fila, [0])
	figuraInv.append(invKine(fila[0], fila[1], fila[2], 0))

home = [-25, 12, 3, 0]
home = invKine(home[0], home[1], home[2], home[3])

herramienta = [-25, 12]
angHerramienta = m.atan(herramienta[0] / herramienta[1])

tomarHerramientaInv = []
dejarHerramientaInv = []
rangoTotal = 5
for i in range(1, rangoTotal+1):
	if i != rangoTotal:
		tomarHerramientaInv.append(
		    invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 1))
	else:
		tomarHerramientaInv.append(
		    invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 1))
		tomarHerramientaInv.append(
		    invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 0))
		tomarHerramientaInv.append(
		    invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, arriba, 0))
		tomarHerramientaInv.append(home)


for i in range(1, rangoTotal+1):
	if i != rangoTotal:
		dejarHerramientaInv.append(
			invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, 4, 0))
	else:
		dejarHerramientaInv.append(
			invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, 4, 0))
		dejarHerramientaInv.append(
			invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, 4, 0))
		dejarHerramientaInv.append(
			invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 1))




while not rospy.is_shutdown():
        key=input()

        if key == 'q':
            joint_publisher(arcoIntInv)
            key=' '
        if key == 'a':
            joint_publisher(arcoExtInv)
            key=' '
        elif key == 's':
            joint_publisher(namesInv)
            key=' '
        elif key == 'd':
            joint_publisher(trianguloInv)
            key=' '
        elif key == 'f':
            joint_publisher(circuloInv)
            key=' '
        elif key == 'h':
            joint_publisher(lineasInv)
            key=' '
        elif key == 'g':
            joint_publisher(puntosInv)
            key=' '
        elif key == 'p':
            joint_publisher(figuraInv)
            key=' '
        elif key == 'i':
            joint_publisher(tomarHerramientaInv)
            key=' '
        elif key == 'j':
            joint_publisher(dejarHerramientaInv)
            key=' '
        
        


#joint_publisher([home])
#joint_publisher(tomarHerramientaInv)
#joint_publisher([home])
#joint_publisher(arcoIntInv)
#joint_publisher([home])
#joint_publisher(arcoExtInv)
#joint_publisher([home])
#joint_publisher(namesInv)
#joint_publisher([home])
#joint_publisher(trianguloInv)
#joint_publisher([home])
#joint_publisher(circuloInv)
#joint_publisher([home])
#joint_publisher(lineasInv)
#joint_publisher([home])
#joint_publisher(puntosInv)
#joint_publisher([home])
#joint_publisher(figuraInv)
#joint_publisher([home])
#joint_publisher(dejarHerramientaInv)
#joint_publisher([home])

#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#    listener.join()
