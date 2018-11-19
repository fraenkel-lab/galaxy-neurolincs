#!/bin/bash

VARS=('genomics', 'genomics_other', 'epigenomics', 'proteomics', 'transcriptomics')
SAS=''

for VAR in "${VARS[@]}"
do
        echo /pool/data/globus/$VAR

        azcopy sync "/pool/data/globus/$VAR" "https://thecdr.blob.core.windows.net/globus/$VAR?sv=2017-11-09&ss=bfqt&srt=sco&sp=rwdlacup&se=2018-12-04T11:55:38Z&st=2018-11-19T03:55:38Z&spr=https&sig=caICNa0ugfSixq4%2B1TkM2wSMMKiQNKu6SGr50loIa9I%3D" --recursive=true
done

