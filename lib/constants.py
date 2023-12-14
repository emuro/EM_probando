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

GIT_PROJECT_PATH        = os.path.dirname(__file__) + "/../" 
MAIN_TABLES_PATH        = GIT_PROJECT_PATH + "main_tables/"
#
GENES_PROTS_LENGTH_PATH =  base_path_in + "results/geneLength/"
#
STAT_G_FILE      = "stat_protCodGenes.tsv" 
STAT_P_FILE      = "stat_proteins.tsv"
STAT_MERGED_FILE = "stat_merged.tsv"

#
COLOR_FOR_DIST = {
    "genes":    matplotlib.colors.to_hex("#76bdfb", keep_alpha=False),
    "proteins": matplotlib.colors.to_hex("#ffab98", keep_alpha=False)
}

ORG_GROUPS       = ["bacteria", "archaea","protists", "plants", "fungi", "invertebrates", "vertebrates"]
ORG_KINGDOMS     = ['bacteria', 'archaea', 'eukaryota']
COLOR_ORG_GROUPS        = ['#F4B183', '#FFFFFF', '#FFF2CC', '#385723', '#9DC3E6', '#D0A8CD', '#F997CE']
COLOR_BORDER_ORG_GROUPS = ['#D26E2A', '#000000', '#BF9000', '#A9D18E', '#3B64AD', '#9664A0', '#C00000']
#
OLD_COLOR_ORG_GROUPS    = ['#D83B01', '#002050', '#A80000', '#FFA500', '#107C10',
                           '#EF008C', '#0078D7', '#B4009E']
