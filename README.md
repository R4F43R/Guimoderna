# Guimoderna
3. Instalación en PC
bash
pip install websockets pyautogui
python server.py
4. Configuración
Obtén la IP de tu PC:

Windows: ipconfig (Busca "IPv4")

Linux/macOS: ifconfig

En el móvil:

Abre index.html en Chrome/Firefox

Reemplaza TU_IP_PC en el código JavaScript

Permite acceso a la cámara

5. Funcionamiento
El modelo de IA detecta tu rostro y sigue el movimiento de tu nariz.

Las coordenadas se envían vía WebSocket a la PC.

PyAutoGUI mueve el mouse proporcionalmente a tu movimiento.

Características Adicionales
Seguridad: Agrega token de autenticación en WebSocket.

Clics: Detecta parpadeos con eyeBlink del modelo.

Optimización: Usa requestAnimationFrame para mejor rendimiento.