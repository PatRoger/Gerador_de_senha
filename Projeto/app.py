from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho, usar_minusculas, usar_maiusculas, usar_numeros, usar_especiais):
    caracteres = ""
    
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not caracteres:
        return ""
    
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = ""
    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 12))
        usar_minusculas = "minusculas" in request.form
        usar_maiusculas = "maiusculas" in request.form
        usar_numeros = "numeros" in request.form
        usar_especiais = "especiais" in request.form
        
        senha_gerada = gerar_senha(tamanho, usar_minusculas, usar_maiusculas, usar_numeros, usar_especiais)
    
    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)