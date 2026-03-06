import os
import sys

# Importación directa
try:
    from iqoptionapi.stable_api import IQ_Option
    print("✅ Motor IQ Option cargado con éxito.")
except ImportError as e:
    print(f"❌ Error crítico: {e}")
    sys.exit(1)

# Variables
IQ_USER = os.getenv("IQ_EMAIL")
IQ_PASS = os.getenv("IQ_PASSWORD")

if not IQ_USER or not IQ_PASS:
    print("❌ ERROR: Faltan variables IQ_EMAIL o IQ_PASSWORD.")
    sys.exit(1)

print(f"🚀 Iniciando sesión para: {IQ_USER}")
Iq = IQ_Option(IQ_USER, IQ_PASS)
check, reason = Iq.connect()

if check:
    print("✅ EL PULPO ESTÁ VIVO Y CONECTADO.")
else:
    print(f"❌ Error de conexión: {reason}")
