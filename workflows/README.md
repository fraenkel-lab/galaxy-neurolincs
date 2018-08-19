# RNA-Seq Workflow Information

### Background

Our consortium defines data levels for each omics data type. For RNA-seq, those data `levels` are as follows:

| level1 | level2 | level3 | level4  |
|--------|--------|--------|---------|
| fastq  | bam    | counts | DEGenes |


Generally, each sample in the experiment will be represented by a single pair of fastqs, but we occasionally split samples across sequencing lanes in order to reduce batch effects which could arise from sequencing lanes crashing and whatnot. However, when a sample is split across lanes, each sample will yield more than a _single_ pair of fastqs.

When a sample is associated with a single pair of fastqs, it is possible to define a set of operations against those fastqs which yield a `level3` representation of that sample. However, when a sample is split across multiple fastqs, there is no way to automatically merge them to generate a single `level3` file for that sample.

In the context of RNA-seq, the options are as follows:
1.  Concatenate the pairs of fastqs which correspond to a single sample, then run the `level1` > `level3` workflow.
2.  Run a `level1` > `level2` workflow for each pair of fastqs, then merge each bam corresponding to a single sample, then run a `level2` > `level3` pipeline on the merged bam.
3.  Run a `level1` > `level3` workflow on each pair of fastqs, then sum the counts files.

In principle, these should yield equivalent results. And indeed when we tested each approach, they did. But each of these approaches has certain side-effects, especially in the case in which there truly is an issue with one of the sequencing lanes.

Option 1 above tacitly asserts that there will not be very much technical artifacting from each lane, and averaging across lanes removes any existing batch effects sufficiently well for our use case.
Contrarily, option 2 and 3 provide the ability to compare bams or counts files respectively for any given sample in order to check for lane-specific batch effects. Since we have good tooling for comparing and merging bam files (but less tooling for comparing and merging counts files) we decided to opt for option 2.

The trouble with this approach is that we had to split apart the `level1` > `level3` pipeline into a `level1` > `level2` pipeline and a `level2` > `level3` pipeline, with hand-operated bam-compare and bam-merge between those two workflows.

### Running the workflow

In order to process RNA-seq samples corresponding to any sample which has been split across sequencing lanes, we must:
- Prepare collections of pairs of fastqs in a Galaxy history.
- Run the `level1` > `level2` RNA-seq pipeline against that collection.
- bam-compare all bam files corresponding to a particular sample, looking for extremely high concordance.
- Assuming those bam files are nearly identical, bam-merge those bam files into a single bam file corresponding to the sample.
- Build a collection of sample-`level `bam files.
- Run the `level2` > `level3` RNA-seq pipeline against that collection, yielding final counts files.


<!-- # ATAC-seq Workflow -->







