# Product-network

<hr>

### Stack: Django, Python3.10, PostgreSQL

## API
#### Создать предприятие (завод - роль=0) - необходимо указать список товаров
```
url-post: goods/suppliers/create

{
    "contact": {
        "country": "Russia",
        "city": "Moscow",
        "street": "Fabrician",
        "house": 1,
        "email": "zavod1@test.ru"
    },
    "products": [
        {
            "name": "tovar1",
            "model": "model1"
        },
        {
            "name": "tovar1",
            "model": "model2"
        },
        {
            "name": "tovar2",
            "model": "model1"
        }
    ],
    "name": "zavod1",
    "role": 0
}
```

#### Создать предприятие (ритейлер или ИП - роль= 1 или 2 соответственно) - необходимо указать id поставщика, в списке товаров указываются id товаров
#### Важно: id товаров должны соответстовать id товаров, выпускаемых поставщиком 
```
url-post: goods/suppliers/create

{
    "provider": 17,
    "contact": {
        "country": "Russia",
        "city": "Moscow",
        "street": "Agentskaya",
        "house": 1,
        "email": "agent1@test.ru"
    },
    "products": [1, 3],
    "name": "r3",
    "role": 1
}
```
<hr />

#### Список всех поставщиков
```
url-get: goods/suppliers
```
<hr />


#### Конкретный поставщик:
```
url-get: goods/suppliers/<id>
```
<hr />


#### Удаление поставщика:
```
url-delete: goods/suppliers/<id>
```