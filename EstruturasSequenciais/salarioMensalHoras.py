import locale

ganhoPorHora = float(input("Quanto você ganha por hora: "))
horas = int(input("Horas trabalhadas por mês: "))

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
salario = locale.currency(ganhoPorHora*horas, symbol=False)

print("Seu salário deve ser de R$" + salario)