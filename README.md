# Messanger stats

### Description

Ce projet contient déjà un fichier d'exemple (message_umber.json) pour pouvoir tester les fonctionnalités du scripts.

Export d'exemple se passe sur une durée de 15 jours :
 
 <code>01/01/2019 - 15/01/2019</code>
### Features 
<h4>Base</h4>
<ul>
<li>
 Parse messanger export (json format)    
</li>
<li>
Génération d'un rendu visuel pour chaque graphique au format HTML5 (graphiques)
</li>
</ul>


<h4>Statistiques</h4>
<ul>
<li>
    <strong>Nombre de messages par personne</strong>
</li>
<li>
    <strong>Nombre de caractère écrient par personne</strong>
</li>
<li>
    <strong>Plus gros message par personne</strong>
</li>
<li>
    <strong>Temps passé entre chaque messages</strong>
</li>

</ul>

### Required 

<ul>
<li>
        Python >= 3
</li>
<li>
        pip3
</li>
<li>
       data export from messanger (default : <code>message_umber.json</code> )
</li>
</ul>


### Dependencies 

<ul>
<li>
<code>
    $ pip3 install plotly
</code>
</li>
<li>
<code>
    $ pip3 install numpy
</code>
</li>
<li>
<code>
    json
</code>
</li>
<li>
<code>
    pprint
</code>
</li>
</ul>


            
### Get started  

<code>
    $ python3 main.py 
</code>
      
### Display

<ul>
<li>
    Terminal (bref résumé)
</li>
<li>
    HTML5 (ouvert automatiquement pendant l'exécution du script main.py)
</li>
</ul>
       
       
### Structure

```
sylvain.joly
│   README.md
│   .gitignore    
│   umber.py  // main script 
|   message_umber.json //messanger export
│
└───src
│   │   __init__.py
│   │   graphService.py //methods for draw charts ...
│   │   messageService.py // methods parse / play with JSON
│   │   utils.py // cool methods
│   
│   
└───charts // save charts generated 
    │   .gitkeep
```
 
 
 