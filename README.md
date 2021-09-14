# FAST-API-CRUD
Crud utilizando fast api con python y Mysql
![alt text](https://github.com/sebas1017/FAST-API-CRUD/blob/main/FASTAPICRUD.png?raw=true)



[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=sebas1017&layout=compact)](https://github.com/sebas1017/FAST-API-CRUD/)


Durante este proyecto tendremos una APIREST desarrollada en FASTAPI nos permitira dicha api realizar el registro de usuarios con ciertos atributos y poder 
almacenar estos datos en una base de datos MYSQL.

requisitos previos:
tener instalado mysql en tu equipo y tener una base de datos creada y que tengas el usuario y contraseña para acceder a esta base de datos
ya que la necesitaremos despues

luego de tener esto en cuenta procederemos con los pasos para correr el proyecto de forma local

crear una carpeta en tu equipo donde quieras instalar el proyecto
en la terminal que prefieras wsl (linux para windows) o cmd en windows directamente ejecutar el siguiente comando

git clone https://github.com/sebas1017/FAST-API-CRUD

con esto clonaras el repositorio en tu carpeta local luego de esto:
crear entorno virtual en la carpeta digita este comando en la carpeta donde clonaste el repositorio


python3 -m venv FASTAPI

activar entorno virtual
ir a la ruta y ejecutar este comando
source FASTPI/bin/activate

luego de activado el entorno veras que tu consola cambio de apariencia LUEGO instala todas las dependencias del proyecto en tu entorno virtual anteriormente creado

pip install -r requirements.txt

esto tardara un momento e instalara lo necesario para ejecutar el proyecto

ahora bien.. como se menciono anteriormente para que este proyecto se ejecute correctamente debemos tener previamente creada una base de datos mysql instalada localmente
a la que podamos acceder
para crear la base de datos teniendo mysql instalado en nuestro equipo vamos a cmd o wsl cualquiera de los dos y ejecutamos el comando

mysql -u root -p

esto nos pedira la contraseña que hayamos definido para poder acceder a mysql esto se configura cuando instalamos mysql por primera vez
una vez dentro de mysql ejecutamos el comando

CREATE DATABASE NOMBREBASEDEDATOSPREFERIDO;

aqui le ponemos el nombre que queramos a nuestra base de datos y la contraseña para acceder sera la misma contraseña con que accedimos a mysql


luego vamos al archivo database.py el cual esta en nuestra carpeta del proyecto y lo abrimos y veremos algo como esto:
![alt text](https://github.com/sebas1017/FAST-API-CRUD/blob/main/database.PNG?raw=true)


aqui reemplazaremos la contraseña de nuestra base de datos mysql creada el nombre de esta y el resto se queda igual

luego de esto ejecutaremos en la carpeta de nuestro proyecto el siguiente comando

uvicorn main:app --reload

cuanto corramos el proyecto con este comando si configuraron todo correctamente deberan ver lo siguiente:
![alt text](https://github.com/sebas1017/FAST-API-CRUD/blob/main/running.PNG?raw=true)

y ya podremos hacer llamado a los endpoints de nuestra APIREST para saber como ejecutarlos se puede acceder a /docs desde el url local host
http://127.0.0.1:8000/docs
![alt text](https://github.com/sebas1017/FAST-API-CRUD/blob/main/done.PNG?raw=true)

