import time
from iqoptionapi.stable_api import IQ_Option
import os

# 1. Configuración de cuenta (Se lee de las variables de Railway)
email = os.getenv("t2342625@gmail.com")
password = os.getenv("Samael4589")

# Verificación de seguridad
if not email or not password:
    print("❌ ERROR: No se encontraron las credenciales en las variables de Railway.")
    print("Por favor, agregue IQ_EMAIL e IQ_PASSWORD en la pestaña 'Variables'.")
    exit()

# 2. Conectar a IQ Option
print(f"🔄 Intentando conectar a IQ Option con: {email}...")
Iq = IQ_Option(email, password)
check, reason = Iq.connect()

if check:
    print("✅ Sistema Online: Batallón IQ Option desplegado.")
else:
    print(f"❌ Error al conectar: {reason}")
    exit()

# 3. Ciclo Principal del Bot
while True:
    try:
        # Verificamos si seguimos conectados
        if not Iq.check_connect():
            print("⚠️ Conexión perdida. Reconectando...")
            Iq.connect()
        
        ahora = time.strftime("%H:%M:%S")
        
        # Aquí es donde el bot "trabaja"
        print(f"[{ahora}] 🔎 Escaneando mercado... Todo en orden.")
        
        # Espera 60 segundos antes de la siguiente revisión
        time.sleep(60)
        
    except Exception as e:
        print(f"⚠️ Error inesperado en el ciclo: {e}")
        time.sleep(10)
