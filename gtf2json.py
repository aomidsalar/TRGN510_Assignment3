#!/usr/bin/python
import re
import sys
import fileinput
import json
import requests

gene_file=sys.argv[1]
gene_data=[]
homo_sapiens={}
for each_line_of_text in fileinput.input(gene_file):
    gene=re.findall(r'^.*?\t.*?\t(gene)\t', each_line_of_text, re.I)
    geneName=re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)[0]
    chrNumber=re.findall(r'(^.*?)\t', each_line_of_text, re.I)[0]
    startPos=re.findall(r'^.*?\t.*?\t.*?\t(.*?)\t', each_line_of_text, re.I)[0]
    endPos=re.findall(r'^.*?\t.*?\t.*?\t.*?\t(.*?)\t', each_line_of_text, re.I)[0]
    if gene:
        homo_sapiens = {"geneName": geneName, "chr": chrNumber, "startPos": int(startPos), "endPos": int(endPos)}
        gene_data.append(homo_sapiens)
json_objects=json.dumps(gene_data)
print(json_objects)
fileinput.close()
