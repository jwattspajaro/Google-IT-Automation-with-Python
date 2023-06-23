#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    """Verifica si el localhost está configurado correctamente"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    """Verifica la conectividad a Internet mediante una solicitud a Google"""
    request = requests.get("http://www.google.com")
    response = request.status_code
    return response == 200
