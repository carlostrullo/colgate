import gdown

# URL del archivo de Google Drive
url = 'https://drive.google.com/uc?id=1XYZ1234567'

# Nombre con el que se guardará el archivo descargado
output = 'video.mp4'

# Descargar el archivo
gdown.download(url, output, quiet=False)
