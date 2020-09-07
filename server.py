import socket

 

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

 



 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPServerSocket2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))
#UDPServerSocket2.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

   

    m=message.decode()

    clientMsg = "Message from Client "+m[len(m)-1]+": "+m[0:len(m)-1]
    clientIP  = "Client IP Address: {}".format(address)

 
    
    print(clientMsg)
    #print(clientIP)


                                

    msgFromServer       = input("Enter your message for client "+m[len(m)-1]+": ")

    bytesToSend         = str.encode(msgFromServer)

                            

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)


