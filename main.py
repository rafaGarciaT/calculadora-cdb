from datetime import datetime, timedelta
import numpy as np
from models import cdb
import api_calls
import utils
import calculations

date = utils.date_info()

cdb1 = cdb.Cdb(1, "2025-09-23", 400)
dias_uteis = cdb1.business_days_count()
dias = cdb1.calendar_days_count()

cdi_dia = round(api_calls.get_cdi(date["d"], date["m"], date["a"]), 4)
cdi_dia = cdi_dia / 100
print("CDI diário = " + str(cdi_dia) + "% ao dia")

cdi_anu = calculations.calc_cdi_anual(cdi_dia)
print("CDI anual = " + str(cdi_anu) + "% ao ano")

ipca = api_calls.get_ipca(date["d"], date["m"], date["a"])
ipca_acumulado = (1 + ipca["valor"] / 100).prod() - 1

pf_bruto = (1 + (cdi_dia * cdb1.percentage)) ** dias_uteis - 1
print("Rendimento Bruto = " + str(pf_bruto) + "%")

rendimento = (4000.00 * pf_bruto)
print("Rendimento Bruto = " + str(rendimento))

pf_liquido = rendimento * calculations.calc_tabela_reg(cdb1.calendar_days_count())
print("Rendimento Líquido = " + str(rendimento - pf_liquido))

rendimento_real = (1 + (rendimento - pf_liquido)) / (1 + int(ipca_acumulado)) - 1
print("Rendimento Real = " + str(rendimento_real))
