#!/bin/bash

set -e

echo "Atualizando lista de pacotes..."
sudo apt update -y

echo "Instalando Docker..."
sudo apt install -y docker.io

echo "Instalando Docker Compose..."
sudo apt install -y docker-compose

echo "Clonando repositório FIWARE..."
git clone https://github.com/fabiocabrini/fiware

echo "Entrando no diretório..."
cd fiware

echo "Iniciando containers..."
sudo docker-compose up -d

echo "✔ FIWARE iniciado com sucesso!"
