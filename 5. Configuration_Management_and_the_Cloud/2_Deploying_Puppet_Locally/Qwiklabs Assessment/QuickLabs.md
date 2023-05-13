Procedimientos para la Instalación de Paquetes y Configuración en Puppet
1. Instalación de Paquetes
Primero, navega a la carpeta packages en el directorio de módulos de Puppet:

Copy 
```
    cd /etc/puppet/code/environments/production/modules/packages
```
Luego, cambia los permisos del archivo manifests/init.pp para poder editarlo:

Copy 
```
    sudo chmod 646 manifests/init.pp
    
output    
    class packages {

    package { 'python-requests':
        ensure => installed,
    }


```

Copy 
```
Abre el archivo manifests/init.pp con nano (o tu editor de texto preferido) para editarlo:
```
Copy 
```

    nano manifests/init.pp
```
Copy 
Ejecuta el siguiente comando para obtener la dirección IP externa de la instancia de VM:

Copy 
```
    gcloud compute instances describe linux-instance --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
```

2. Acceder a la Instancia de VM

**Abre una nueva terminal y usa SSH para conectarte a la instancia de VM. Asegúrate de reemplazar <XXXXX.pem>, <username> y <external Ip Address> con la ruta a tu archivo de clave SSH, tu nombre de usuario y la dirección IP externa que obtuviste anteriormente, respectivamente:**

Copy 
```
    ssh -i <XXXXX.pem> <username>@<external Ip Address>

```
Una vez que estés en la instancia de VM, ejecuta el agente de Puppet para aplicar cualquier cambio que hayas hecho:

Copy 
```
    sudo puppet agent -v --test
 
```
Verifica la política de instalación de Go con el siguiente comando:

Copy 
```
    apt policy golang

```  
3. Obtención de Información de la Máquina
Regresa a la terminal de Puppet y navega a la carpeta machine_info:

Copy 
```
    cd /etc/puppet/code/environments/production/modules/machine_info

```  
Cambia los permisos del archivo manifests/init.pp para poder editarlo:

Copy 
```
    sudo chmod 646 manifests/init.pp

```
Abre el archivo manifests/init.pp con nano para editarlo:

Copy 
```
    nano manifests/init.pp
 
```  
4. Uso de Plantillas de Puppet
Cambia los permisos del archivo info.erb en la carpeta templates:

Copy 
```  
    sudo chmod 646 templates/info.erb
De nuevo en la instancia de VM, ejecuta el agente de Puppet para aplicar los cambios:

Copy 
```
    sudo puppet agent -v --test

```
Comprueba que la información de la máquina se ha guardado correctamente:

Copy 
```
    cat /tmp/machine_info.txt

  ```
5. Reinicio de la Máquina
Primero, crea el directorio reboot/manifests en la carpeta de módulos:

Copy 
```
    sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests
 
```
Navega a este nuevo directorio:

Copy 
```
    cd /etc/puppet/code/environments/production/modules/reboot/manifests

```
Crea y edita el archivo init.pp:

Copy 
```
    sudo nano init.pp
 
```
Crea y edita el archivo site.pp en el directorio manifests:

Copy 
```
    sudo nano /etc/puppet/code/environments/production/manifests/site.pp
 
```
Finalmente, ejecuta el agente de Puppet para aplicar los cambios:
Copy 
```
sudo puppet agent -v --test

```
``
