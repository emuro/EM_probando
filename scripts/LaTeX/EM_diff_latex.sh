#!/bin/bash
#
# 1.-run LaTeX on the new LaTeX version
# 2.-generate differences with previous version
# 3.-run LaTeX on differences with previous version

# Force two imput parameters
print "EM_diff_LaTeX stem_of_original_LaTeX_file stem_of_new_LaTeX_file #not .tex" 
if [ $# -lt 2 ]; then
    print "EM_diff_LaTeX stem_of_original_LaTeX_file stem_of_new_LaTeX_file #not .tex" 
    exit 1
fi

# get original and last LaTeX' versions of the file
fi=${1:-'Methods'}
fo=${2:-'Methods_EM_v2'}
echo $fi
echo $fo
diffo='diff__'
diffo+=$fo
echo $diffo
#
fi_ext=$fi
fi_ext+='.tex'
fo_ext=$fo
fo_ext+='.tex'
diffo_ext=$diffo
diffo_ext+='.tex'


# run LaTeX new version
pdflatex $fo_ext
bibtex $fo
pdflatex $fo_ext
pdflatex $fo_ext

# difference with the original version
latexdiff $fi_ext $fo_ext > $diffo_ext

# run LaTeX of the differences
pdflatex $diffo_ext
bibtex $difoo
pdflatex $diffo_ext
pdflatex $diffo_ext


