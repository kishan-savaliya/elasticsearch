from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200}])
print(es.indices.get_alias("*"))

data = [{
            "age": 40, "name": "Bettie Buckner", "gender": "female"
        },
        {
            "age": 28, "name": "Hanson Gates", "gender": "male"
        },
        {
            "age": 20, "name": "Audra Marshall", "gender": "female"
        },
        {
            "age": 34, "name": "Milagros Conrad", "gender": "female"
        }]

for a_data in data:
    result = es.index(index='my-index', body=a_data)
    # print(result)

body = {
    "query": {
        "bool":{
            "must":
                [{
                    "match":{
                        "gender": "male"
                    }
                },
                {
                    "range":{
                        "age":{
                            "gte":25
                        }
                    }
                }
                
                ]
            }
        }
    }

res = es.search(index='my-index',body=body)
print(res)


"""To show all index in elasticsearch."""
print(es.indices.get_alias("*"))