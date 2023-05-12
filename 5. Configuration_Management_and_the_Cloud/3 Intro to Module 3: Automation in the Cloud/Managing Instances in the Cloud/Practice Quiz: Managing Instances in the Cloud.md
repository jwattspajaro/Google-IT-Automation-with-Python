### ¡Felicitaciones! ¡Aprobaste!
#### Calificación recibida 100 %

1.
Pregunta 1
### What is templating?

1 / 1 punto

⚫ **The process of capturing the entire system configuration to enable us to reproduce virtual machines**


⚪ The process of copying virtual machines


⚪ The process of creating a new virtual machine instance


⚪ The process of testing configurations against known-working settings

    Correcto
    Way to go! Effective templating software allows you to capture an entire virtual machine configuration and use it to create new ones.

2.
Pregunta 2
### Why is it important to consider the region and zone for your cloud service?

1 / 1 punto

⚪ To follow local laws and regulations


T⚪ o avoid time zone discrepancy


⚪ To avoid language barriers


⚫ **To ensure bandwidth and reliability for users**

    ✅Correcto
    Right on! Generally, you're going to want to choose a region that is close to your users so that you can deliver better performance.

3.
Pregunta 3
### What option is used to determine which OS will run on the VM?

1 / 1 punto

⚪ Machine type


⚫ **Boot disk**


⚪ Region


⚪ Template

      ✅Correcto
      Woohoo! The boot disk from which the VM boots will determine what operating system runs on the VM.

4.
Pregunta 4
### When setting up a new series of VMs using a reference image, what are some possible options for upgrading services running on our VM at scale?

1 / 1 punto

🔲 Manually updating files via the command line


🔳 **Create a new reference image each update**

    ✅Correcto
    Nice job! One way of updating VM services at scale is to simply spin them up again with an updated reference image.


🔲 Editing parameters and uploading files individually through the web interface


🔳 **Use a configuration management system like Puppet**

      ✅Correcto
      Awesome! Puppet or other configuration management systems provide a streamlined way to deploy service updates at scale.

5.
Pregunta 5
### When using gcloud to manage VMs, what two parameters tell gcloud that a) we want to manage our VM resources and b) that we want to deal with individual VMs? (Check two)

1 / 1 punto

🔳 **compute**

     ✅ Correcto
      Way to go! The compute parameter tells gcloud that we are managing Compute Engine resources.


🔲 init


🔳 **instances**

      ✅Correcto
      Woohoo! The instances parameter that follows the compute parameter tells gcloud that we want to manage our VMs on the instance level.


create
