import vlc
import time

# Esperar 3 segundos para iniciar el script después de que el escritorio esté visible
time.sleep(3)

# Ruta al video
video_path = "/path/to/your/video.mp4"

# Crear instancia de VLC y cargar el video
player = vlc.MediaPlayer(video_path)

# Configurar video para que se reproduzca en pantalla completa
player.set_fullscreen(True)

# Ocultar el cursor del mouse en el video
player.video_set_mouse_input(False)
player.video_set_key_input(False)

# Reproducir el video
player.play()

# Bucle infinito para mantener el video en reproducción continua
while True:
    time.sleep(1)  # Puedes ajustar este tiempo según sea necesario
    if player.get_state() == vlc.State.Ended:
        player.play()
