import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 1. Describe what the constants socket.AF_INET and socket.SOCK_STREAM are used for in the above line
    
    # 2. Add a line of code that invokes bind() to make the socket listen on 
    
    s.listen(5)
    while True:
        # 3. Uncomment and complete the next line of Python code such that it use the accept method to permit a new connection,
        # returning a tuple with a new (usable) socket and the IP/port of the client which connected to the server
        
        # conn, src =  
        
        print(f"New connection: {src}")
        
        # 4. Invoke the .recv method to read 4096 bytes from the socket into the variable 'data'
        
        # data = 
        
        print(data.decode())
        
        # 5. Is the method accept() a blocking function or non-blocking function? Explain why.
        
        # 6. If we wanted to truly permit multiple concurrent connections, we would need to allow multi-threading. Briefly explain how multi-threading could be used to this end.

