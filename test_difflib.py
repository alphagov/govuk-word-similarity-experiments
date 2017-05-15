import difflib
from graphviz import Digraph

terms = []

with open('output/terms.txt') as f:
    for line in f:
        terms.append(line.strip())

dot = Digraph()

for term in terms:
    other_words = list(terms)
    other_words.remove(term)
    matches = difflib.get_close_matches(term, other_words)
    for match in matches:
        dot.edge(term, match)

dot.render("output/graph")
