from Bio import SeqIO
import requests
import gzip
from io import BytesIO

# URL del archivo FASTA comprimido en gzip
url = "https://ftp.uniprot.org/pub/databases/uniprot/"
url += "current_release/knowledgebase/reference_proteomes/Eukaryota/UP000005640/"
url += "UP000005640_9606.fasta.gz"

# Descargar el archivo comprimido en formato gzip desde la URL
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Cargar el contenido en BytesIO para que actúe como un archivo en memoria
    gzip_io = BytesIO(response.content)
    
    # Descomprimir el archivo gzip en memoria y leer el contenido FASTA
    with gzip.open(gzip_io, "rt") as fasta_io:
        for record in SeqIO.parse(fasta_io, "fasta"):
            print(f"ID: {record.id}")
            print(f"Secuencia: {record.seq}")
            print(f"Descripción: {record.description}")
else:
    print(f"No se pudo acceder al archivo. Código de estado HTTP: {response.status_code}")
