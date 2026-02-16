------------------------------------------------------------------------------------------------------
ATELIER METRIQUES
------------------------------------------------------------------------------------------------------
L’idée en 30 secondes : Cet atelier a pour objectif de vous apprendre à **créer des graphiques** (dans le cadre de création de métriques par exemple) grace à une application **Python** et via la **l'utilisation et la construction d'API**. Vous allez utiliser et mettre en oeuvre au travers de cet atelier, un **serveur Web Python** utilisant le **Framework Flask**. Vous allez créer des API pour mettre en service des bibliothèques graphiques. Large programme mais tout à fait accessible et ne nécessitant pas de base technique particulière. Juste de l'observation et de la rigueur dans votre travail.
  
**Architecture cible :** Ci-dessous, voici l'architecture cible souhaitée.   
  
![Screenshot Actions](Architecture_cible.png)  
  
-------------------------------------------------------------------------------------------------------
Séquence 1 : Codespace de Github
-------------------------------------------------------------------------------------------------------
Objectif : Création d'un environnement Codespace Github  
Difficulté : Très facile (~5 minutes)
-------------------------------------------------------------------------------------------------------
**Faites un Fork de ce projet**. Si besoin, voici une vidéo d'accompagnement pour vous aider à "Forker" un Repository Github : [Forker ce projet](https://youtu.be/p33-7XQ29zQ) 
  
Ensuite depuis l'onglet **[CODE]** (boutton vert) dans votre nouveau Repository Github, **ouvrez un Codespace Github**.
  
---------------------------------------------------
Séquence 2 : Création de votre environnement de travail
---------------------------------------------------
Objectif : Créer votre environnement de travail  
Difficulté : Simple (~10 minutes)
---------------------------------------------------
Vous allez dans cette séquence **installer un serveur Flask** dans votre Codespace. Depuis le terminal de votre Codespace copier/coller les lignes de codes ci-dessous étape par étape :  

**Création du serveur Flask**  
```
make install
```
**Lancement de l'application**  
```
make run
```
**Réccupération de l'URL de votre application Web**. Votre application Web Flask est déployée dans votre Codespace. Pour obtenir votre URL cliquez sur l'onglet **[PORTS]** dans votre Codespace (à coté de Terminal) et rendez public votre port 5000 (Visibilité du port). Ouvrez l'URL dans votre navigateur et c'est terminé, votre application est en ligne et accessible depuis Internet !  
  
---------------------------------------------------
Séquence 3 : Modifier son code dans Github
---------------------------------------------------
Objectif : Apporter des modifications à son code et le mettre en ligne
Difficulté : Facile (~15 minutes)
---------------------------------------------------  
Dans cette séquence, vous allez **modifier le code du fichier hello.html dans Github**, pour ensuite mettre à jour votre environnement Codespace et observer le résultat en ligne sur votre site Web.  

**Etape 1 :** Dans Github, **modifier la ligne 6 du fichier hello.html** pour y ajouter votre nom et prénom. **Commitez** (bouton vert) pour enregistrer vos modifications dans Github.  

**Etape 2 :** Depuis le terminal de votre Codespace, **stoppez votre serveur Web** via la **combinaison de touches Ctrl+c**. Cette combinaison de touches stop votre serveur.
   
**Etape 3 :** Toujours depuis le terminal Codespace, **mettre à jour votre code** en executant la commande suivante :
```
git pull
```

**Etape 4 :** Dernière étape, relancer votre serveur Web et observez le résultat sur votre site Web en ligne.
```
make run
```

Notions acquises dans cette séquence : Vous avez dans cette séquence modifier du code dans Github, puis mis à jour votre espace Codespace pour enfin observer le résultat en ligne (environnement en "production").

---------------------------------------------------
Séquence 4 : Exercices
---------------------------------------------------
Objectif : Apprendre à travailler avec des API  
Difficulté : Moyenne (~1 heure)
---------------------------------------------------
### Exercice 1 : Création d'une nouvelle route dans votre application   
### Objectif : Savoir créer des routes (c'est à dire créer des API)  
L'exercice consiste à créer une nouvelle route accèssible depuis le chemin https://{Votre URL}**/contact** de votre site et qui affichera "Ma page de contact" dans le navigateur de l'internaute. L'internaute saisira l'adresse suivante dans son navigateur : **https://{Votre URL}/contact** et obtiendra donc le résultat "Ma page de contact". Vous allez pour cela, depuis GitHUB, **ajouter le code suivant dans votre fichier app.py** qui est à la racine de votre Repository :
```
@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"  
```
**Remarque importante** : Ce code ci-dessus est à ajouter dans la zone entre commentaires, c'est à dire **entre la ligne 10 à 15 du fichier app.py**.  

Mettez à jour votre serveur (séquence 3) et tappez **https://{Votre URL}/contact** dans l'URL de votre navigateur et observez le résultat en ligne.  
  
Notions acquises lors de cet exercice : Vous avez appris lors de cet exercice à créer des API (c'est à dire des routes) dans une application Python. Vous pouvez créer autant d'API (de routes) que vous le souhaitez pour les besoins de votre application Python.  
  
<sub>_________________________________________________________________________</sub>
### Exercice 2 : Les données d'une API   
### Objectif : Utiliser les données issues d'une API externes pour créer une route adaptée à vos besoins  
Pour commencer, copier l'URL ci-dessous dans un nouvel onglet de votre navigateur et observez le résultat :  
```
https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m
```
Il s'agit ici des **prévisions de températures pour la ville de Paris pour les 7 prochains jours**. Vous observerez que nous utilisons une API gratuite fourni par **api.open-meteo.com**. C'est typiquement le format que vous trouverez dans le cadre des services de métriques (Données issues de serveurs, de réseaux, de stockages, etc..).  
  
Les API fournissent en général des données au format JSON. JSON est un format structuré avec des étiquettes (également appelé des keys) et ont pour objectif de fournir des données "brut". **Prenez ici quelques minutes pour "comprendre" la structure de ces données JSON et identifer les clés et les données.**

Ce qui nous intéresse à présent, c'est extraire la valeur de [time] (c'est à dire les dates) et les valeurs stockées dans le tableau [temperature_2m], c'est à dire les températures associées aux dates.  
  
Vous allez à présent **créer une nouvelle route "/paris"** dans votre application Python pour filtrer l'API d'api.open-meteo.com et extraire uniquement les dates et températures de Paris pour les 7 prochains jours. **Ci-dessous la route à ajouter dans votre application app.py**.
```
@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)
```
**Mettez à jour votre Codespace** et observez le résultat sur votre site Web en ligne.  

Notions acquises dans cet exercice : Vous avez appris lors de cet exercice à créer des API présentant des données filtrées issues d'input au format JSON.
  
<sub>_________________________________________________________________________</sub>
### Exercice 3 : Les fichiers HTML dans Flask   
### Objectif : Comprendre le fonctionnement du Framework Flask    
Le Framework Flask nous impose de déposer tous les fichiers HTML dans le **répertoire templates** dédié à cet effet dans Github.  
Depuis GitHUB, nous allons donc créer et déposer dans le répertoire "templates" une page HTML qui sera accessible depuis la route suivante : https://{VOTRE_URL}**/rapport**  
  
**Etape 1 : Création du fichier graphique.html**  
Dans votre répertoire templates dans Guthub, **créez un fichier graphique.html** contenant le code suivant :  
```
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Graphique</title>
 </head>  
<body>
    <h2>Mon Graphique</h2>
</body>
</html>
```
**Etape 2 : Création d'une nouvelle route**  
Créez à présent une nouvelle route dans votre fichier app.py afin de pouvoir consulter votre fichier graphique.html depuis votre site Web en ligne.
Pour cela, **ajoutez le code ci-dessous dans votre fichier app.py** :
```
@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")
```
**Mettez à jour votre Codespace** et observez le résultat sur votre site Web en ligne.  
  
Notions acquises dans cet exercice : Nous avons vu lors de cet exercice comment créer et où déposer les fichiers HTML lorsque l'on utise le Framework Flask. Nous avons également découvert que les Framework (cadre de travail) nous imposent une structure de travail où chaque élément doit être déposés à sa place.  

<sub>_________________________________________________________________________</sub>
### Exercice 4 : Mise en graphique   
### Objectif : Mettre en graphique les valeurs JSON issues d'une API    
Mettons à présent ces valeurs (issues de l'API /rapport) sous la forme d'un graphique qui sera pour l'utilisateur bien plus agréable et facile à lire que des données brutes au format JSON.  
Pour cela, nous devons utiliser les données de notre nouvelle API /rapport (la température de Paris pour les 7 prochains jours) et les injecter dans notre fichier graphique.html. Nous allons utiliser une bibliothèque open source fournie par Google pour créer ce graphique. **Modifier votre précédent fichier graphique.html** dans GitHUB et remplacer son code par celui-ci :  
```
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Températures Paris — Google LineChart</title>

  <script src="https://www.gstatic.com/charts/loader.js"></script>

  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 24px; }
    #chart { width: 100%; height: 520px; }
    #status { margin-top: 12px; white-space: pre-wrap; }
  </style>
</head>

<body>
  <h1>Températures horaires — Paris</h1>
  <div id="chart"></div>
  <div id="status"></div>

  <script>
    google.charts.load('current', { packages: ['corechart'] });
    google.charts.setOnLoadCallback(init);

    let cachedRows = null;

    async function init() {
      try {
        const rows = await fetchParisData();
        cachedRows = rows;
        drawChart(rows);

        window.addEventListener('resize', () => {
          if (cachedRows) drawChart(cachedRows);
        });
      } catch (err) {
        showStatus("Erreur: " + (err?.message || err));
        console.error(err);
      }
    }

    async function fetchParisData() {
      const res = await fetch('/paris', { headers: { 'Accept': 'application/json' } });

      if (!res.ok) {
        throw new Error(`HTTP ${res.status} sur /paris`);
      }

      const json = await res.json();

      // json attendu: [{ datetime: "2026-02-15T00:00", temperature_c: 0.5 }, ...]
      // Convertir en rows: [Date, Number]
      const rows = json.map(p => {
        const dt = toDate(p.datetime);
        const temp = Number(p.temperature_c);
        return [dt, temp];
      });

      // Optionnel: trier par date au cas où
      rows.sort((a, b) => a[0] - b[0]);

      return rows;
    }

    function toDate(isoLike) {
      // "2026-02-15T00:00"
      // On parse en Date locale. Si tu veux forcer UTC, dis-moi.
      const [datePart, timePart] = isoLike.split('T');
      const [y, m, d] = datePart.split('-').map(Number);
      const [hh, mm] = timePart.split(':').map(Number);
      return new Date(y, m - 1, d, hh, mm, 0);
    }

    function drawChart(rows) {
      const data = new google.visualization.DataTable();
      data.addColumn('datetime', 'Date/Heure');
      data.addColumn('number', 'Température (°C)');
      data.addRows(rows);

      const options = {
        title: 'Température à Paris (horaire)',
        legend: { position: 'bottom' },
        hAxis: {
          title: 'Date/Heure',
          format: 'dd/MM HH:mm'
        },
        vAxis: {
          title: '°C'
        },
        explorer: { actions: ['dragToZoom', 'rightClickToReset'] }
      };

      const chart = new google.visualization.LineChart(document.getElementById('chart'));
      chart.draw(data, options);

      showStatus(`OK — ${rows.length} points chargés depuis /paris`);
    }

    function showStatus(msg) {
      document.getElementById('status').textContent = msg;
    }
  </script>
</body>
</html>
```
Notions acquises dans cet exercice : Nous avons fetcher le endpoint Flask /paris au fichier html graphique.html (en ajoutant un Google Charts LineChart) transformant ainsi la réponse JSON de l'API /paris en un graphique lisible pour l'utisateur.  

<sub>_________________________________________________________________________</sub>
### Exercice 5 : Créer votre propre graphique   
### Objectif : Devenir autonome dans la création de vos graphiques    
A l'aide des graphiques disponibles dans la galerie open source de Google disponibles à l'adresse suivante :  
https://developers-dot-devsite-v2-prod.appspot.com/chart/interactive/docs/gallery?hl=fr  
**créer un nouveau graphique à colonnes** (un histogramme) afin de présenter les prévisions météorologiques de Paris pour ces 7 prochains jours sous la forme d'un histogramme. Ce nouveau graphique sera accessible sur votre site Web en ligne via le chemin suivant : **https://{Votre URL}/histogramme**

<sub>_________________________________________________________________________</sub>
### Exercice 6 : Faites preuve de créativité...   
### Objectif : Customisation de votre page de contact    
Reprenez l'exercice 1 et faites pointer à présent votre route "/contact" vers un fichier HTML un peu plus élaboré (faites preuve de créativité). Dans cette page de contact, l'utilisateur sera en mesure de pouvoir laisser son nom, son prénom et un message à votre attention. L'enregistrement des données ne sera pas opérationnel dans le cadre de cet exercice (il n'y a pas de base de données dans cet atelier). Il s'agit ici juste de vous évaluer sur l'aspect esthétique de votre création. Les points de cet exercice vous seront donc attribués sur la base du Design de votre œuvre (à la convenance de l'examinateur :-)...

---------------------------------------------------
Séquence 4 : Atelier
---------------------------------------------------
Objectif : Constuire votre propre graphique  
Difficulté : Moyenne (~1 heure)
---------------------------------------------------
Depuis la solution https://open-meteo.com/en/docs, **choisissez ce que vous souhaitez mettre en graphique** (exemple : la vitesse du vent à Marseille, l'humidité de Versailles ou le niveau de précipitations de Lille) et **créez votre propre indicateur**. Attention, n'utilisez pas les Lines Chart ou les histogrammes de Google car ils ont déjà été utilisés lors des exercices précédents. Choisissez un nouveau format de graphique our votre atelier. **Votre graphique sera accéssible via la route /atelier**    

Notion acquises : **Vous êtes à présent totalement autonome pour créer vos propres Dashboard de métrologie**.

---------------------------------------------------
Evaluation
---------------------------------------------------
Cet atelier de métrologie, **noté sur 20 points**, est évalué sur la base du barème suivant :  
- Série d'exerices de la séquence 3 (12 points)
- Atelier de la séquence 4 - Ajout d'une fonctionnalité (3 points)
- Qualité de votre réalisation (Design, erreurs, ...) (3 points)
- Processus travail (quantité de commits, cohérence globale, interventions externes, ...) (2 points)

--------------------------------------------------------------------
Troubleshooting :
---------------------------------------------------
Objectif : Visualiser ses logs et découvrir ses erreurs
---------------------------------------------------
Lors de vos développements, vous serez peut-être confronté à des erreurs systèmes car vous aurez faits des erreurs de syntaxes dans votre code, faits de mauvaises déclarations de fonctions, appelez des modules inexistants, mal renseigner vos secrets, etc…  
  
Les causes d'erreurs sont quasi illimitées. **Vous devez donc vous tourner vers les logs de votre serveur via le terminal de Codespace pour comprendre d'où vient le problème**  
