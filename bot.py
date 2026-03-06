import os
import subprocess
import sys
import time
import site

# 1. FUERZA BRUTA PARA LIBRERÍAS
print("📦 Verificando entorno...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "iqoptionapi", "python-telegram-bot", "requests"])

# 2. TRUCO DE RUTA (Basado en lo que vimos en sus registros)
# Agregamos todas las posibles rutas donde Railway guarda cosas
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.venv/lib/python3.13/site-packages')))
sys.path.append(site.getusersitepackages())

# 3. IMPORTACIÓN SEGURA
try:
    from iqoptionapi.stable_api import IQ_Option
    print("✅ Librería cargada correctamente.")
except ImportError:
    print("⚠️ Reintentando carga de librería...")
    time.sleep(2)
    from iqoptionapi.stable_api import IQ_Option

# --- VARIABLES (Usa las que ya configuraste en Railway) ---
IQ_USER = os.getenv("IQ_EMAIL")
IQ_PASS = os.getenv("IQ_PASSWORD")

if not IQ_USER or not IQ_PASS:
    print("❌ ERROR: No se encontraron las variables IQ_EMAIL o IQ_PASSWORD en Railway.")
    sys.exit(1)

# --- CONEXIÓN AL MERCADO ---
print(f"🚀 Intentando conectar a IQ Option con: {IQ_USER}")
Iq = IQ_Option(IQ_USER, IQ_PASS)
check, reason = Iq.connect()

if check:
    print("✅ EL PULPO ESTÁ VIVO: Conexión exitosa a IQ Option.")
    # AQUÍ EMPIEZA SU ESTRATEGIA
    # Ejemplo: print(f"Saldo actual: {Iq.get_balance()}")
else:
    print(f"❌ ERROR DE CONEXIÓN: {reason}")
    # Si el error es 'Invalid Credentials', revise su correo/clave en Railway
