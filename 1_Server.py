import socket

# Caesar cipher function
def caesar_cipher(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shift_char = shift_char.upper()
            encrypted += shift_char
        else:
            encrypted += char
    return encrypted

# Create UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8080))
print("Server is listening...")

while True:
    message, client_addr = server_socket.recvfrom(1024)
    message = message.decode()

    print(f"Received message: {message}")

    # Encrypt the message using Caesar Cipher with a shift of 3
    encrypted_message = caesar_cipher(message, 3)

    # Send the encrypted message back to the client
    server_socket.sendto(encrypted_message.encode(), client_addr)

    print(f"Sent encrypted message : {encrypted_message}")
