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
import numpy as np
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
EXTRA_TABLES_PATH       = MAIN_TABLES_PATH + "more_tables/" #GIT_PROJECT_PATH + "working_on_tables/"
#
GENES_PROTS_LENGTH_PATH =  base_path_in + "results/geneLength/"

# File names
############
STAT_G_FILE        = MAIN_TABLES_PATH + "stat_protCodGenes.tsv" 
STAT_P_FILE        = MAIN_TABLES_PATH + "stat_proteins.tsv"
STAT_MERGED_FILE   = MAIN_TABLES_PATH + "stat_merged.tsv"

G_NCBI_GENOME_DATA_FILE       = EXTRA_TABLES_PATH + "stat_protCodGenes_with_ncbiGenomeData.tsv"
WRONG_ANNOTATIONS_MERGED_FILE = EXTRA_TABLES_PATH + "noisy_stat_merged.tsv"



COLOR_FOR_DIST = {
    "genes":    matplotlib.colors.to_hex("#76bdfb", keep_alpha=False),
    "proteins": matplotlib.colors.to_hex("#ffab98", keep_alpha=False)
}
#
ORG_KINGDOMS            = ['archaea',  'bacteria', 'eukaryota']
COLOR_KINGDOMS          = ['#D83B01',  '#002050',   '#0078D7']
#
ORG_GROUPS       = ["bacteria", "archaea", "protists", "fungi", "plants",
                    "invertebrates", "vertebrates"]
COLOR_OF ={
    "bacteria": '#D83B01', "archaea": '#002050',
    "protists": '#FFA500', "fungi": '#A80000',
    "plants": '#107C10',
    "invertebrates": '#EF008C', "vertebrates": '#0078D7'
}
# Article colors
################
#ARTICLE_COLOR_ORG_GROUPS        = ['#F4B183', '#FFFFFF', '#FFF2CC', '#385723', '#9DC3E6',
#                                   '#D0A8CD', '#F997CE']
#ARTICLE_COLOR_BORDER_ORG_GROUPS = ['#D26E2A', '#000000', '#BF9000', '#A9D18E', '#3B64AD',
#                                   '#9664A0', '#C00000']
BOOL_USE_ARTICLE_COLORS = 0 # Apply borders for better results
if BOOL_USE_ARTICLE_COLORS:
    COLOR_OF = { # update to draft colors
        "bacteria": '#F4B183', "archaea": '#FFFFFF',
        "protists": '#FFF2CC', "fungi": '#9DC3E6',
        "plants": '#385723',
        "invertebrates": '#9664A0', "vertebrates": '#C00000'  #, '#B4009E'
    }

    
COLOR_ORG_GROUPS = []
for g in COLOR_OF:
    COLOR_ORG_GROUPS.append(COLOR_OF[g])




    
################################# alpha start    
# ALPHA: not in use at the moment
################################# 
ALPHA_OF ={
    "bacteria": 0.1, "archaea": 1.0,
    "protists": 1.0, "fungi": 0.1,
    "plants": 1.0,
    "invertebrates": 1.0, "vertebrates": 1.0
}
ALPHA_ORG_GROUPS = np.array(
    [ALPHA_OF["bacteria"], ALPHA_OF["archaea"],
     ALPHA_OF["protists"], ALPHA_OF["fungi"],
     ALPHA_OF["plants"],
     ALPHA_OF["invertebrates"], ALPHA_OF["vertebrates"]]
)
################################# alpha end




