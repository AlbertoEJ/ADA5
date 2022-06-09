# Proyecto 5
Alumno: Alberto Espinosa Juárez

Programa Académico: Maestría en Ciencias de la Computación

## ¿Qué contiene el proyecto 5?
El proyecto 5 consiste en dado un grafo, y utilizando pygame, generar una visualización del mismo. Mediante el método Spring. Calcular la disposición de un grafo mediante el algoritmo de resortes presentado por P. Eades (1984). O(m+n)


Los archivos que contiene la carpeta "Proyecto_05" son: 
+ nodo.py Archivo que contiene la clase que define a un nodo y sus métodos
+ arista.py Archivo que contiene la clase que define a una arista y sus métodos
+ grafo.py y archivos para cada algoritmo. Archivos que contienen la clase que define a un grafo y sus métodos, además, contiene los algortimos descritos para el proyecto 1 y contiene los algoritmos DFS (recursivo e iterativo) y BFS, correspondientes al proyecto 02, así como Dijkstra para el proyecto03 y KruskaID, KruskalI y Prim para el proyecto 4. Así como el método método Spring del proyecto 5.
+ main.py Archivo que contiene la generación y guardado de cada uno de los grafos, tanto los generados como los calculados.
+ grafo2dot.py Archivo que hace la conversión a lenguaje .dot
+ Carpeta imagenes que contiene las imágenes correspondientes a la generación del método Spring


## ¿Cómo veo la documentación?
Para revisar la documentación es necesario hacer uso del método *help(método)* que nos brindará información sobre cómo y qué hace un método.

**Ejemplo**

help(guardar_grafo)

**Desplegará información sobre el método guardar_grafo así como también de los parámetros que recibe**

## Resúmen del proyecto 5

### Modelo de malla 100 nodos
![Grafo en malla de 100 nodos][malla1]
Video: Video: https://drive.google.com/file/d/1NUz4c6-5Y8EMv0DPY3OnBC6vCoGuvvcS/view?usp=sharing

[malla1]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/malla100.png

### Modelo de malla 500 nodos
![Grafo en malla de 500 nodos][malla2]
Video: Video: https://drive.google.com/file/d/1QpbxlvzadBfd-UMPLKn0j23C23abyLmp/view?usp=sharing

[malla2]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/Malla500.png

### Modelo de Gilbert de 100 nodos y probabilidad de 0.02
![Grafo en gilbert de 100 nodos][gilbert1]
Video: Video: https://drive.google.com/file/d/1eSGe77-6_xvhKWU9l8OyXCF5_f6UOClf/view?usp=sharing

[gilbert1]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/gilbert100_nodos_probabilidad_0_02.png

### Modelo de Gilbert de 500 nodos y probabilidad de 0.002
![Grafo en gilbert de 500 nodos][gilbert2]
Video: Video: https://drive.google.com/file/d/1wTNo68PH0sRPDR1SVevbgEw4kC1ofUeR/view?usp=sharing

[gilbert2]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/gilbert500_nodos_probabilidad_0_002.png

### Modelo de Erdos y Renyi de 100 nodos y 200 aristas
![Grafo en erdos y renti de 100 nodos][renyi1]
Video: Video: https://drive.google.com/file/d/1aw_YNfuB45PI9cKOrXoac5khD3mxmd8Q/view?usp=sharing

[renyi1]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/erdos_renyi_100_nodos_200_aristas.png

### Modelo de Erdos y Renyi de 500 nodos y 600 aristas
![Grafo en erdos y renti de 500 nodos][renyi2]
Video: Video: https://drive.google.com/file/d/1Cqe4tosV4Kk1FNYGvoLiUGoN3Av5XjfA/view?usp=sharing

[renyi2]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/erdos_renyi_500_nodos_600_aristas.png

### Modelo de Babarasi-Albert de 100 nodos y grado 10
![Grafo en babarasi-albert de 100 nodos][babarasi]
Video: Video: https://drive.google.com/file/d/1CFD2tGsfg9ngn6YcxvfvUj5S_mJYAFHv/view?usp=sharingg

[babarasi]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/babarasi-albert_100_nodos_grado_10.png

### Modelo de Babarasi-Albert de 500 nodos y grado 10
![Grafo en babarasi-albert de 500 nodos][babarasi2]
Video: Video: https://drive.google.com/file/d/1ssQji2jEsd672kRuaKh7odukFymNvQay/view?usp=sharing

[babarasi2]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/babarasi-albert_500_nodos_grado_10.png

### Modelo de Geográfico de 100 nodos y r=0.21
![Grafo en geografico de 100 nodos][geografico]
Video: Video: https://drive.google.com/file/d/1U9tWGwAigFShIczBTE6kTJgMnnijMHsr/view?usp=sharing

[geografico]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/geografico100_r_0_21.png

### Modelo de Geográfico de 500 nodos y r=0.93
![Grafo en geografico de 500 nodos][geografico2]
Video: Video: https://drive.google.com/file/d/1Nj0SMiVRB2dHxLfRP88HH_lJrujkKQEo/view?usp=sharing

[geografico2]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/geografico500_r_0_093.png

### Modelo de Dorogovtsev_mendes de 100 nodos
![Grafo en Dorogovtsev_mendes de 100 nodos][Dorogovtsev_mendes]
Video: Video: https://drive.google.com/file/d/1k_GiLdi0BrluoDiY7tJ9ttObQLgh5Cd7/view?usp=sharing

[Dorogovtsev_mendes]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/Dorogovtsev_mendes_100_nodos.png

### Modelo de Dorogovtsev_mendes de 500 nodos
![Grafo en Dorogovtsev_mendes de 100 nodos][Dorogovtsev_mendes2]
Video: Video: https://drive.google.com/file/d/11thlhg9bfoFvd1yoiqBMwBITFHU1ACL2/view?usp=sharing

[Dorogovtsev_mendes2]: https://github.com/AlbertoEJ/ADA5/blob/main/imagenes/Dorogovtsev_mendes_500_nodos.png

