import difflib
from graphviz import Digraph

concepts = []

with open('output/lemmatised.txt') as f:
    for line in f:
        concepts.append(line.strip())

dot = Digraph("rankdir='LR'")

for concept in concepts:
    others = list(concepts)
    others.remove(concept)

    matches = difflib.get_close_matches(concept, others)
    for match in matches:
        dot.edge(concept, match)

dot.render("output/lemma_tree")
