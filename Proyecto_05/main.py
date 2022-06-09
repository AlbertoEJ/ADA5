from grafo import Grafo

#generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(500)
grafo_dorogovtsev_mendes_30.layout()

"""
# Generamos grafo de mallas con 30 nodos
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(10, 10)
grafo_malla_30.layout()

# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
grafo_malla_500.layout()

# Generamos grafo Erdös y Rényi con 100 nodos y 200 aristas
grafo_erdos_30_200 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(100, 200)
grafo_erdos_30_200.layout()

# Generamos grafo Erdös y Rényi con 500 nodos y 600 aristas
grafo_erdos_30_200 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(500, 200)
grafo_erdos_30_200.layout()


# generamos grafo con modelo de Gilbert 100 nodos y probabilidad 0.02
grafo_gilbert_30_05 = Grafo(dirigido=False)
grafo_gilbert_30_05.grafo_gilbert(100, 0.02)
grafo_gilbert_30_05.layout()

# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.002
grafo_gilbert_30_05 = Grafo(dirigido=False)
grafo_gilbert_30_05.grafo_gilbert(500, 0.02)
grafo_gilbert_30_05.layout()

# generamos grafo con modelo geográfico simple con 100 nodos y r=0.21
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(500, 0.21)
grafo_geografico_30_05.layout()

# generamos grafo con modelo geográfico simple con 500 nodos y r=0.093
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(500, 0.093)
grafo_geografico_30_05.layout()

# generamos grafo con modelo Barabási-Albert con 100 nodos y grado 10
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(100, 10, False, False)
grafo_babarasi_30_10.layout()

# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 10
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(500, 10, False, False)
grafo_babarasi_30_10.layout()

generamos grafo con modelo Dorogovtsev-Mendes con 100 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(100)
grafo_dorogovtsev_mendes_30.layout()
"""


