import graphviz

# Création d'un graphique
graph = graphviz.Digraph()

# Ajout des nœuds (les postes dans l'organigramme)
graph.node('CEO', 'PDG')
graph.node('CTO', 'Directeur Technique')
graph.node('CFO', 'Directeur Financier')
graph.node('HR', 'Responsable des Ressources Humaines')

# Ajout des relations entre les nœuds (les liens hiérarchiques)
graph.edge('CEO', 'CTO')
graph.edge('CEO', 'CFO')
graph.edge('CEO', 'HR')

# Affichage du graphique
graph.view()