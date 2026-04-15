from flask import Flask, render_template, abort
from config import HERRAMIENTAS # Importamos tu lista de herramientas

app = Flask(__name__)

# RUTA PARA LA PÁGINA DE INICIO
@app.route('/')
def index():
    # Pasamos la lista de herramientas para que el inicio las muestre
    return render_template('base.html', herramientas=HERRAMIENTAS)

# RUTA DINÁMICA PARA LAS HERRAMIENTAS
@app.route('/tools/<slug>')
def dynamic_tool(slug):
    # Buscamos la herramienta en el diccionario de config.py
    data = HERRAMIENTAS.get(slug)
    
    if not data:
        # Si no existe (ej: /tools/hacking), lanza error 404
        return "Error: Herramienta no encontrada", 404
        
    # Cargamos la plantilla automática y le pasamos los datos
    return render_template('tools/automatica.html', herramienta=data, slug=slug)

if __name__ == '__main__':
    # host='0.0.0.0' es CLAVE para que el navegador de tu Oppo lo vea
    # debug=True permite ver errores si algo falla
    app.run(debug=True, host='0.0.0.0', port=5000)

