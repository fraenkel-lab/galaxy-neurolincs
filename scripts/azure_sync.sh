#!/bin/bash

VARS=('genomics', 'genomics_other', 'epigenomics', 'proteomics', 'transcriptomics')

for VAR in "${VARS[@]}"
do
        echo /pool/data/globus/$VAR

        azcopy sync --source /pool/data/globus/$VAR --destination https://thecdr.blob.core.windows.net/globus/$VAR --dest-key VfL34sl9bJ/zJ2J55NnHAJDt7me3va65REBl5YKYBh2Nzaz9KIJ5V8j1fPxUFc2UsGozrRPTHcDUd/ED1nA6/w==
done

