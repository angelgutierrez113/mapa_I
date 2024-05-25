import matplotlib.pyplot as plt
import networkx as nx

# Creación del grafo
G = nx.DiGraph()

# Añadir nodos y aristas
G.add_node("Educación a Distancia (EaD)")
G.add_nodes_from(["Historia y Evolución", "Tecnología y Herramientas", "Rol del Docente", "Aprendizaje Autónomo", "Paradigma Educativo", "Sociedad Digital", "Desafíos y Perspectivas"])
G.add_edges_from([
    ("Educación a Distancia (EaD)", "Historia y Evolución"),
    ("Educación a Distancia (EaD)", "Tecnología y Herramientas"),
    ("Educación a Distancia (EaD)", "Rol del Docente"),
    ("Educación a Distancia (EaD)", "Aprendizaje Autónomo"),
    ("Educación a Distancia (EaD)", "Paradigma Educativo"),
    ("Educación a Distancia (EaD)", "Sociedad Digital"),
    ("Educación a Distancia (EaD)", "Desafíos y Perspectivas"),
    ("Historia y Evolución", "Surgimiento en el siglo XX"),
    ("Historia y Evolución", "De la correspondencia a las TIC"),
    ("Tecnología y Herramientas", "Plataformas virtuales"),
    ("Tecnología y Herramientas", "Herramientas digitales"),
    ("Tecnología y Herramientas", "E-pedagogía"),
    ("Rol del Docente", "Motivador y dinamizador"),
    ("Rol del Docente", "Creativo e innovador"),
    ("Rol del Docente", "Reflexivo y organizado"),
    ("Rol del Docente", "Uso de TIC y producción de conocimiento"),
    ("Rol del Docente", "Investigación y escritura"),
    ("Aprendizaje Autónomo", "Gestión del conocimiento"),
    ("Aprendizaje Autónomo", "Planificación y disciplina"),
    ("Aprendizaje Autónomo", "Autoevaluación y crítica"),
    ("Paradigma Educativo", "Cambio de lo presencial a lo virtual"),
    ("Paradigma Educativo", "Mediación pedagógica"),
    ("Paradigma Educativo", "Inclusión y calidad educativa"),
    ("Sociedad Digital", "Oportunidad formativa"),
    ("Sociedad Digital", "Conexión y aprendizaje en línea"),
    ("Sociedad Digital", "Cultura mediada por TIC"),
    ("Desafíos y Perspectivas", "Convergencia tecnológica y educación"),
    ("Desafíos y Perspectivas", "Pedagogías high tech"),
    ("Desafíos y Perspectivas", "Reorganización social y educativa"),
    ("Desafíos y Perspectivas", "Seguridad y privacidad"),
    ("Desafíos y Perspectivas", "Formación docente para el nuevo escenario"),
    ("Desafíos y Perspectivas", "Educación para la InfoCiudadanía"),
])

# Posiciones de los nodos
pos = nx.spring_layout(G)

# Dibujar el grafo
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=10, font_weight="bold", arrows=True, arrowstyle='-|>', arrowsize=20, edge_color="gray")
plt.title("Mapa Mental: Relación entre Epistemología y Pedagogía en la Educación a Distancia")
plt.show()
