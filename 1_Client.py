import socket

# Create UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a word (or type 'exit' to quit) : ")
    if message.lower() == 'exit':
        break

    # Send message to server
    client_socket.sendto(message.encode(), ('localhost', 8080))

    # Receive cipher text from server
    cipher_text, _ = client_socket.recvfrom(1024)
    print(f"Cipher Text from server : {cipher_text.decode()}")
