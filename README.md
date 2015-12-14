# Server_stress-testing_Python

Web server stress-testing tool written in Python.  
There are actually two versions of the tool, the basic version of the tool ("ddos.py") and the advanced version of the stress-testing tool ("ddos_commandline.py"), which receives the required arguments from the user at execution, e.g. "--destination 192.168.43.1".  

Features:  
   **1. Basic version:**  
    1. Easily accessible interface  
      1. User is asked for confirmation before starting the stress-testing    
      2. Review of variables -- destination, amount of threads, port 
      3. Guides the user through setting up the required variables 
    2. Clean interface  
      1. Built-in Exception-Handling  
      2. Messages with clear structures ("[+] IP set to: 192.168.43.1" for example)
        
  **2. Advanced version:**  
      2.1 Advanced interface   
        2.1.1 Arguments supplied at execution ("python ddos_commandline.py -d 192.168.43.1 -t 100000 -r "GET /images/logo.jpg HTTP/1.0" ")  
        2.1.2 Easily include the tool in your own script, e.g. write a script which automatically runs the program at startup  
      2.2 More customization  
        2.2.1 Use your own custom HTTP requests to stress-test your server with. A tip: use the HTTP POST method with login forms and long arguments for maximum processor load, so to speak: efficiency.  
  **3. Both versions:**  
      3.1 Maximum amount of processor efficieny  
        3.1.1 Via low-level socket programming  
        3.1.2 Tool does not let any threads go to waste via the reconnection of disconnected sockets  
      3.2 Large amount of power  
        3.2.1 No limit on number of threads  
        3.2.2 Custom HTTP requests for the maximum amount of processor and bandwidth load    
    
