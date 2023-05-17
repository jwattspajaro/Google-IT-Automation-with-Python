Enviar el correo electrónico a través de un servidor SMTP
Como mencionamos, para enviar correos electrónicos, nuestras computadoras usan el Protocolo simple de transferencia de correo (SMTP) . Este protocolo especifica cómo las computadoras pueden enviarse correos electrónicos entre sí. Hay ciertos pasos que deben seguirse para hacer esto correctamente. Pero, como de costumbre, no lo haremos manualmente; enviaremos el mensaje utilizando el módulo Python smtplib incorporado . Comencemos importando el módulo.

    import smtplib

Con smtplib, crearemos un objeto que representará nuestro servidor de correo y manejará el envío de mensajes a ese servidor. Si está utilizando una computadora con Linux, es posible que ya tenga un servidor SMTP configurado como postfix o sendmail. Pero tal vez no. Vamos a crear un objeto smtplib.SMTP e intentar conectarnos a la máquina local.

      mail_server = smtplib.SMTP('localhost')
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      (...We deleted a bunch of lines here...)
        
ConnectionRefusedError: [Errno 61] Connection refused
¡Ups! Este error significa que no hay un servidor SMTP local configurado. ¡Pero no entres en pánico! Todavía puede conectarse al servidor SMTP para su dirección de correo electrónico personal. La mayoría de los servicios de correo electrónico personal tienen instrucciones para enviar correo electrónico a través de SMTP; simplemente busque el nombre de su servicio de correo electrónico y "Configuración de conexión SMTP".

Al configurar esto, hay un par de cosas que probablemente deba hacer: Use una capa de transporte segura y autentíquese en el servicio con un nombre de usuario y una contraseña. Veamos qué significa esto en la práctica.

Puede conectarse a un servidor SMTP remoto utilizando Transport Layer Security (TLS) . Una versión anterior del protocolo TLS se denominaba Capa de sockets seguros (SSL) y, a veces, verá que TLS y SSL se usan indistintamente. Este SSL/TLS es el mismo protocolo que se usa para agregar una capa de transmisión segura a HTTP, convirtiéndolo en HTTPS. Dentro de smtplib, hay dos clases para realizar conexiones a un servidor SMTP: la clase SMTP realizará una conexión SMTP directa y la clase SMTP_SSL realizará una conexión SMTP a través de SSL/TLS. Como esto:

    mail_server = smtplib.SMTP_SSL('smtp.example.com')
    
Si desea ver los mensajes SMTP que el módulo smtplib envía y recibe en segundo plano, puede establecer el nivel de depuración en el objeto SMTP o SMTP_SSL. Los ejemplos de esta lección no mostrarán el resultado de la depuración, ¡pero puede que le resulte interesante!

    mail_server.set_debuglevel(1)
    
Ahora que hemos realizado una conexión con el servidor SMTP, lo siguiente que debemos hacer es autenticarnos en el servidor SMTP. Por lo general, los proveedores de correo electrónico quieren que proporcionemos un nombre de usuario y una contraseña para conectarse. Pongamos la contraseña en una variable para que no sea visible en la pantalla.

    import getpass
    mail_pass = getpass.getpass('Password? ')
    Password?

El ejemplo anterior usa el módulo getpass para que los transeúntes no vean la contraseña en la pantalla. Sin embargo, ten cuidado; ¡la variable mail_pass sigue siendo solo una cadena ordinaria!

    print(mail_pass)
    It'sASecr3t!
  
Ahora que tenemos el usuario de correo electrónico y la contraseña configurados, podemos autenticarnos en el servidor de correo electrónico utilizando el método de inicio de sesión del objeto SMTP .

     mail_server.login(sender, mail_pass)
    (235, b'2.7.0 Accepted')
  
Si el intento de inicio de sesión tiene éxito, el método de inicio de sesión devolverá una tupla del código de estado SMTP y un mensaje que explica el motivo del estado. Si falla el intento de inicio de sesión, el módulo generará una excepción SMTPAuthenticationError .

Si escribiera un script para enviar un mensaje de correo electrónico, ¿cómo manejaría esta excepción?


Enviando tu mensaje
¡Está bien! Estamos conectados y autenticados al servidor SMTP. Ahora, ¿cómo enviamos el mensaje?

    mail_server.send_message(message)
{}
De acuerdo, bueno, ¡eso último fue bastante fácil! ¡Primero hicimos la parte difícil! El método send_message devuelve un diccionario de los destinatarios que no pudieron recibir el mensaje. Nuestro mensaje se entregó con éxito, por lo que send_message devolvió un diccionario vacío. Finalmente, ahora que se envió el correo electrónico, cerremos la conexión con el servidor de correo.

    mail_server.quit()
  
¡Y ahí lo tienes! Cubrimos mucho en esta lección, ¡así que recapitulemos! Primero, construimos un mensaje de correo electrónico utilizando la clase EmailMessage del módulo de correo electrónico incorporado . A continuación, agregamos un archivo adjunto a nuestro mensaje con la ayuda del módulo integrado de mimetypes . Finalmente, nos conectamos a un servidor SMTP y enviamos el correo electrónico utilizando la clase SMTP_SSL del módulo smtplib .

¿Tenías idea de que todo esto estaba sucediendo detrás de un simple mensaje de correo electrónico?
