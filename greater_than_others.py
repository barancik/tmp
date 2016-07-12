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
from collections import defaultdict, Counter

systems=['CHIMERA_AFTER','CHIMERA_BEFORE','GT_AFTER','GT_BEFORE']
tms=['CHIMERA','GT']

def count_score(fil):
    wins = defaultdict(list)
    loses = defaultdict(list)
    chimera =  Counter()
    gt =  Counter()
    for idx in fil:
       if not idx:
           continue
       scores={s:int(fil[idx][s]) for s in systems if s in fil[idx]}
       if not scores:
           continue
       for s in scores:
           top = float(len([x for x in scores if scores[s] > scores[x]]))
           down = float(len([x for x in scores if scores[s] != scores[x]]))
           wins[s].append(top)
           loses[s].append(down)
       if scores['CHIMERA_AFTER'] < scores['CHIMERA_BEFORE']:
           chimera["AFTER"] += 1
       elif  scores['CHIMERA_AFTER'] > scores['CHIMERA_BEFORE']:
           chimera["BEFORE"] += 1
       else:
           chimera["TIES"] += 1 
       if scores['GT_AFTER'] < scores['GT_BEFORE']:
           gt["AFTER"] += 1
       elif scores['GT_AFTER'] > scores['GT_BEFORE']:
           gt["BEFORE"] += 1
       else:
           gt["TIES"] += 1
    return wins,loses,chimera,gt 

WINS = defaultdict(list)
LOSES = defaultdict(list)
CHIMERA =  Counter()
MOSES =  Counter()
    
for phil in glob.glob("*.log"):
    fil = json.load(open(phil,"r"))
    wins,loses,chimera,moses = count_score(fil)
    for system in systems:
        WINS[system].extend(wins[system])
        LOSES[system].extend(loses[system])
    CHIMERA += chimera
    MOSES += moses

for n in WINS.keys():    
    print n,sum(WINS[n])/sum(LOSES[n])

print MOSES, CHIMERA

#user based
for phil in glob.glob("*.log"):
    print phil
    fil = json.load(open(phil,"r"))
    wins,loses,chimera,gt = count_score(fil)
    print "Moses", chimera
    print "GT", gt
        
#source based
print "Source before"
CHIMERA =  Counter()
GT =  Counter()
for phil in glob.glob("*.log"):
    print phil
    print "Source before"
    fil = json.load(open(phil,"r"))
    #import pdb; pdb.set_trace()
    f = {x:fil[x] for x in fil if fil[x]["source"] == "SOURCE_BEFORE"}
    wins,loses,chimera,gt = count_score(f)
    CHIMERA += chimera
    GT += gt
print "Moses", CHIMERA
print "GT", GT

print "Source after"
CHIMERA =  Counter()
GT =  Counter()
for phil in glob.glob("*.log"):
    print phil
    print "Source before"
    fil = json.load(open(phil,"r"))
    #import pdb; pdb.set_trace()
    f = {x:fil[x] for x in fil if fil[x]["source"] == "SOURCE_AFTER"}
    wins,loses,chimera,gt = count_score(f)
    CHIMERA += chimera
    GT += gt
print "Moses", CHIMERA
print "GT", GT
