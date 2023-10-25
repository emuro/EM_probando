python3 ~/git/github/EM_probando/scripts/file_header.py ~/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv 1

grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | wc -l # to avoid the header
#
##col2: division_7
echo "---------------division_7"
cat /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f2 | sort | uniq -c        # c2, division_7 con header

##col3: species
echo "---------------species"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f3 | sort | uniq | wc -l   # diff species without header
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f3 | sort | uniq -c | sort -n | grep -P "\s+1\s" | wc -l  # uniq species
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f3 | sort | uniq -c | sort -n | grep -vP "\s+1\s" | wc -l # species names duplicated twice (checked visually)
#
#col32 :taxonomy_id
echo "---------------taxonomy_id"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f32 | sort -n | uniq | wc -l   # diff taxid without header
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f32 | sort -n | uniq -c | grep -P "\s+1\s" | wc -l  # taxid en 1 única entrada 
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f32 | sort -n | uniq -c | grep -Pv "\s+1\s" | wc -l  # taxid en varias entradas
# grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f32 | sort -n | uniq -c | grep -Pv "\s+1\s" | sort -n | more #ver las redundantes; explorar
#
#col34: Scientific name
echo "---------------Scientific name"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f34 | sort  | uniq | wc -l   # diff Scientific_names
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f34 | sort  | uniq -c | grep -P "\s+1\s" | wc -l  # taxid en 1 única entrada 
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f34 | sort  | uniq -c | grep -Pv "\s+1\s" | wc -l  # taxid en varias entradas
# grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f34 | sort | uniq -c | grep -Pv "\s+1\s" | sort -n | more #ver las redundantes; explorar
#
#col36: Lineage
echo "--------------- Lineage"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f36 | grep -P ";" | wc -l   # tiene lineage
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f36 | grep -Pv ";" | wc -l  # no tiene lineage o un nivel
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f36 | grep -Pv ";" | sort | uniq -c  # no tiene lineage o un nivel
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f36 | sort  | uniq | wc -l   # diff Lineages
#
#col37: division_4 (lineage)
echo "--------------- division_4(lineage)"
grep -v trunk_genes_path /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f37 | sort | uniq -c 

#
##col39: division_8 
echo "---------------division_8"
cat /home/emuro/git/github/borrador_v2/main_tables/stat_protCodGenes.tsv | cut -f39 | sort | uniq -c        # c39, division_8  con header


