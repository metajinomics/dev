#!/usr/bin/pythn
import urllib
import ijson
import sys

def get_taxid(md5):
    try:
        url_string = "http://api.metagenomics.anl.gov//m5nr/md5/" + md5
        f = urllib.urlopen(url_string)
        objects = ijson.items(f, '')
        taxid = ""
        for item in objects:
            for x in item["data"]:
                if(x["source"] == "KEGG"):
                    taxid = x["ncbi_tax_id"]
                    break
        return taxid
    except KeyError:
        taxid = "null"
        return taxid
