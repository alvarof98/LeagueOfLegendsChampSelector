# LeagueOfLegendsChampSelectorv1.0.0

**IMPORTANTE LEER TODO**

-alvarof98.github.io --> Contiene los notebooks donde he creado todo el trabajo de machine learning, y la WebApp donde se encuentra la parte front-end
-alvarofPython.github.io --> Contiene los scripts de python y los modelos.pkl que se ejecutan en un servidor aparte y componen la parte back-end

Para inicializar el servidor se han de cumplir los siguientes requisitos:
1. Desplegar el repositorio obscure-harbor-96731 (descargar heroku y registrarse en heroku)

  -$heroku login
  
  -$ heroku git:clone -a obscure-harbor-96731 
  
  -$ cd obscure-harbor-96731
  
  -$ git add .
  
  -$ git commit -am "make it better"
  
  -$ git push heroku master
  
  Una vez inicializado, abrimos heroku, seleccionamos el proyecto, y le damos a open app
 
 2. Abrir un servidor local en \alvarof98.github.io\WebApp con el puerto 8080
 
 -Para abrir el servidor local, en el repositorio donde esta el index.html poner el siguiente comando:
 
 $WebApp>python -m http.server 8080
 
 3. Lo unico que queda es abrir la ruta en un navegador localhost:8080/index.html y probar la aplciacion!
 
 Nota: La aplicacion esta en su primera version. Ire metiendole parches y funcionalidades, lo que hay hecho es todo el trabajo de machine learning del selector de campeones y desplegado en una aplicacion web basica. El modelo NLP se puede probar en el notebook de NLP. Ire actualizando versiones segun vaya avanzando en el proyecto, lo que hay es la base.
 
 Nota2: Tuve que comprimir el archivo model_sup.pkl porque el archivo era demasiado grande. Descomprimir el archivo .rar para que funcione.
 
