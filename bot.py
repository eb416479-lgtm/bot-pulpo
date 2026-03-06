import os
import subprocess
import sys
import time

# 1. Forzamos la instalación (Railway ya debería tenerlas, pero esto asegura)
print("📦 Verificando entorno...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "iqoptionapi", "python-telegram-bot", "requests"])

# 2. TRUCO MAESTRO: Agregamos la carpeta de librerías al sistema manualmente
import site
importlib_path = site.getusersitepackages()
sys.path.append(importlib_path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'venv/lib/python3.13/site-packages')))

# 3. Ahora intentamos el import
try:
    from iqoptionapi.stable_api import IQ_Option
    print("✅ Librería cargada correctamente.")
except ImportError:
    print("⚠️ Fallo inicial, reintentando con path forzado...")
    time.sleep(2)
    from iqoptionapi.stable_api import IQ_Option

# --- VARIABLES ---
IQ_USER = os.getenv("IQ_EMAIL")
IQ_PASS = os.getenv("IQ_PASSWORD")
# ... resto del código
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
