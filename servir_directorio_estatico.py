from flask import Flask, render_template, request, send_from_directory

"""
    Estas dos rutas son para servir el CSS y los iconos
"""
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/webfonts/<path:path>')
def send_webfont(path):
    return send_from_directory('webfonts', path)
