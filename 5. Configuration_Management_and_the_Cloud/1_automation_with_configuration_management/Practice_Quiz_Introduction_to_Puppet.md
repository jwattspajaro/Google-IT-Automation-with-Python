✅ ### ¡Felicitaciones! ¡Aprobaste!
### Calificación recibida 100 %
#### Para Aprobar 80 % o más

#### Pregunta 1
A Puppet agent inspects /etc/conf.d, determines the OS to be Gentoo Linux, then activates the Portage package manager. What is the provider in this scenario?  

⚪ 1 punto

⚪ /etc/conf.d  


⚫ **Portage**


⚪ Gentoo Linux  


The Puppet agent  

### 2.
#### Pregunta 2
Which of the following examples show proper Puppet syntax?  

⚫ 1 punto
```python

class AutoConfig {
  package { 'Executable':
    ensure => latest,
  }
  file { 'executable.cfg':
    source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace => true,
  }
  service { 'executable.exe':
    enable  => true,
```
⚪
```python
class AutoConfig :
  package ''Executable':
    ensure => latest,
  
  file  'executable.cfg':
    source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace => true,
  
  service  'executable.exe':
    enable  => true,
```
⚪
```python
class AutoConfig {
  package { 'Executable':
    ensure == latest,
  }
  file { 'executable.cfg':
    source == 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace == yes,
  }
  service { 'executable.exe':
    enable  == yes,
```
⚪
```python
class AutoConfig {
  package { 'Executable':
    assure=> latest,
  }
  file { 'executable.cfg':
    origin=> 'puppet:///modules/executable/Autoconfig/executable.cfg'
    substitute=> true,
  }
  program{ 'executable.exe':
    activate => true,

```
3. ### Pregunta 3
#### What is the benefit of grouping resources into classes when using Puppet?

1 punto

⚪ Providers can be specified


⚫ **Configuration management is simplified**


⚪ The title is changeable


⚪ Packages are not required

4.
Pregunta 4
What defines which provider will be used for a particular resource?

1 punto

⚫ **Puppet assigns providers based on the resource type and data collected from the system.**


⚪ A menu allows you to choose providers on a case-by-case basis.


⚪ The user is required to define providers in a config file.


⚪ Puppet uses an internet database to decide which provider to use.

5.
Pregunta 5
In Puppet’s file resource type, which attribute overwrites content that already exists?

1 punto

⚪ Purge


⚪ Overwrite


⚪ Replace


⚪ Save

Código de ho
