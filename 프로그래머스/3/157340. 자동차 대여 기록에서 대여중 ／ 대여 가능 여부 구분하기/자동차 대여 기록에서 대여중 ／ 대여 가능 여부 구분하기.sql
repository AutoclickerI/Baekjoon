-- 코드를 입력하세요
SELECT CAR_ID, max(case when START_DATE <= DATE('2022-10-16') and DATE('2022-10-16') <= END_DATE then '대여중'
               else '대여 가능'
               end) as AVAILABILITY FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    Group by CAR_ID
    ORDER BY CAR_ID desc