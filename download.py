import gdown

# URL del archivo de Google Drive
url = 'https://drive.google.com/uc?id=1emEBEK2_Vnd4bntMcsEoAnhX8VF2Z3xr'

# Nombre con el que se guardará el archivo descargado
output = 'video.mp4'

# Descargar el archivo
gdown.download(url, output, quiet=False)
