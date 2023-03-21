from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
Phylo.draw_ascii(tree)
print(tree.rooted)
Phylo.draw(tree)
