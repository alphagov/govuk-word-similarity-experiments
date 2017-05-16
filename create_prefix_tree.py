import difflib
from graphviz import Digraph

concepts = []

with open('output/lemmatised.txt') as f:
    for line in f:
        concepts.append(line.strip())

dot = Digraph("rankdir='LR'")

for concept in concepts:
    for other in concepts:
        if other != concept and other.startswith(concept):
            dot.edge(concept, other)

dot.render("output/prefix_tree")
