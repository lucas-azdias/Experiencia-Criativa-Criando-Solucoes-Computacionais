from models import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def generate_seeds(db:SQLAlchemy):
    role1 = Role(name='admin')
    role2 = Role(name='waiter')
    role3 = Role(name='cashier')

    db.session.add_all([role1, role2, role3])
    db.session.commit()

    user1 = User(email = "antonio.teste@pucpr.br", username = "antoniot", password = generate_password_hash("minhasenha"))
    user2 = User(email = "joao.teste@pucpr.br", username = "joaot", password = generate_password_hash("minhasenha"))
    user3 = User(email = "marcos.teste@pucpr.br", username = "marcost", password = generate_password_hash("minhasenha"))
    user4 = User(email = "Jardel.teste@pucpr.br", username = "jardelt", password = generate_password_hash("minhasenha"))
    user5 = User(email = "Joaquim.teste@pucpr.br", username = "joaquimt", password = generate_password_hash("minhasenha"))
    user6 = User(email = "Valter.teste@pucpr.br", username = "valtert", password = generate_password_hash("minhasenha"))
    
    user1.roles = [role1,role2,role3]
    user2.roles = [role2,]
    user3.roles = [role3,]
    user4.roles = [role2,]
    user5.roles = [role2,]
    user6.roles = [role2,]

    db.session.add_all([user1, user2, user3, user4, user5, user6])
    db.session.commit()
    
    person1 = Person(name = "Antonio Test", cpf = "01010101011", gender = "M", birth_date = datetime.strptime("2002-01-01", "%Y-%m-%d"), phone = "41999999999", created_at = datetime.today())
    person2 = Person(name = "Maria Test", cpf = "01010101012", gender = "F", birth_date = datetime.strptime("2001-01-01", "%Y-%m-%d"), phone = "41999999998", created_at = datetime.today())
    person3 = Person(name = "Marcos Test", cpf = "01010101013", gender = "M", birth_date = datetime.strptime("2000-01-01", "%Y-%m-%d"), phone = "41999999997", created_at = datetime.today())
    person4 = Person(name = "Joaquim Test", cpf = "01010101014", gender = "M", birth_date = datetime.strptime("2004-01-01", "%Y-%m-%d"), phone = "41999999996", created_at = datetime.today())
    person5 = Person(name = "Valter Test", cpf = "01010101015", gender = "M", birth_date = datetime.strptime("2005-01-01", "%Y-%m-%d"), phone = "41999999995", created_at = datetime.today())
    person6 = Person(name = "Solange Test", cpf = "01010101016", gender = "F", birth_date = datetime.strptime("2004-01-01", "%Y-%m-%d"), phone = "41999999994", created_at = datetime.today())
    person7 = Person(name = "Rosimere Test", cpf = "01010101017", gender = "F", birth_date = datetime.strptime("2002-01-01", "%Y-%m-%d"), phone = "41999999993", created_at = datetime.today())
    person8 = Person(name = "Jardel Test", cpf = "01010101018", gender = "M", birth_date = datetime.strptime("2003-01-01", "%Y-%m-%d"), phone = "41999999992", created_at = datetime.today())
    person9 = Person(name = "Francisco Test", cpf = "01010101019", gender = "M", birth_date = datetime.strptime("1990-01-01", "%Y-%m-%d"), phone = "41999999991", created_at = datetime.today())
    person10 = Person(name = "Marcela Test", cpf = "01010101010", gender = "F", birth_date = datetime.strptime("1999-01-01", "%Y-%m-%d"), phone = "41999999990", created_at = datetime.today())
    person11 = Person(name = "Joao Test", cpf = "01010101000", gender = "M", birth_date = datetime.strptime("1993-01-01", "%Y-%m-%d"), phone = "41999999990", created_at = datetime.today())
    
    db.session.add_all([person1, person2, person3, person4, person5, person6, person7, person8, person9,person10,person11])
    db.session.commit()
    
    employee1 = Employee(id = person1.id, user_id = user1.id, created_at = datetime.today())
    employee2 = Employee(id = person3.id, user_id = user3.id, created_at = datetime.today())
    employee3 = Employee(id = person4.id, user_id = user5.id, created_at = datetime.today())
    employee4 = Employee(id = person5.id, user_id = user6.id, created_at = datetime.today())
    employee5 = Employee(id = person8.id, user_id = user4.id, created_at = datetime.today())
    employee6 = Employee(id = person11.id, user_id = user2.id, created_at = datetime.today())

    db.session.add_all([employee1, employee2, employee3, employee4, employee5, employee6])
    db.session.commit()


    general_service1 = GeneralService(id = employee1.id, salary = 2000.00)
    general_service2 = GeneralService(id = employee2.id, salary = 2350.00)

    db.session.add_all([general_service1, general_service2])
    db.session.commit()

    waiter1 = Waiter(id = employee3.id , hour_price = 80.00)
    waiter2 = Waiter(id = employee4.id , hour_price = 80.00)
    waiter3 = Waiter(id = employee5.id , hour_price = 80.00)
    waiter4 = Waiter(id = employee6.id , hour_price = 80.00)

    db.session.add_all([waiter1, waiter2, waiter3,waiter4])
    db.session.commit()

    client1 = Client(id = person1.id, created_at = datetime.today())
    client2 = Client(id = person2.id, created_at = datetime.today())
    client3 = Client(id = person3.id, created_at = datetime.today())
    client4 = Client(id = person4.id, created_at = datetime.today())
    client5 = Client(id = person5.id, created_at = datetime.today())
    client6 = Client(id = person6.id, created_at = datetime.today())
    client7 = Client(id = person7.id, created_at = datetime.today())
    client8 = Client(id = person8.id, created_at = datetime.today())
    client9 = Client(id = person9.id, created_at = datetime.today())
    client10 = Client(id = person10.id, created_at = datetime.today())
    client11 = Client(id = person11.id, created_at = datetime.today())

    db.session.add_all([client1, client2, client3, client4, client5, client6, client7, client8, client9,client10,client11])
    db.session.commit()

    ticket1 = Ticket(client_id = client1.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket2 = Ticket(client_id = client2.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket3 = Ticket(client_id = client3.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket4 = Ticket(client_id = client4.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket5 = Ticket(client_id = client5.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket6 = Ticket(client_id = client6.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket7 = Ticket(client_id = client7.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket8 = Ticket(client_id = client1.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket9 = Ticket(client_id = client2.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket10 = Ticket(client_id = client3.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket11 = Ticket(client_id = client4.id, creation_datetime = datetime.now(), purchase_total = None, items = None)
    ticket12 = Ticket(client_id = client5.id, creation_datetime = datetime.now(), purchase_total = None, items = None)

    db.session.add_all([ticket1, ticket2, ticket3, ticket4, ticket5, ticket6, ticket7, ticket8, ticket9,ticket10,ticket11,ticket12])
    db.session.commit()

    product1 = Product(name = "Batata Frita", current_price = 12.00, available_quantity = 100)
    product2 = Product(name = "Executivo Frango", current_price = 22.00, available_quantity = 100)
    product3 = Product(name = "Cerveja Lata", current_price = 8.00, available_quantity = 100)
    product4 = Product(name = "Cerveja Garrafa", current_price = 15.00, available_quantity = 100)
    product5 = Product(name = "Pastel Carne", current_price = 7.00, available_quantity = 100)
    product6 = Product(name = "Executivo Carne", current_price = 32.00, available_quantity = 100)
    product7 = Product(name = "Mignon Acebolado", current_price = 40.00, available_quantity = 100)
    product8 = Product(name = "Alcatra e Fritas Rústica", current_price = 49.00, available_quantity = 100)
    product9 = Product(name = "Hamburguer Combo 1", current_price = 23.00, available_quantity = 100)
    product10 = Product(name = "Hamburguer Combo 2", current_price = 26.00, available_quantity = 100)
    product11 = Product(name = "Sobremesa Pudim", current_price = 14.00, available_quantity = 100)
    product12 = Product(name = "Hamburguer Combo 5", current_price = 54.00, available_quantity = 100)

    db.session.add_all([product1, product2, product3, product4, product5, product6, product7, product8, product9,product10,product11,product12])
    db.session.commit()

    order1 = Order(ticket_id = ticket1.id, product_id = product1.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product1.current_price, quantity = 3)
    order2 = Order(ticket_id = ticket1.id, product_id = product2.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product2.current_price, quantity = 2)
    order3 = Order(ticket_id = ticket1.id, product_id = product3.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product3.current_price, quantity = 1)
    order4 = Order(ticket_id = ticket1.id, product_id = product4.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product4.current_price, quantity = 1)
    order5 = Order(ticket_id = ticket1.id, product_id = product5.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product5.current_price, quantity = 1)
    order6 = Order(ticket_id = ticket1.id, product_id = product6.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product6.current_price, quantity = 3)
    order7 = Order(ticket_id = ticket1.id, product_id = product7.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product7.current_price, quantity = 2)
    order8 = Order(ticket_id = ticket1.id, product_id = product8.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product8.current_price, quantity = 3)
    order9 = Order(ticket_id = ticket1.id, product_id = product9.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product9.current_price, quantity = 6)
    
    db.session.add_all([order1, order2, order3, order4, order5, order6, order7, order8, order9])
    db.session.commit()

    order10 = Order(ticket_id = ticket2.id, product_id = product10.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product10.current_price, quantity = 4)
    order11 = Order(ticket_id = ticket2.id, product_id = product11.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product11.current_price, quantity = 1)
    order12 = Order(ticket_id = ticket2.id, product_id = product12.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product12.current_price, quantity = 2)
    order13 = Order(ticket_id = ticket2.id, product_id = product1.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product1.current_price, quantity = 4)
    order14 = Order(ticket_id = ticket2.id, product_id = product2.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product2.current_price, quantity = 2)
    order15 = Order(ticket_id = ticket3.id, product_id = product1.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product1.current_price, quantity = 2)
    order16 = Order(ticket_id = ticket3.id, product_id = product2.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product2.current_price, quantity = 1)
    order17 = Order(ticket_id = ticket3.id, product_id = product3.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product3.current_price, quantity = 1)
    order18 = Order(ticket_id = ticket3.id, product_id = product4.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product4.current_price, quantity = 2)
    order19 = Order(ticket_id = ticket4.id, product_id = product5.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product5.current_price, quantity = 3)
    
    db.session.add_all([order10, order11, order12, order13, order14, order15, order16, order17, order18, order19])
    db.session.commit()
    
    order20 = Order(ticket_id = ticket4.id, product_id = product6.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product6.current_price, quantity = 4)
    order21 = Order(ticket_id = ticket5.id, product_id = product7.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product7.current_price, quantity = 5)
    order22 = Order(ticket_id = ticket5.id, product_id = product8.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product8.current_price, quantity = 8)
    order23 = Order(ticket_id = ticket5.id, product_id = product9.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product9.current_price, quantity = 7)
    order24 = Order(ticket_id = ticket6.id, product_id = product10.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product10.current_price, quantity = 5)
    order25 = Order(ticket_id = ticket6.id, product_id = product11.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product11.current_price, quantity = 3)
    order26 = Order(ticket_id = ticket6.id, product_id = product12.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product12.current_price, quantity = 5)
    order27 = Order(ticket_id = ticket7.id, product_id = product1.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product1.current_price, quantity = 3)
    order28 = Order(ticket_id = ticket7.id, product_id = product2.id, waiter_id = waiter4.id, payment_id = None, creation_datetime = datetime.now(), product_price = product2.current_price, quantity = 2)
    order29 = Order(ticket_id = ticket7.id, product_id = product3.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product3.current_price, quantity = 1)

    db.session.add_all([order20, order21, order22, order23, order24, order25, order26, order27, order28, order29])
    db.session.commit()
    
    order30 = Order(ticket_id = ticket8.id, product_id = product4.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product4.current_price, quantity = 2)
    order31 = Order(ticket_id = ticket9.id, product_id = product5.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product5.current_price, quantity = 10)
    order32 = Order(ticket_id = ticket9.id, product_id = product6.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product6.current_price, quantity = 1)
    order33 = Order(ticket_id = ticket10.id, product_id = product7.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product7.current_price, quantity = 4)
    order34 = Order(ticket_id = ticket11.id, product_id = product8.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product8.current_price, quantity = 5)
    order35 = Order(ticket_id = ticket8.id, product_id = product1.id, waiter_id = waiter3.id, payment_id = None, creation_datetime = datetime.now(), product_price = product1.current_price, quantity = 2)
    order36 = Order(ticket_id = ticket9.id, product_id = product2.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product2.current_price, quantity = 1)
    order37 = Order(ticket_id = ticket9.id, product_id = product3.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product3.current_price, quantity = 3)
    order38 = Order(ticket_id = ticket10.id, product_id = product4.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product4.current_price, quantity = 2)
    order39 = Order(ticket_id = ticket11.id, product_id = product5.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product5.current_price, quantity = 1)
    order40 = Order(ticket_id = ticket12.id, product_id = product10.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product10.current_price, quantity = 1)
    order41 = Order(ticket_id = ticket12.id, product_id = product11.id, waiter_id = waiter1.id, payment_id = None, creation_datetime = datetime.now(), product_price = product11.current_price, quantity = 3)
    order42 = Order(ticket_id = ticket12.id, product_id = product12.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product12.current_price, quantity = 2)
    order43 = Order(ticket_id = ticket12.id, product_id = product5.id, waiter_id = waiter2.id, payment_id = None, creation_datetime = datetime.now(), product_price = product5.current_price, quantity = 1)

    db.session.add_all([order30, order31, order32, order33, order34, order35, order36, order37, order38, order39, order40, order41, order42, order43])
    db.session.commit()


    #updating tickets number of idb.session.add_all([tems and purchase total
    info1 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket1.id).first()
    ticket1.items = info1[0]
    ticket1.purchase_total = info1[1]

    info2 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket2.id).first()
    ticket2.items = info2[0]
    ticket2.purchase_total = info2[1]
    
    info3 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket3.id).first()
    ticket3.items = info3[0]
    ticket3.purchase_total = info3[1]
    
    info4 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket4.id).first()
    ticket4.items = info4[0]
    ticket4.purchase_total = info4[1]
    

    info5 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket5.id).first()
    ticket5.items = info5[0]
    ticket5.purchase_total = info5[1]
    

    info6 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket6.id).first()
    ticket6.items = info6[0]
    ticket6.purchase_total = info6[1]
    

    info7 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket7.id).first()
    ticket7.items = info7[0]
    ticket7.purchase_total = info7[1]
    

    info8 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket8.id).first()
    ticket8.items = info8[0]
    ticket8.purchase_total = info8[1]
    

    info9 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket9.id).first()
    ticket9.items = info9[0]
    ticket9.purchase_total = info9[1]
    

    info10 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket10.id).first()
    ticket10.items = info10[0]
    ticket10.purchase_total = info10[1]
    

    info11 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket11.id).first()
    ticket11.items = info11[0]
    ticket11.purchase_total = info11[1]
    

    info12 = db.session.query(db.func.count().label('items'), db.func.sum(Order.product_price).label('total')).filter(Order.ticket_id == ticket12.id).first()
    ticket12.items = info12[0]
    ticket12.purchase_total = info12[1]

    billing_form1 = BillingForm(name='crédito')
    billing_form2 = BillingForm(name='débito')
    billing_form3 = BillingForm(name='pix')
    billing_form4 =  BillingForm(name='dinheiro')

    db.session.add_all([billing_form1, billing_form2, billing_form3, billing_form4])
    db.session.commit()

    billing1 = Billing(value = ticket1.purchase_total, billing_date = datetime.now())
    billing2 = Billing(value = ticket2.purchase_total, billing_date = datetime.now())
    billing3 = Billing(value = ticket3.purchase_total, billing_date = datetime.now())
    billing4 = Billing(value = ticket4.purchase_total, billing_date = datetime.now())
    billing5 = Billing(value = ticket5.purchase_total, billing_date = datetime.now())
    billing6 = Billing(value = ticket6.purchase_total, billing_date = datetime.now())
    billing7 = Billing(value = ticket7.purchase_total, billing_date = datetime.now())
    billing8 = Billing(value = ticket8.purchase_total, billing_date = datetime.now())
    billing9 = Billing(value = ticket9.purchase_total, billing_date = datetime.now())
    billing10 = Billing(value = ticket10.purchase_total, billing_date = datetime.now())
    billing11 = Billing(value = ticket11.purchase_total, billing_date = datetime.now())
    billing12 = Billing(value = ticket12.purchase_total, billing_date = datetime.now())

    
    db.session.add_all([billing1, billing2, billing3, billing4, billing5,billing6,billing7,billing8,billing9,billing10,billing11,billing12])
    db.session.commit()

    billing_billing_forms1 = BillingBillingForms(billing_id = billing1.id, billing_form_id = billing_form1.id, value = ticket1.purchase_total)
    billing_billing_forms2 = BillingBillingForms(billing_id = billing2.id, billing_form_id = billing_form1.id, value = ticket2.purchase_total)
    billing_billing_forms3 = BillingBillingForms(billing_id = billing3.id, billing_form_id = billing_form2.id, value = ticket3.purchase_total)
    billing_billing_forms4 = BillingBillingForms(billing_id = billing4.id, billing_form_id = billing_form2.id, value = ticket4.purchase_total)
    billing_billing_forms5 = BillingBillingForms(billing_id = billing5.id, billing_form_id = billing_form2.id, value = ticket5.purchase_total)
    billing_billing_forms6 = BillingBillingForms(billing_id = billing6.id, billing_form_id = billing_form3.id, value = ticket6.purchase_total)
    billing_billing_forms7 = BillingBillingForms(billing_id = billing7.id, billing_form_id = billing_form3.id, value = ticket7.purchase_total)
    billing_billing_forms8 = BillingBillingForms(billing_id = billing8.id, billing_form_id = billing_form3.id, value = ticket8.purchase_total)
    billing_billing_forms9 = BillingBillingForms(billing_id = billing9.id, billing_form_id = billing_form3.id, value = ticket9.purchase_total)
    billing_billing_forms10 = BillingBillingForms(billing_id = billing10.id, billing_form_id = billing_form4.id, value = ticket10.purchase_total)
    billing_billing_forms11 = BillingBillingForms(billing_id = billing11.id, billing_form_id = billing_form4.id, value = ticket11.purchase_total)
    billing_billing_forms12 = BillingBillingForms(billing_id = billing12.id, billing_form_id = billing_form4.id, value = ticket12.purchase_total)
    
    db.session.add_all([billing_billing_forms1, billing_billing_forms2, billing_billing_forms3, billing_billing_forms4, billing_billing_forms5,billing_billing_forms6,billing_billing_forms7,billing_billing_forms8,billing_billing_forms9,billing_billing_forms10,billing_billing_forms11,billing_billing_forms12])
    db.session.commit()

    #IOT

    device1 = Device(brand = "ESP32", model = "ESP32", name = "Umidade", voltage = 5, description = "Sendor de umidade com medida em percentual")
    device2 = Device(brand = "ESP32", model = "ESP32", name = "Temperatura", voltage = 5, description = "Sendor de temperatura com unidade de medida em graus celsios")
    device3 = Device(brand = "ESP32", model = "ESP32", name = "Infravermelhor", voltage = 5, description = "Sendor de pequenas distâncias infravermelho")
    device4 = Device(brand = "ESP32", model = "ESP32", name = "Luminosidade", voltage = 5, description = "Sendor de luminosidade (LDR)")
    device5 = Device(brand = "ESP32", model = "ESP32", name = "Movimento/Presença", voltage = 5, description = "Sendor de movimento/presença, retornando booleano pra detecção ou não de objetos em movimento")
    device6 = Device(brand = "ESP32", model = "ESP32", name = "Lampada LED", voltage = 5, description = "Atuador - Lâmpada led")
    device7 = Device(brand = "ESP32", model = "ESP32", name = "Motor Corrente Contínua", voltage = 5, description = "Motor de corrente contínua com caixa de redução")
    device8 = Device(brand = "ESP32", model = "ESP32", name = "Motor de Passo", voltage = 5, description = "Motor de passo para tarefas específicas e com precisão de movimento")
    device9 = Device(brand = "ESP32", model = "ESP32", name = "Servo Motor", voltage = 5, description = "Servo motor para movimentos específicos 180 graus")

    db.session.add_all([device1, device2, device3, device4, device5,device6,device7,device8,device9])
    db.session.commit()

    sensor1 = Sensor(id = device1.id, measure = "%")
    sensor2 = Sensor(id = device2.id, measure = "ºC")
    sensor3 = Sensor(id = device3.id, measure = "cm")
    sensor4 = Sensor(id = device4.id, measure = "Lumens")
    sensor5 = Sensor(id = device5.id, measure = "")

    db.session.add_all([sensor1, sensor2, sensor3, sensor4, sensor5])
    db.session.commit()
    data = {}
    data["id"] = sensor1.id
    data["brand"] = device1.brand
    data["name"] = device1.name
    data["model"] = "Teste Update"
    data["voltage"] = device1.voltage
    data["description"] = device1.description
    data["is_active"] = False
    data["measure"] = "Measure Teste"
    Sensor.update_sensor(data)

    actuator1 = Actuator(id = device6.id, actuator_type = None)
    actuator2 = Actuator(id = device7.id, actuator_type = "Chassi Robótico")
    actuator3 = Actuator(id = device8.id, actuator_type = "ULN2003")
    actuator4 = Actuator(id = device9.id, actuator_type = None)

    db.session.add_all([actuator1, actuator2, actuator3, actuator4])
    db.session.commit()
    
