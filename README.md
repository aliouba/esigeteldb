esigeteldb
==========

//////Installation de Python ///////////////

cd ~/Downloads/

wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz

tar -xvf Python-2.7.5.tgz

cd Python-2.7.5

./configure

make

sudo make altinstall



////////////////Installation de pip/////////////

sudo apt-get install python-pip

///////////////////Les dépendances pour que PostgreSQL puisse travailler avec python /////////////

sudo apt-get install libpq-dev python-dev

///////////////////////Installer PostgreSQL/////////////////////

sudo apt-get install postgresql postgresql-contrib

////////////////////////Configurer Postgres/////

sudo su - postgres

createdb taxi

sudo su - postgres

createuser -P

/////Requete pour ajouter les droits ////

psql //pour passer en mode requête

GRANT ALL PRIVILEGES ON DATABASE taxi TO admin; /

//////////////Téléchrager tout ce projet //////////////////


/////////////lancer l'environnment virtuel  ////


source django_env/bin/activate


/////////////lancer le serveur Web////


python manage.py runserver



//////Enjoy en accedant à l'adresse http://127.0.0.1:8888/taxi/planning   ////////////////////
