# https://www.uniprot.org/help/api_queries
curl -H "Accept: text/plain; format=fasta" "https://rest.uniprot.org/uniprotkb/search?query=reviewed:true+AND+organism_id:9606+AND+Gene:PTEN"
