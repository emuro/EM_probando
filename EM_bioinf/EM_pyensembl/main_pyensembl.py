import pyensembl
ensembl = pyensembl.EnsemblRelease(release=98)

genes = ensembl.genes_at_locus(contig="1", position=1000000)
print(genes)

genes_by_prot = ensembl.gene_by_protein_id("ENSP00000350283")
print(genes_by_prot)
