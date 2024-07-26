# Сдача второй части проекта
![image](https://github.com/user-attachments/assets/0698de51-738e-4702-9348-93396adf6821)

## SQL запрос первый:
SELECT cour.login, COUNT(ord."inDelivery")  
FROM "Couriers" AS cour JOIN "Orders" AS ord ON cour.id = ord."courierId"  
WHERE ord."inDelivery" = true  
GROUP BY cour.login;

## SQL запрос второй:
SELECT 
    track, 
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders";
