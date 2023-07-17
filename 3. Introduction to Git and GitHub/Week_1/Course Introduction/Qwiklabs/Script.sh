#!/usr/bin/bash

# Instalar Git
sudo apt update
sudo apt install git -y
git --version

# Inicializar un nuevo repositorio
mkdir my-git-repo
cd my-git-repo
git init

# Configurar Git
git config --global user.name "Nombre"
git config --global user.email "usuario@ejemplo.com"

# Operaciones de Git
echo "Este es mi primer repositorio." > readme
git add readme
git commit -m "Este es mi primer commit."
echo "Un repositorio es un lugar donde se almacenan todos los archivos de un proyecto en particular." > readme
git diff readme
git add readme
git status
git commit -m "Este es mi segundo commit."
git log
