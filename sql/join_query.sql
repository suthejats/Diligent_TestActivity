SELECT
    u.name AS user_name,
    o.order_id,
    o.order_date,
    p.product_name AS product_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS total_value,
    pay.method,
    pay.amount
FROM
    users u
JOIN
    orders o ON u.user_id = o.user_id
JOIN
    order_items oi ON o.order_id = oi.order_id
JOIN
    products p ON oi.product_id = p.product_id
JOIN
    payments pay ON o.order_id = pay.order_id
WHERE
    pay.status = 'success'
ORDER BY
    o.order_date DESC;
