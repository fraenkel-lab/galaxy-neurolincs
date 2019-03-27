#!/bin/bash

VARS=('genomics', 'genomics_other', 'epigenomics', 'proteomics', 'transcriptomics')
SAS='?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-01-24T12:29:46Z&st=2019-01-18T04:29:46Z&spr=https&sig=Rc5STU8Km5mUL5uhu9Qls5%2FqdxxTjyHw3%2FY%2FNIO6VtQ%3D'

for VAR in "${VARS[@]}"
do
        echo /pool/data/globus/$VAR

        azcopy sync "/pool/data/globus/$VAR" "https://thecdr.blob.core.windows.net/globus/$VAR$SAS" --recursive=true
done

