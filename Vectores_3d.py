from re import X
import matplotlib.pyplot as plt

# se describe a continuación 5 vectores con sus componentes en x, y & z.
v = 1, 2, 2
w = 0, 0, -1
x = -2, -1, -3
y = 0, 1, 2
z = -3, -1, -3

#Se describen los parametros del entorno donde se graficará.
fig = plt.figure()
ax = plt.axes(projection ='3d')

ax.set_xlim([-5,3])
ax.set_ylim([-1.5,1.5])
ax.set_zlim([-5,4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
start = [0,0,0]

#se describen las instrucciones de proyección para cada vector y se le asigna un color
ax.quiver(start[0],start[1],start[2],v[0],v[1], v[2],color='blue')
ax.quiver(start[0],start[1],start[2],w[0],w[1], w[2],color='red')
ax.quiver(start[0],start[1],start[2],x[0],x[1], x[2],color='black')
ax.quiver(start[0],start[1],start[2],y[0],y[1], y[2],color='green')
ax.quiver(start[0],start[1],start[2],z[0],z[1], z[2],color='orange')

#Muestra el gráfico.
plt.show()

