## Tâches à réaliser juste après la création d'une machine virtuelle sur VirtualBox


- Connexion SSH : https://medium.com/@pierangelo1982/setting-ssh-connection-to-ubuntu-on-virtualbox-af243f737b8b

- Aller dans le Terminal de la machine virtuelle

- Exécuter sudo apt-get update puis sudo apt-get install openssh-server

- Stopper la machine

- Créer une redirection de ports (Port Forwarding) dans VirtualBox :
    - Configuration > Réseau (Network) > Avancé (Advanced) > Redirection de ports (Port Forwarding) > Ajouter (Add) :
        - Nom: ssh, Port hôte: 2222, IP hôte: 127.0.0.1, Port invité: 22
        - Nom: jupyter, Port hôte: 8004, IP hôte: 127.0.0.1, Port invité: 8004

- Relancer la machine et ouvrir le terminal

- Autoriser l'authentification pour root dans le fichier sshd_config :
    - sudo nano /etc/ssh/sshd_config
    - Décommenter PermitRootLogin et remplacer par "yes"
    - Relancer le service ssh via sudo service ssh restart

- Créer un mdp pour le user root : sudo passwd root (à utiliser pour se connecter à la machine via SSH/éxecuter le code python)

- Se connecter à la machine en local via la commande : ssh root@127.0.0.1 -p 2222

- Installer curl : (sudo) apt install curl

- Exporter les variables d'environnement qui seront nécessaires pour JAVA, SPARK et ANACONDA:

    1) Ouvrir le fichier .bashrc via 'nano ~/.bashrc'
    2) Ajouter les lignes suivantes à la fin du fichier :
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
        export SPARK_HOME="/home/{NOM_UTILISATEUR}/spark-hadoop/spark-2.4.5-bin-hadoop2.7"
        export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
        export PATH="$HOME/anaconda3/bin:$PATH"
    3) Exécuter 'source ~/.bashrc'

NB: si le nom d'utilisateur est inconnu, exécuter 'cd /home && ls' et le nom d'utilisateur s'affichera.

- Exécuter le fichier python via la commande :  cat {chemin_dossier}/test_mkdir_ssh.py | ssh -p 2222 root@localhost python3 -