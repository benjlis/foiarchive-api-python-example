"""Shows how to query FOIArchive REST API."""
import requests
import pandas as pd


def call_api(api_url):
    """Call api_url and return results in a dataframe."""
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print(f'{response.status_code} returned by {api_url}')


#
# Some queries expressed as API endpoints
#
# All PDBs authored 1962-10-16 and 1962-10-28 (Cuban Missle Crisis)
pdb_cmc = ("https://api.foiarchive.org/docs?"
           "select=doc_id,corpus,classification,authored,title,body,source&"
           "corpus=eq.pdb&authored=gte.1962-10-16&authored=lt.1962-10-28")
# Same date range, fewer data attributes, but reference Kruschev in text
pdb_cnk = ("https://api.foiarchive.org/docs?"
           "select=doc_id,authored,title,source&"
           "corpus=eq.pdb&authored=gte.1962-10-16&authored=lt.1962-10-28&"
           "full_text=wfts.khrushchev")
# Multi-collection query of documents mentioning hussein and rumsfeld
drsh = ("https://api.foiarchive.org/docs?"
        "select=doc_id,corpus,authored,classification,title,body,"
        "persons(full_name),countries(country_name)&"
        "wfts.hussein%20rumsfeld")
# Documents referencing Haiti authored since Oct 1, 2012
haitir = ("https://api.foiarchive.org/countries?country_name=eq.Haiti&"
          "select=docs(doc_id,authored,classification,title)&"
          "docs.authored=gt.2012-10-01")


df = call_api(pdb_cmc)     # Try the others or your own
print(df)
