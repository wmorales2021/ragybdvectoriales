1. Desde Python, escriba un programa para enviar mensajes a Chatgpt y recuperar respuestas
   
se procede a escribir la linea de comandos, tal como se encuentra estrucurada en la plataforma https://campusvirtual.escuelaing.edu.co/ y se adjunta evidencia de la ejecución.

Nota: Fue necesario adquirir un APIKEY de openAI para llevar a cabo el ejercicio, especificamente la APIKEY (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) 

![image](https://github.com/wmorales2021/ragybdvectoriales/assets/79813722/2967ed2a-9da3-4219-bc83-8d080d36d6e2)

2. Escriba un RAG simple usando una base de datos vectorial en memoria

   A continuación se adjunta la evidencia de la ejecución realizada en pycharm

   Nota: Fue necesario adquirir un APIKEY de openAI para llevar a cabo el ejercicio 

 ![image](https://github.com/wmorales2021/ragybdvectoriales/assets/79813722/c9ec6c61-c3a0-421e-9dcc-5c1902f80ff5)


3 se escribe un RAG usando Pinecone

Se hace uso de las APIKEY de adquiridas de OPEANAI y la creada en PINECONE, como se muestra a continuación : 

os.environ["OPENAI_API_KEY"] = "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"
os.environ["PINECONE_API_KEY"] = "4ce1743e-57db-4a13-9809-530ec8c90e32"

![image](https://github.com/wmorales2021/ragybdvectoriales/assets/79813722/673c1fa7-fceb-4100-aea0-dd188087d714)

se realiza llamado al APIKEY DE openAI, haciendole preguntas, para lograr este objetivo, hacemos uso de la siguiente funcion, creando una instancia donde se le agraga un archivo TXT
con la información relevante que deseamos consultar, en mi caso por ejemplo le agregué inicialmente un archivo de la segunda guerra mundial, y le hice preguntas de la segunda guerra,  acto seguido, y  para efectos de pruebas le agregué otro llamado 
"iglesia_Dios.txt"

<img width="609" alt="image" src="https://github.com/wmorales2021/ragybdvectoriales/assets/79813722/c2f0f63d-192f-4a97-927c-1ab9d1b7610b">

![image](https://github.com/wmorales2021/ragybdvectoriales/assets/79813722/e4ef9f30-ba35-4929-b9f0-045b536cdb16)













   






