use pjbl_exp_criativa;

# USER
insert into users(username, name, email, phone, password, is_admin, date_creation, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date)
values ("bafome", "Bafomé Pinto Carvalho", "bafome@gmail.com", "+5511999998888", "jesus", true, "2023-04-21", "1234123412341234", "Bafomé P Carvalho", "123", 01, 2040);

# PAYMENT
insert into payments(id_user, value, month, year, is_paid, date_payment, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date)
values (1, 19.99, 05, 2023, true, "2023-05-01", "1234123412341234", "Bafomé P Carvalho", "123", 01, 2040);

# SENSOR
insert into sensors(id_user, name, model, brand, measure, voltage, register_date)
values (1, "Sensor", "Soil humidity", "China", "%", 3.3, "2023-06-01 11:50:01");
