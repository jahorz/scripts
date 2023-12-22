# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:26:46 2023

@author: jakob
"""

"""

works on BLAST table output format 6. 
!!!    Make sure to parse flag -outfmt 6 for BLAST run  !!!

Also put "_x" at the end of primer name in your FASTA input file. Where x = length of primer


blastn \
-query PATH/TO/QUERY/file.fasta \
-subject PATH/TO/SUBJECT/file.fasta \
-out PATH/TO/OUTPUT/file.txt \
-word_size 4 \
-evalue 1000 \
-dust no \
-soft_masking false \
-penalty -3 \
-reward 1 \
-gapopen 5 \
-gapextend 2 \
-outfmt 6 &


"""
#Collects BLAST hits and stores in lists locally
def get_PCR_fragments(blast_results):
    contig = []
    subject_start = []
    subject_end = []
    primer_name = []

    with open(blast_results, "r") as blast:
        line = blast.readline()
        while line:
            if int(line.split("\t")[0].split("_")[-1]) -3 <= int(line.split("\t")[7]):                                             
                contig.append(line.split("\t")[1])
                subject_start.append(line.split("\t")[8])
                subject_end.append(line.split("\t")[9])
                primer_name.append(line.split("\t")[0])
            line = blast.readline()
    blast.close
 
    
    c = 0
    fragment = []
    primer_hits = []
    fragment_site = []
    igv_prompt = []
    for i in range(len(contig)):
        orientation_i = subject_start[i] < subject_end[i]
        for s in range(c, len(contig)):
            #checks if primers are oriented towards each other on opposing strands 
            orientation_s = subject_start[s] < subject_end[s]
            if contig[i] == contig[s] and orientation_i != orientation_s:
                if orientation_i == True:
                    size = int(subject_start[s]) - int(subject_start[i])
                    fragment_site = str(subject_start[i]) + "-" + str(subject_start[s])
                else:
                    size = int(subject_start[i]) - int(subject_start[s])
                    fragment_site = str(subject_start[s]) + "-" + str(subject_start[i])
                    
                #choose cutoff values for the desired fragment size
                if 20 < size < 1400:
                    fragment.append(size)
                    primer_hits.append(str(size) + " bp \t" + primer_name[i] + " " + primer_name[s] +" " +  contig[i])
                    igv_prompt.append(contig[i] + ":" + fragment_site)
        
        c = c+1
        
    return primer_hits, igv_prompt
#Filter the initial fragments for the provided primer IDs 
def primer_pairs(primer_hits, primer1, primer2):
    filtered_fragments = []
    for i in range(len(primer_hits)):
        if primer1 in primer_hits[i].split("\t")[1].split(" ")[0] \
        and primer2 in primer_hits[i].split("\t")[1].split(" ")[1] \
        or primer2 in primer_hits[i].split("\t")[1].split(" ")[0] \
        and primer1 in primer_hits[i].split("\t")[1].split(" ")[1] \
        or primer1 in primer_hits[i].split("\t")[1].split(" ")[0] \
        and primer1 in primer_hits[i].split("\t")[1].split(" ")[1] \
        or primer2 in primer_hits[i].split("\t")[1].split(" ")[0] \
        and primer2 in primer_hits[i].split("\t")[1].split(" ")[1]:
            
            
            filtered_fragments.append(primer_hits[i])
            
    return filtered_fragments
    

blast_results = "PATH/TO/BLAST/results.txt"

primer1 = "Primer1_ID"
primer2 = "Primer2_ID"

primer_hits, igv_prompt= get_PCR_fragments(blast_results)
for i in range(len(primer_hits)):
    print(primer_hits[i] + "\t" +igv_prompt[i])


print("### selection")

selection = primer_pairs(primer_hits, primer1, primer2)    
for i in selection:
    print(i)
