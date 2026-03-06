import os
import subprocess
import sys

# --- ESTO OBLIGA A RAILWAY A INSTALAR LA LIBRERÍA ---
def instalar_librerias():
    print("📦 Intentando instalar librerías faltantes...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "iqoptionapi", "python-telegram-bot", "requests"])
        print("✅ Librerías instaladas con éxito.")
    except Exception as e:
        print(f"❌ Error instalando: {e}")

# Intentar importar, si falla, instalar
try:
    from iqoptionapi.stable_api import IQ_Option
except ImportError:
    instalar_librerias()
    from iqoptionapi.stable_api import IQ_Option

# --- CONFIGURACIÓN DE VARIABLES ---
# Railway leerá estas que ya configuraste
IQ_USER = os.getenv("IQ_EMAIL")
IQ_PASS = os.getenv("IQ_PASSWORD")

if not IQ_USER or not IQ_PASS:
    print("❌ ERROR: No se encontraron las variables IQ_EMAIL o IQ_PASSWORD en Railway.")
    sys.exit(1)

print("🚀 Iniciando conexión con IQ Option...")

# Conexión real
Iq = IQ_Option(IQ_USER, IQ_PASS)
check, reason = Iq.connect()

if check:
    print("✅ SISTEMA ONLINE: El Pulpo está conectado a IQ Option.")
else:
    print(f"❌ ERROR DE CONEXIÓN: {reason}")
