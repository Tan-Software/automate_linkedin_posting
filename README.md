<p id="start" align="center">
<h1>TANSOFTWARE</h1>
<h3>Publication automatique sur LinkedIn.</h3>
</p>
<table>
<tr>
<td>
<h3>Contribution légale :</h3>
<ul>
    <li>Ceci est un dépôt public.</li>
    <li>Vous pouvez copier librement ce dossier.</li>
    <li>Vous pouvez aussi y <strong>participer</strong> en émettant des pull requests.</li>
    <li>Réalisé par <a href="https://www.tansoftware.com" target="_blank">Tanguy Chénier</a>.</li>
</ul>
<img width="1000" height="0">
</td>
</tr>
</table>
</p>
<p align="center">
<a href="#prerequis">Prérequis</a> | <a href="#utilisation">Utilisation</a>  | <a href="#version">Version</a> 
</p>

<h2>Prérequis</h2>

<ol>
    <li>Installez python 3 </li>
    <li>Installez pip </li>
    <li>Modifiez les variables "<strong>access_token</strong>" et "<strong>urn</strong>" présentes dans le fichier "<strong>libs/post_on_linkedin.py</strong>"</li>
    <li>Entrez la commande suivante
    <span></span>

```python
pip install -r requirements.txt
 ```

</li>
</ol>

<h2>Utilisation</h2>

<ul>
    <span>Entrez la commande suivante</span>
    <span></span>

```bash
python main.py
 ```
</ul>
<ul>
Trois choix s'offrent à vous:

```bash
1 - De générer un "docx" dans lequel vous écrivez votre post.
Durant sa génération, il vous sera demandé à quelle date et quelle heure, vous souhaitez qu'il soit posté.
Vous pouvez en générer autant que vous le désirez.
```
   
```bash
2 - De lancer le programme en tache de fond, afin qu'il regarde toutes les heures, les documents que vous avez générés.
Et qu'ils les envoient sur votre compte LinkedIn, sous forme de post.
```

```bash
3 - De lancer un test de connexion afin de vérifier que les éléments renseignés "access_token" et "urn", soit les bons.
```
</ul>

<h2>Version</h2>

```
Python 3.0
```


