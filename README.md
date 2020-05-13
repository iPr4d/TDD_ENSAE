Ce repository contient le code Python pour le cours de Traitement des données distribuées (ENSAE 2020). Il permet d'automatiser l'installation de Java, Spark et Anaconda puis de configurer un environnement conda contenant pyspark et de lancer un serveur jyputer notebook accessible depuis le navigateur hôte après une rapide configuration SSH sur la machine virtuelle.

### Tâches à réaliser juste après la création d'une machine virtuelle sur VirtualBox


1) Connexion SSH : https://medium.com/@pierangelo1982/setting-ssh-connection-to-ubuntu-on-virtualbox-af243f737b8b

    - Aller dans le Terminal de la machine virtuelle

    - Exécuter sudo apt-get update puis sudo apt-get install openssh-server

    - Stopper la machine

    - Créer une redirection de ports (Port Forwarding) dans VirtualBox :
      Configuration > Réseau (Network) > Avancé (Advanced) > Redirection de ports (Port Forwarding) > Ajouter :
        - Nom: ssh, Port hôte: 2222, IP hôte: 127.0.0.1, Port invité: 22
        - Nom: jupyter, Port hôte: 8004, IP hôte: 127.0.0.1, Port invité: 8004

     - Relancer la machine et ouvrir le terminal

    - Autoriser l'authentification pour root dans le fichier sshd_config :
        - sudo nano /etc/ssh/sshd_config
        - Décommenter PermitRootLogin et remplacer par "yes"
        - Relancer le service ssh via sudo service ssh restart

2) Créer un mdp pour le user root : sudo passwd root (à utiliser pour se connecter à la machine via SSH)

3) Se connecter à la machine en local via la commande : ssh root@127.0.0.1 -p 2222

4) Exécuter le fichier python via la commande :  
    cat {chemin_dossier}/TDD_ENSAE/start_jupyter.py | ssh -p 2222 root@localhost python3 -
    
 Jupyter notebook est accessible dans le navigateur hôte à l'adresse http://127.0.0.1:8004/?token={TOKEN_ID}. L'environnement conda activé permet d'utiliser pyspark configuré sur la machine. 
