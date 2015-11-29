# SearchDB
Es un boceto de un servidor con servicio web, que analiza 
las conexiones en las base datos asociadas a un documento. Es necesario agregarlas
antes por formulario para no generar fallas es recontra beta, pero sirve. Para empezar
tengo que agregar un login de usuarios y  bueno se podrian analizar cosas dentro
de cada base de datos. Por el momento solo revisar si hay conexion es la unica opcion
se tendria que correr un crontab o algo parecido que ejecute el servicio en el 
http://localhost:8000/_host_ping -X PUT o un script en python , 
hay que correr el cyclone.py para que se puede acceder desde la area local 
