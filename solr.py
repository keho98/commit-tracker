import sunburnt
import httplib2

SOLR_URL = "http://localhost:8983/solr"
h = httplib2.Http(cache="/var/tmp/solr_cache")
solr_interface = sunburnt.SolrInterface(url=SOLR_URL, http_connection=h)
