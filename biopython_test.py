import Bio
print(Bio.__version__)


"""
from Bio import SeqIO
help(SeqIO)
"""

from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print(my_seq)
my_seq1 = my_seq.complement()
print(my_seq1)
my_seq2 = my_seq.reverse_complement()
print(my_seq2)