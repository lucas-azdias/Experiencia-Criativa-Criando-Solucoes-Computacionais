# Lucas Azevedo Dias

from flask import Blueprint, request, render_template, url_for
from json import dumps


payment = Blueprint("payment", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

# Informações vindas do servidor
garcons = sorted([(1, 18), (2, 25), (3, 40)]) # (Id_garcom, Valor_hora_garcom)
funcs = sorted([(4, 500), (5, 700), (8, 340)]) # (Id_func, Salario)

# Informações salvas no servidor
hrs_garcons = list()
hrs_garcons_pagos = list()
salarios_funcs_pagos = list()


@payment.route("/")
def payment_index():
    return render_template("/payment/payment_index.html")


@payment.route("/register_horas_garcons")
def payment_register_horas_garcons():
    id_garcons = [garcom[0] for garcom in garcons]
    return render_template("/payment/register_horas_garcons.html", id_garcons=id_garcons)


@payment.route("/save_horas_garcom", methods=["POST"])
def payment_save_horas_garcom():
    id_garcom = request.form.get("id_garcom")
    num_horas = request.form.get("num_horas")
    cur_time = request.form.get("cur_time")

    hrs_garcons.append((int(id_garcom), float(num_horas), cur_time))

    return url_for("payment.payment_register_horas_garcons")


@payment.route("/payment_horas_garcons")
def payment_payment_horas_garcons():
    #id_garcons = sorted(set([hrs_garcom[0] for hrs_garcom in hrs_garcons].__iter__()))
    id_garcons = [garcom[0] for garcom in garcons]
    pagos = list()
    for hrs_garcom_pago in hrs_garcons_pagos:
        hrs = 0
        for l in hrs_garcom_pago[1]:
            hrs += l[0]
        pagos.append((hrs_garcom_pago[0], hrs, hrs_garcom_pago[2], hrs_garcom_pago[3]))

    return render_template("/payment/payment_horas_garcons.html", id_garcons=id_garcons, pagos=pagos)


@payment.route("/get_hrs_garcom_by_id", methods=["POST"])
def payment_get_hrs_garcom_by_id():
    id_garcom = int(request.form.get("id_garcom_select"))
    response = list()
    for item in hrs_garcons:
        if item[0] == id_garcom:
            response.append(item)
    return dumps(sorted(response))


@payment.route("/get_valor_hora_garcom_by_id", methods=["POST"])
def payment_get_valor_hora_garcom_by_id():
    id_garcom = int(request.form.get("id_garcom_select"))
    response = list()
    for garcom in garcons:
        if garcom[0] == id_garcom:
            response = garcom
    return dumps(response)


@payment.route("/save_payment_horas_garcom", methods=["POST"])
def payment_save_payment_horas_garcom():
    id_garcom = int(request.form.get("id_garcom"))
    valor_num = float(request.form.get("valor_num"))
    cur_time = request.form.get("cur_time")

    hrs_garcom = list()
    for item in hrs_garcons:
        if item[0] == id_garcom:
            hrs_garcom.append(item)

    valor_total = sum([(item[1]) for item in hrs_garcom])
    valor_hora = 0
    for garcom in garcons:
        if garcom[0] == id_garcom:
            valor_hora = garcom[1]
    valor_total *= valor_hora
    
    pagos = list()
    if valor_total == valor_num:
        for item in hrs_garcom:
            hrs_garcons.remove(item)
            pagos.append([item[1], item[2]])
        hrs_garcons_pagos.append((id_garcom, pagos, valor_hora, cur_time))

    return url_for("payment.payment_payment_horas_garcons")


@payment.route("/payment_funcionarios")
def payment_payment_funcionarios():
    id_funcs = [func[0] for func in funcs]
    return render_template("/payment/payment_funcionarios.html", id_funcs=id_funcs, salarios_funcs_pagos=salarios_funcs_pagos)


@payment.route("/get_salario_funcionario", methods=["POST"])
def payment_get_salario_funcionario():
    id_func = int(request.form.get("id_func_select"))
    response = list()
    for func in funcs:
        if func[0] == id_func:
            response = func
    return dumps(response)


@payment.route("/save_payment_funcionario", methods=["POST"])
def payment_save_payment_funcionario():
    id_func = int(request.form.get("id_func"))
    valor_num = float(request.form.get("valor_num"))
    cur_time = request.form.get("cur_time")

    valor_total = 0
    for func in funcs:
        if func[0] == id_func:
            valor_total = func[1]

    if valor_total == valor_num:
        salarios_funcs_pagos.append((id_func, valor_total, cur_time))

    return url_for("payment.payment_payment_funcionarios")
