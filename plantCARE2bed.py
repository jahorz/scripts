# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:25:27 2023

@author: Jakob Horz. j.horz@tu-bs.de

This script turns a tab-delimited PLANTCare results file into a BED file which can be viewed in IGV

PLANTCare:
https://bioinformatics.psb.ugent.be/webtools/plantcare/html/

"""

def Plantcare_to_BED(plantcare_file, output_file):
    #read information from the plantcare file and write it local lists
    with open(plantcare_file, "r") as IN:
        line = IN.readline()
        ctg_ls = []
        motiftype_ls = []
        motifstart_ls = []
        motifend_ls = []
        strand_ls = []
        while line:
            region = line.split("\t")[0]
            ctg = region.split("_")[0] + "_" + region.split("_")[1]
            motiftype = line.split("\t")[1]
            motifstart = int(line.split("\t")[3]) + int(region.split("_")[2])
            motifend = round(float(line.split("	")[4])) + motifstart
            strand = line.split("\t")[5]
            ctg_ls.append(ctg)
            motifstart_ls.append(motifstart)
            motifend_ls.append(motifend)
            if motiftype == "":
                motiftype_ls.append("n/a")
            else:
                motiftype_ls.append(motiftype)
            strand_ls.append(strand)
            line = IN.readline()
        IN.close()
    
    #construct bed file from the information stored in the lists
    with open(output_file, "w") as OUT:
        for i in range(len(ctg_ls)):
            line_out = ctg_ls[i] \
            + "\t" + str(motifstart_ls[i]) \
            + "\t" + str(motifend_ls[i]) \
            + "\t" + motiftype_ls[i] \
            + "\t" + "500" \
            + "\t" + str(strand_ls[i]) \
            + "\t" + str(motifstart_ls[i]) \
            + "\t" + str(motifend_ls[i]) \
            + "\t" + "255,0,0" \
            + "\n"
            OUT.write(line_out)
            
        OUT.close
        
plantcare_file = "PATH/TO/PLANT/CARE/file.tab"
output_file = "PATH/TO/OUTPUT/file.bed"

Plantcare_to_BED(plantcare_file, output_file)