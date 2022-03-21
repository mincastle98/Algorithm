SELECT c.first_name as 이름, c.last_name as 성, price.누적숙박비
FROM customers as c, (SELECT r.customer_id, rooms.price * r.period as 누적숙박비
                        FROM rooms join (SELECT room_no, customer_id, date_out - date_in + 1 as period
                                        FROM reservations) as r
                            on rooms.room_no = r.room_no) as price
WHERE c.customer_id = price.customer_id