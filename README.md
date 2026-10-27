# Révision SSA

Quiz de révision du **Surveillant Sauveteur Aquatique** (références techniques nationales, édition septembre 2026) : sessions rapides de 10 questions, examen blanc de 30 questions, révision par chapitre et suivi des erreurs.

**Fiches de révision :** les points clés de chaque fiche RTN, à lire ou à écouter (synthèse vocale du navigateur), et la fiche officielle elle-même (pages du PDF affichées dans le site, sur tous les téléphones). Accessibles depuis l'accueil, depuis chaque réponse (« Lire la fiche », « Fiche PDF ») et depuis le résultat d'une session (« Lire les fiches à revoir »). Le document officiel complet se consulte aussi page par page ou en PDF d'origine.

**Site :** https://blefebvre-lfbvrr.github.io/Revision-SSA/

## Progression

Tout est automatique, il n'y a rien à faire :

- Enregistrée dans le navigateur (`localStorage`) à chaque réponse. Une session interrompue reprend là où elle s'est arrêtée, même après fermeture de la page.
- Le site demande au navigateur un stockage persistant, pour qu'il ne l'efface pas quand il fait de la place.
- Plusieurs onglets ouverts ne s'écrasent pas : chaque onglet relit la dernière progression enregistrée quand il revient au premier plan.
- Installable sur l'écran d'accueil et utilisable hors ligne. Sur iPhone, l'installation évite que Safari efface les données d'un site non visité depuis 7 jours.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `index.html` | L'application complète. Les questions sont dans le tableau `RAW` : `[chapitre, fiche, question, bonne réponse, faux 1, faux 2, faux 3, explication]`. |
| `sw.js` | Service worker : hors ligne, réseau d'abord pour toujours servir la dernière version des questions. |
| `manifest.webmanifest`, `icons/` | Installation sur l'écran d'accueil. |
| `rtn/` | Le document officiel *Références techniques nationales SSA* (DGSCGC, édition septembre 2026) : le PDF d'origine et une image WebP par page. |
| `outils/pages_rtn.py` | Régénère `rtn/` à partir d'une nouvelle édition du PDF et affiche la table des pages de chaque fiche à recopier dans `index.html` (`PAGES`, `PDF_PAGES`). |

Modifier ou ajouter une question ne fait pas perdre la progression des autres : chaque question est identifiée par son texte.
