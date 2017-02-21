# Machine Vagrant Spark / Toree
## Objectif
Une version la plus simple possible de spark sous linux en installation automatique avec intégration de Toree pour pouvoir travailler directement avec des notebooks

## Pré-requis
- Virtual Box
- Vagrant
- Disponibilité du réseau 192.168.33.0/24 sur votre machine

## Installation
- git clone
- Se mettre dans le répertoire cloner
- vagrant up

## Utilisation
- vagrant ssh
- Lancer spark (1 cluster manager + 1 noeud) : toree-launch.sh
- Lancer le notebook : jupyter-launch.sh
- Ouvrir un browser sur la machine hôte + se logger : http://192.168.33.10:7077 (accès à spark)
- Dans une autre fenêtre du browser, copier/coller le lien vers jupyter notebook
- Ouvrir le test scala
- Lancer => affichage de la valeur de Pi

## Arrêt
- Ctrl + C pour arrêter le notebook
- toree-stop.sh
- exit
- vagrant halt (ou destroy)

## 32 ou 64 bits ?
- Editer le fichier bootstrap.sh et modifier la valeur de la variable d'environnement HW_ARCH (32 pour 32bits, ...)
- Editer le fichier Vagrantfile et changer la valeur de la box (64bits ou 32bits box)

## Pour travailler
Vos notebooks sont automatiquement sauvegardés dans le répertoire workspace de votre installation

## Plus d'infos sur notre société 
www.isitix.com

