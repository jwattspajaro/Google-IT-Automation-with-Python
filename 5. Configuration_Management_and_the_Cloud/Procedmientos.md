Acceder al módulo de paquetes: Primero necesitas ir al directorio donde se encuentra el módulo de paquetes que vas a modificar. El comando para hacer esto es:



**cd /etc/puppet/code/environments/production/modules/packages**

cd es el comando para cambiar de directorio en la terminal de Linux.

Ver el archivo init.pp: Este archivo contiene las reglas actuales para la instalación de paquetes. Puedes ver su contenido con el comando cat:

**cat manifests/init.pp**

cat es un comando que imprime el contenido de un archivo en la terminal.

Modificar los permisos del archivo init.pp: Antes de poder editar el archivo, necesitas cambiar sus permisos para que puedas escribir en él. El comando para hacer esto es:


**sudo chmod 646 manifests/init.pp**

sudo te permite ejecutar comandos con privilegios de superusuario, chmod cambia los permisos de un archivo, y 646 establece los permisos para que el propietario pueda leer y escribir el archivo, y el resto pueda leerlo.

Editar el archivo init.pp: Ahora puedes abrir el archivo en un editor de texto como nano para agregar las nuevas reglas:


**sudo nano manifests/init.pp**

nano es un editor de texto para la terminal. sudo es necesario aquí porque cambiaste los permisos del archivo para que solo el superusuario pueda escribir en él.

Agregar la regla para instalar golang: Dentro del editor, debes agregar el siguiente fragmento de código después de la entrada del recurso existente:


if $facts[os][family] == "Debian" {

  package { 'golang':
  
    ensure => installed,
    
  }
  
}


Este código verifica si el sistema operativo de la máquina es de la familia Debian, y si es así, asegura que el paquete golang esté instalado.

Agregar la regla para instalar nodejs: De manera similar, debes agregar la siguiente regla para instalar nodejs en las máquinas de la familia RedHat:


if $facts[os][family] == "RedHat" {
  package { 'nodejs':
    ensure => installed,
  }
}

Guarda los cambios y cierra el editor.

Verificar las reglas: Ahora necesitas verificar que las reglas funcionan correctamente. Para hacer esto, primero necesitas obtener la dirección IP de la máquina a la que te vas a conectar. El comando para hacer esto es:


gcloud compute instances describe linux-instance --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
Copia la dirección IP que este comando te da.

Conectarte a la otra máquina: Abre otra terminal y conéctate a la otra máquina usando SSH. El comando para hacer esto es:

ssh [usuario]@[dirección IP]
Donde [usuario] es tu nombre de usuario y [dirección IP] es la dirección
