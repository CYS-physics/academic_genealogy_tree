# used basic packages
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from tqdm import tqdm

from sickle import Sickle
#sickle = Sickle('http://etd.adm.unipi.it/ETD-db/NDLTD-OAI/oai.pl')    # NDLTD url

def harvest():
    sickle = Sickle('http://export.arxiv.org/oai2')           # ARXIV url

    records = sickle.ListRecords(metadataPrefix='oai_dc') # this gives the oai item iterator
    records.next()

    arxiv = df()


    index = ['creator', 'subject', 'contributor', 'publisher', 'date', 'identifier', 'language']

    for record in tqdm(records):
        data = record.raw
        a=data.split("<dc:")                   # data starts with <dc: title > information </dc:title~
        d = dict()
        for e in a:
            b = e.split(">")
            if b[0]in index:
                while b[0] in d.keys():          # to handle if a thesis has multiple contributor
                    b[0] += "1"
                else:
                    pass
            
                c = b[1].split("</dc")        # remove following data
                d[b[0]] = c[0]
            else:
                pass
        arxiv = arxiv.append(d, ignore_index=True)
    
    

# save file as csv

    arxiv.to_csv("arxiv.csv")
