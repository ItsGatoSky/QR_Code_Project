#Importando las librerías adicionales para el proyecto
from datetime import datetime

import pymysql
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Configurar el acceso a la base de datos
DB_SERVER ='centroagsapo.mysql.database.azure.com'
DB_NAME = 'dbvideojuegos'
DB_USER = 'utede'
DB_PASSWORD = 'utede2025'
DB_PORT = 3306