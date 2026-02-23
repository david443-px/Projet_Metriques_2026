import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nom = request.form.get("nom", "")
        prenom = request.form.get("prenom", "")
        message = request.form.get("message", "")
        return f" Message reçu ! Merci {prenom} {nom}. (Message: {message})"

    return render_template("contact.html")

@app.route("/paris")
def paris():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=48.8566&longitude=2.3522"
        "&hourly=temperature_2m"
        "&timezone=Europe%2FParis"
    )
    r = requests.get(url, timeout=10)
    data = r.json()

    # On récupère seulement ce qui nous intéresse
    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]

    # On renvoie une liste de couples time/temp
    result = [{"time": t, "temperature": temp} for t, temp in zip(times, temps)]
    return jsonify(result)

@app.route("/rapport")
def rapport():
    return render_template("graphique.html")

@app.route("/histogramme")
def histogramme():
    return render_template("histogramme.html")

@app.route("/paris_weathercode")
def paris_weathercode():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=48.8566&longitude=2.3522"
        "&hourly=weather_code"
        "&timezone=Europe%2FParis"
    )
    r = requests.get(url, timeout=10)
    data = r.json()

    codes = data["hourly"]["weather_code"][:24]  # prochaines 24h

    # Compter combien de fois chaque code apparaît
    counts = {}
    for c in codes:
        counts[c] = counts.get(c, 0) + 1

    # Retour format facile pour le graphique
    result = [{"code": str(k), "count": v} for k, v in counts.items()]
    return jsonify(result)

@app.route("/atelier")
def atelier():
    return render_template("atelier.html")

# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
