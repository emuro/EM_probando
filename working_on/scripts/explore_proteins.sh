python3 ~/git/github/EM_probando/scripts/file_header.py ~/git/github/borrador_v2/main_tables/stat_proteins.tsv 1

grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_proteins.tsv | wc -l # to avoid the header


##col1: species
echo "---------------species"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_proteins.tsv | cut -f1 | sort | uniq | wc -l   # diff species without header

##col2: proteome_id
echo "---------------proteome_id"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_proteins.tsv | cut -f2 | sort | uniq | wc -l   # diff 

#
#col3 :taxonomy_id
echo "---------------taxonomy_id"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_proteins.tsv | cut -f3 | sort -n | uniq | wc -l   # diff taxid without header

#
#col4 : superregnum
echo "---------------superregnum"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_proteins.tsv | cut -f4 | sort -n | uniq -c

exit
echo "Not reaching this line"




