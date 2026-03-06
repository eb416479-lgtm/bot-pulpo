import os
import sys
import subprocess
import time
import glob

# 1. FUERZA BRUTA: Instalamos y buscamos la ruta real al mismo tiempo
print("📦 Verificando librerías en el sistema...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "iqoptionapi", "python-telegram-bot", "requests"])

# 2. EL TRUCO MAESTRO: Buscamos cualquier carpeta que termine en 'site-packages'
# Esto encuentra la librería esté donde esté, incluso en carpetas ocultas
for posible_ruta in glob.glob('/app/**/site-packages', recursive=True):
    if posible_ruta not in sys.path:
        sys.path.append(posible_ruta)
        print(f"✅ Ruta inyectada: {posible_ruta}")

# 3. CARGA SEGURA
try:
    from iqoptionapi.stable_api import IQ_Option
    print("✅ ¡LOGRADO! El motor de IQ Option está cargado.")
except ImportError:
    print("⚠️ Reintentando carga con path de emergencia...")
    # Último intento: ruta manual reportada en sus logs
    sys.path.append('/app/.venv/lib/python3.13/site-packages')
    from iqoptionapi.stable_api import IQ_Option

# --- VARIABLES ---
IQ_USER = os.getenv("IQ_EMAIL")
IQ_PASS = os.getenv("IQ_PASSWORD")

# --- CONEXIÓN FINAL ---
if IQ_USER and IQ_PASS:
    print(f"🚀 Iniciando sesión para: {IQ_USER}")
    Iq = IQ_Option(IQ_USER, IQ_PASS)
    check, reason = Iq.connect()
    if check:
        print("✅ EL PULPO ESTÁ VIVO Y CONECTADO.")
    else:
        print(f"❌ Error de conexión: {reason}")
else:
    print("❌ ERROR: Faltan variables de entorno.")
