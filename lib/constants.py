# python3
# ################################################################## #
# constants.py (C) 2023 Mainz.
# Author: Enrique M. Muro
# ################################################################## #
#
# ------------------------------------------------------------------------
# Project: gene_length
#
# Purpose: Constants used in the project
# ################################################################## #

import os
import matplotlib
import sys


system = list(os.uname())[0]
if system == 'Linux':
    base_path_in = "/media/emuro/Nubya/"
elif system == 'Darwin':
    base_path_in = "/Volumes/Nubya/" # or Wes

# Paths
#######
GIT_PROJECT_PATH        = os.path.dirname(__file__) + "/../" 
MAIN_TABLES_PATH        = GIT_PROJECT_PATH + "main_tables/"
#
EXTRA_TABLES_PATH       = GIT_PROJECT_PATH + "working_on_tables/"
#
GENES_PROTS_LENGTH_PATH =  base_path_in + "results/geneLength/"

# File names
############
STAT_G_FILE        = MAIN_TABLES_PATH + "stat_protCodGenes.tsv" 
STAT_P_FILE        = MAIN_TABLES_PATH + "stat_proteins.tsv"
STAT_MERGED_FILE   = MAIN_TABLES_PATH + "stat_merged.tsv"

G_NCBI_GENOME_DATA_FILE       = EXTRA_TABLES_PATH + "stat_protCodGenes_with_ncbiGenomeData.tsv"
WRONG_ANNOTATIONS_MERGED_FILE = EXTRA_TABLES_PATH + "noisy/noisy_stat_merged.tsv"

#
COLOR_FOR_DIST = {
    "genes":    matplotlib.colors.to_hex("#76bdfb", keep_alpha=False),
    "proteins": matplotlib.colors.to_hex("#ffab98", keep_alpha=False)
}

ORG_GROUPS       = ["bacteria", "archaea","protists", "plants", "fungi",
                    "invertebrates", "vertebrates"]
#OLD_COLOR_ORG_GROUPS    = ['#D83B01', '#002050', '#A80000', '#FFA500', '#107C10',
#                           '#EF008C', '#0078D7', '#B4009E']
OLD_COLOR_ORG_GROUPS    = ['#D83B01', '#002050', '#A80000', '#FFA500', '#107C10',
                           '#EF008C', '#0078D7', '#B4009E']
# article colors
COLOR_ORG_GROUPS        = ['#F4B183', '#FFFFFF', '#FFF2CC', '#385723', '#9DC3E6',
                           '#D0A8CD', '#F997CE']
COLOR_BORDER_ORG_GROUPS = ['#D26E2A', '#000000', '#BF9000', '#A9D18E', '#3B64AD',
                           '#9664A0', '#C00000']


ORG_KINGDOMS            = ['archaea',  'bacteria', 'eukaryota']
COLOR_KINGDOMS          = ['#D83B01',  '#002050',  '#4475B4']

