# Scooter Rent Project

Оксана Кубликова 27-я когорта финальный проект курса "Инженер по тестированию плюс".

## Как запустить автотест
1. Установливаю зависимости: `pip install requests`.
2. Запускаю тест: `python test_order_api.py`.

### Задание 1
```sql
SELECT "Couriers".login, COUNT("Orders".id) AS orders_in_delivery
FROM "Couriers"
JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders".inDelivery = true
GROUP BY "Couriers".login;
Задание 2 
SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN inDelivery = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";