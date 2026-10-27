# Révision SSA

Quiz de révision du **Surveillant Sauveteur Aquatique** (références techniques nationales, édition septembre 2026) : sessions rapides de 10 questions, examen blanc de 30 questions, révision par chapitre et suivi des erreurs.

**Site :** https://blefebvre-lfbvrr.github.io/Revision-SSA/

## Progression

- Sauvegardée automatiquement dans le navigateur (`localStorage`) à chaque réponse. Une session interrompue reprend là où elle s'est arrêtée, même après fermeture de la page.
- Le site demande au navigateur un stockage persistant, pour qu'il ne l'efface pas quand il fait de la place.
- Plusieurs onglets ouverts ne s'écrasent pas : chaque onglet relit la dernière progression enregistrée quand il revient au premier plan.
- **Exporter / Importer** (en bas de l'accueil) : un fichier `.json` pour garder une copie ou passer à un autre appareil.
- Installable sur l'écran d'accueil et utilisable hors ligne. Sur iPhone, l'installation évite que Safari efface les données d'un site non visité depuis 7 jours.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `index.html` | L'application complète. Les questions sont dans le tableau `RAW` : `[chapitre, fiche, question, bonne réponse, faux 1, faux 2, faux 3, explication]`. |
| `sw.js` | Service worker : hors ligne, réseau d'abord pour toujours servir la dernière version des questions. |
| `manifest.webmanifest`, `icons/` | Installation sur l'écran d'accueil. |

Modifier ou ajouter une question ne fait pas perdre la progression des autres : chaque question est identifiée par son texte.
