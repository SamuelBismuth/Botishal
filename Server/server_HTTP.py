import socket

from botichal import chatbot

HOST, PORT = '', 8888


def from_http_question_to_hebrew(response):
    response = response.split('+');
    hebrew_answer = chr(int(response[0]))
    for i in range(1, len(response)):
        hebrew_answer += chr(int(response[i]))
    return hebrew_answer


def from_hebrew_to_http_response(response):
    http_answer = str(ord((response[0])))
    for i in range(1, len(response)):
        http_answer += '+' + str(ord((response[i])))
    return http_answer


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    request = str(request, 'utf-8')
    request = request[request.find("ST /") + 4:request.find("HTTP")]
    request = from_http_question_to_hebrew(request)
    answer = chatbot.get_response(request)
    answer = from_hebrew_to_http_response(str(answer))
    http_response = "HTTP/1.1 200 OK\n\n" + answer
    http_response = http_response.encode()
    client_connection.sendall(http_response)
    client_connection.close()
