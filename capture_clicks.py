import os
import time

from PIL import ImageGrab

# Definir a pasta onde as capturas de tela serão salvas
output_folder = "capturas"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def capture_screen(region):
    # Captura a região especificada da tela
    screenshot = ImageGrab.grab(bbox=region)
    timestamp = int(time.time())
    file_path = os.path.join(output_folder, f"screenshot_{timestamp}.png")
    screenshot.save(file_path)
    print(f"Captured screen and saved to {file_path}")

def on_click(x, y, button, pressed):
    if pressed:
        # Definir a região a ser capturada
        # Aqui, por exemplo, captura uma área de 100x100 pixels ao redor do clique
        region = (x - 830, y - 300, x - 170, y + 310)
        capture_screen(region)

if __name__ == "__main__":
    print("Pressione Ctrl+C para sair.")
    from pynput import mouse

    # Iniciar o listener de mouse
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
