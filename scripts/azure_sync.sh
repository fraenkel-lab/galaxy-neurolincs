#!/bin/bash

VARS=('genomics', 'genomics_other', 'epigenomics', 'proteomics', 'transcriptomics')
SAS=''

for VAR in "${VARS[@]}"
do
        echo /pool/data/globus/$VAR

        azcopy sync "/pool/data/globus/$VAR" "https://thecdr.blob.core.windows.net/globus/$VAR?sv=2018-03-28&ss=b&srt=sco&sp=rwdlac&se=2018-12-31T08:15:22Z&st=2018-12-31T00:15:22Z&spr=https,http&sig=2Cf1rGEr%2FlOhP8aiOQ3xlJc8U%2BbhYugqimkrkR4LWXU%3D" --recursive=true
done

