#!/usr/bin/python

import json
import random

FILENAMES={"SOURCE_BEFORE"  : "czech_before.txt",
           "SOURCE_AFTER"   : "czech_after.txt",
           "GT_BEFORE"      : "google_translate_original.txt",
           "GT_AFTER"       : "google_translate_after.txt",
           "CHIMERA_BEFORE" : "chimera_before.txt",
           "CHIMERA_AFTER"  : "chimera_after.txt"}

def process_file(filename):
   return [x.strip() for x in open(filename,"r")]

def create_json(files):
    out = []
    TRANSLATIONS=["GT_BEFORE","GT_AFTER","CHIMERA_BEFORE","CHIMERA_AFTER"]
    for i in range(100):
        for source in ["SOURCE_BEFORE", "SOURCE_AFTER"]:
            s = {"text":files[source][i], "file":source}
            random.shuffle(TRANSLATIONS)
            t = [{"text":files[tr][i], "file":tr} for tr in TRANSLATIONS]
            out.append({"id":i,"source":s,"translations":t})
    return out

FILES={}
PROCESSED=[]
for filename in FILENAMES:
    FILES[filename] = process_file(FILENAMES[filename])
    for files in FILES.values():
      if len(files) != 100:
        print "CHYBA"
        break
out = create_json(FILES)
import pdb; pdb.set_trace()


    
