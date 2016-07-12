#!/usr/bin/python

# Script for counting system score from relative score 
# using the "> others" method, i.e. wins/(wins+loses)

#Official WMT12 score, used in WMT14 Parmesan article

# Needs following input:
# cat results.csv | grep English,Czech | cut -d',' -f8,10,12,14,16-
# automatic calling for all languages from extract_scores.sh


import glob
import sys
import json
from nltk.metrics.agreement import AnnotationTask
from collections import defaultdict, Counter

systems=['CHIMERA_AFTER','CHIMERA_BEFORE','GT_AFTER','GT_BEFORE']
tms=['CHIMERA','GT']

def get_voting(phil):
    coder = phil[:-4]
    results = []
    fil = json.load(open(phil,"r"))
    for idx in fil:
         scores={s:int(fil[idx][s]) for s in systems if s in fil[idx]}
         if not scores:
             continue
         for mt in tms:
             task=idx+mt[:1]
             if scores[mt+"_AFTER"] < scores[mt+"_BEFORE"]:
                 results.append((coder,task,"a"))
                 print coder, task, "A"
             elif scores[mt+"_AFTER"] > scores[mt+"_BEFORE"]:
                 results.append((coder,task,"b"))
                 print coder, task, "B"
             else:
                 results.append((coder,task,"t"))
                 print coder, task, "C"
    return results

print "Source after"
scores = []
for phil in glob.glob("*.log"):
    scores.extend(get_voting(phil))
    
t = AnnotationTask(scores)

#import pdb; pdb.set_trace()

