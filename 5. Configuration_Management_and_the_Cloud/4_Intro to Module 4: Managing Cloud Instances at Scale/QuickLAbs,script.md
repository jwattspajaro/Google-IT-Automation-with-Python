### Procedimientos para la resolución de conflictos de puerto en Apache2
Primero, verifica el estado de Apache2. Si Apache2 falló al iniciar, es posible que otro proceso esté utilizando el puerto 80:

bash
Copy code
'''

        sudo systemctl status apache2
        
'''   
Intenta reiniciar Apache2:

bash
Copy code
'''

        sudo systemctl restart apache2
'''

Verifica nuevamente el estado de Apache2. Si sigue fallando, es posible que el puerto 80 esté siendo utilizado por otro proceso:

bash
Copy code
'''

        sudo systemctl status apache2
        
'''
Utiliza el comando netstat para encontrar qué procesos están escuchando en qué puertos:

bash
Copy code
'''

        sudo netstat -nlp
        
'''
Busca cuál programa python3 está utilizando el puerto 80:


Copy code
'''

    ps -ax | grep python3
    
'''
Si encuentras un programa python3 que está utilizando el puerto 80, puedes examinar su código con:


Copy code
'''

    cat /usr/local/bin/jimmytest.py
'''
Mata el proceso creado por /usr/local/bin/jimmytest.py. Reemplaza [process-id] con el PID del programa python3:


Copy code
'''

    sudo kill [process-id]
    
'''

**Lista los procesos nuevamente para verificar si el proceso que acabas de matar fue realmente terminado:**


Copy code
'''

    ps -ax | grep python3
    
'''

Verifica la disponibilidad de cualquier servicio con las palabras clave "python" o "jimmy":


Copy code
'''

    sudo systemctl --type=service | grep jimmy
    
'''

Detén y deshabilita el servicio:

Copy code
'''

    sudo systemctl stop jimmytest && sudo systemctl disable jimmytest
    
'''

Confirma que ningún proceso esté escuchando en el puerto 80:


Copy code
'''

    sudo netstat -nlp
    
'''

Finalmente, intenta iniciar Apache2 nuevamente:


Copy code
'''

    sudo systemctl start apache2
    
'''    
