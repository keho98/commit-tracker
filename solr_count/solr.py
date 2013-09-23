import sunburnt
import httplib2

SOLR_URL = "http://localhost:8983/solr"
h = httplib2.Http(cache="/var/tmp/solr_cache")
solr_interface = sunburnt.SolrInterface(url=SOLR_URL, http_connection=h)

document = {"id":"0553573403",
            "cat":"book",
            "name":"A Game of Thrones",
            "price":7.99,
            "inStock": True,
            "author_t":
            "George R.R. Martin",
            "series_t":"A Song of Ice and Fire",
            "sequence_i":1,
            "genre_s":"fantasy"}

solr_interface.add(document)
