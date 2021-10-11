import json
import requests

res = requests.request(
    'POST',
    'https://apitest.nakala.fr/collections',
    headers={
        'X-API-KEY': '01234567-89ab-cdef-0123-456789abcdef',
        'Content-Type': 'application/json'
    },
    data=json.dumps({
        "status": "public",
        "metas": [
            {
                "propertyUri": "http://nakala.fr/terms#title",
                "value": "Ma belle collection",
                "typeUri": "http://www.w3.org/2001/XMLSchema#string",
                "lang": "fr"
            }
        ]
    })
)
print(res.text)

collection_id = json.loads(res.text)["payload"]["id"]

res = requests.request(
    'POST',
    'https://apitest.nakala.fr/datas/uploads',
    headers={
        'X-API-KEY': '01234567-89ab-cdef-0123-456789abcdef',
    },
    files=[
        ('file', ('canard.jpeg', open('canard.jpeg', 'rb')))
    ]
)
print(res.text)

imageMetadata = json.loads(res.text)

res = requests.request(
    'POST',
    'https://apitest.nakala.fr/datas',
    headers={
        'X-API-KEY': '01234567-89ab-cdef-0123-456789abcdef',
        'Content-Type': 'application/json'
    },
    data=json.dumps({
        'status': 'published',
        'files': [imageMetadata],
        'metas': [
            # le titre de la donnée
            {
                "propertyUri": "http://nakala.fr/terms#title",
                "value": "Ma première image",
                "typeUri": "http://www.w3.org/2001/XMLSchema#string",
                "lang": "fr"
            },
            # le type de la donnée (image)
            {
                "propertyUri": "http://nakala.fr/terms#type",
                "value": "http://purl.org/coar/resource_type/c_c513",
                "typeUri": "http://www.w3.org/2001/XMLSchema#anyURI",
            },
            # le créateur de la donnée
            {
                "propertyUri": "http://nakala.fr/terms#creator",
                "value": {
                    "givenname": "Jean",
                    "surname": "Dupont"
                }
            },
            # la date de création de la donnée
            {
                "propertyUri": "http://nakala.fr/terms#created",
                "value": "2020-01-01",
                "typeUri": "http://www.w3.org/2001/XMLSchema#string"
            },
            # la licence associée à la donnée
            {
                "propertyUri": "http://nakala.fr/terms#license",
                "value": "CC-BY-4.0",
                "typeUri": "http://www.w3.org/2001/XMLSchema#string"
            }
        ]
    })
)
print(res.text)

data_id = json.loads(res.text)["payload"]["id"]

res = requests.request(
    'POST',
    f"https://apitest.nakala.fr/collections/{collection_id}/datas",
    headers={
        'X-API-KEY': '01234567-89ab-cdef-0123-456789abcdef',
        'Content-Type': 'application/json'
    },
    data=json.dumps([data_id])
)
print(res.text)
