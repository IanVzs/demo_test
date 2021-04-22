select user_list, sum(rounds) as sm from chats group by user_list order by sm desc limit 10;

select item_id, sum(cnt) as sm from sales_record group by item_id order by sm desc limit 10;
select item_id, sum(cnt) as sm from sales_record group by cus_id, item_id order by sm desc limit 10;
