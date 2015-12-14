# Server_stress-testing_Python

Web server stress-testing tool written in Python.  
There are actually two versions of the tool, the basic version of the tool ("ddos.py") and the advanced version of the stress-testing tool ("ddos_commandline.py"), which receives the required arguments from the user at execution, e.g. "--destination 192.168.43.1".  

Features:  
  **1. Basic version:**  
      **1.1 Easily accessible interface**  
         * User is asked for confirmation before starting the stress-testing    
         * Review of variables -- destination, amount of threads, port 
         * Guides the user through setting up the required variables   
     **1.2 Clean interface**  
      * Built-in Exception-Handling  
      * Messages with clear structures ("[+] IP set to: 192.168.43.1" for example)  
        
  **2. Advanced version:**  
      **2.1 Advanced interface**    
        * Arguments supplied at execution ("python ddos_commandline.py -d 192.168.43.1 -t 100000 -r "GET /images/logo.jpg HTTP/1.0" ")  
        * Easily include the tool in your own script, e.g. write a script which automatically runs the program at startup  
      **2.2 More customization**  
        * Use your own custom HTTP requests to stress-test your server with. A tip: use the HTTP POST method with login forms and long arguments for maximum processor load, so to speak: efficiency.  
  **3. Both versions:**  
      **3.1 Maximum amount of processor efficieny**  
        * Via low-level socket programming  
        * Tool does not let any threads go to waste via the reconnection of disconnected sockets  
      **3.2  Large amount of power**  
        * No limit on number of threads  
        * Custom HTTP requests for the maximum amount of processor and bandwidth load    
    
