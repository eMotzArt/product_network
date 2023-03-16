# Product-network

<hr>
<center> 

<b>Возможности:</b>
* Создать предприятия (завод, ритейлерскую сеть, индивидуального предпринимателя) <br>
* Для завода: выпустить товар на рынок <br>
* Для ритейлера\ИП: заказать товар у своего поставщика <br>
* При заказе вся сумма за товар записывается заказчику в долг <br>


</center>

<hr/>

### Stack: Django, Python3.10, PostgreSQL

## Запуск

```sh
docker-compose up -d --build
```
<hr/>

## Логика
#### Этап1 -  регистрация предприятия
```
url-post: auth/reg

{   
    "name": "zavod1",
    "email": "zavod1@test.ru",
    "password": "zavod1password",
    "contact": {
        "street": "fabrician",
        "house": 1,
        "city": "Moscow",
        "country": "Russia"
    },
    "role": 0
}
```
#### role - роль предприятия. 0 - завод, 1 - ретейлерская сеть, 2 - Индивидуальный Предприниматель
#### При регистрации ролей 1 и 2 требуется указать в теле запроса на регистрацию ID поставщика (пример: "supplier": 1)
#### Возможность завода:
* Выпускать товар
```
url-post: goods/make


{
    "name": "Supply name",
    "model": "Supply model",
    "count": 1000,
    "price": 444.25
}
```

* Просматривать свой склад (url-get: goods/storage)
#### Возможности ретейлера и ИП:
* Посмотреть свой склад (url-get: goods/storage)
* Посмотреть склад поставщика (url-get: goods/supplier)
* Заказать у поставщика товар
```
url-post: goods/order


{
    "name": "Supply name",
    "model": "Supply model",
    "count": 255
}
```
#### Просмотр всех предприятий (url-get: enterprises)
#### Просмотр всех предприятий с фильтрацией по стране (url-get: enterprises?country=Russia)

