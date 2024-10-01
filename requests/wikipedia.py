import requests

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
url = "https://es.wikipedia.org/"

respuesta = requests.get(url, headers=encabezado)
print(respuesta.text)

