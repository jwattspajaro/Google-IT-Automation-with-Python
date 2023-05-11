#!/usr/bin/env bash
# Esta línea sirve para decirle al sistema que interprete el script usando Bash. 

echo $PATH
# Este comando imprime el valor actual de la variable de entorno PATH. PATH es una variable del sistema que contiene una lista de directorios en los que Bash busca comandos.

export PATH=/bin:/usr/bin
# Esta línea redefine la variable de entorno PATH para que sólo contenga los directorios /bin y /usr/bin. Esto puede ser útil para asegurarse de que sólo se estén usando las herramientas básicas del sistema.

cd /etc/puppet/code/environments/production/modules/profile/manifests
# Este comando cambia el directorio de trabajo actual al directorio especificado, que parece ser donde se almacenan los manifiestos del módulo de perfil en un entorno de producción de Puppet.

sudo nano init.pp
# Este comando abre el archivo init.pp en el editor de texto Nano con privilegios de superusuario. Puede ser que estés editando un archivo de configuración de Puppet.

sudo puppet agent -v --test
# Este comando ejecuta Puppet Agent con privilegios de superusuario. La opción -v habilita la salida detallada (verbose) y la opción --test permite ejecutar el agente en modo de prueba, lo que significa que se aplicarán las configuraciones pero no se instalarán en el sistema como una configuración permanente.

echo $PATH
# Finalmente, este comando imprime el valor de la variable PATH de nuevo. Esto podría ser útil para comprobar que la variable PATH ha vuelto a su valor original después de ejecutar el script.
