# A ideia é criar um algoritmo para acompanhamento financeiro
# Com a criação da classe 'category' é possivel acompanhar a
# movimentação em cada categoria como entradas (deposit), saidas
# (transfer e withdraw) no qual transfer move de uma categoria para
# outra e wihdraw somente desconta caso há o valor requerido
# Por fim, é criado mais um algoritmo para, de forma visual, criar 
# um gráfico de gastos baseado na categoria
# não excluindo a adição das dunder "repr" e "str" que possibilitam uma
# descrição das instancias

import spend_chart

class Category:
    def __init__(self, categoria):
        self.categoria = categoria
        self.ledger = []

    def __repr__(self):
        return self.categoria

    def __str__(self):
        linha1 = f"{self.categoria.capitalize():^30}\n".replace(' ', '*')
        linha2 = "\n".join([f"{item['description'][:23]:<23}{item['amount']:>7.2f}" for item in self.ledger])
        return f"{linha1}{linha2}\nTotal: {self.get_balance():.2f}"

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return 'Transação Realizada'
        return 'Transação não autorizada'

    def get_balance(self):
        return sum(transacao['amount'] for transacao in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {repr(budget_category)}")
            budget_category.deposit(amount, f"Transfer from {repr(self)}")
            return True
        return False

payment = Category('payment')
payment.deposit(3000)

groceries = Category('groceries')
payment.transfer(500, groceries)
# went to a market
groceries.withdraw(360, 'Bought some food of the list')


health_care = Category('health_care') 
payment.transfer(200, health_care)
health_care.withdraw(200, 'health care expense')

print(payment)
print(groceries)
print(health_care)
print(spend_chart.create_spend_chart([payment, groceries, health_care]))