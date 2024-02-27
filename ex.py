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
# All presidential briefs authored between 1962-10-16 and 1962-10-28 (Cuban Missle Crisis)
pdb_cmc = ("https://api.foiarchive.org/docs?"
           "select=doc_id,corpus,classification,authored,title,body,source&"
           "corpus=eq.briefing&authored=gte.1962-10-16&authored=lt.1962-10-28")
# Same date range, fewer data attributes, but reference Kruschev in text
pdb_ck = ("https://api.foiarchive.org/docs?"
           "select=doc_id,authored,title,source&"
           "corpus=eq.briefing&authored=gte.1962-10-16&authored=lt.1962-10-28&"
           "full_text=wfts.khrushchev")
# Multi-collection query of documents mentioning hussein and rumsfeld
drsh = ("https://api.foiarchive.org/docs?"
        "select=doc_id,corpus,authored,classification,title,body&"
        "wfts.hussein%20rumsfeld")


df = call_api(pdb_cmc)     # Try the others or your own
print(df)
