import socket, cv2, pickle, struct

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "0.0.0.0"
port = 7077

sever_socket.bind((host_ip, port))

sever_socket.listen()
print('Listening...')


session, addr = sever_socket.accept()
print('Connected')
if session:
    camera = cv2.VideoCapture(0)

    while(camera.isOpened()):
        ret, frame = camera.read()
        data = pickle.dumps(frame)
        data = struct.pack('Q', len(data)) + data
        try :
            session.sendall(data)
        except:
            session.close()

        cv2.imshow('Server', frame)
        if cv2.waitKey(10) == 13:
            session.close()
            break
        
    cv2.destroyAllWindows()