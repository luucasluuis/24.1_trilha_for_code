def create_spend_chart(categories):
    linhas = "Percentage spent by category\n"
    spendings_per_category = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spent = sum(spendings_per_category)

    spending_rate = [spend / total_spent for spend in spendings_per_category]
    for i in range(100, -1, -10):
        linhas += f"{i:>3}| "
        for rate in spending_rate:
            linhas += 'o' if rate * 100 >= i else ' '
            linhas += '  '
        linhas += '\n'

    linhas += "    " + "-" * (len(categories) * 3 + 1) + '\n'

    max_len = max(len(category.categoria) for category in categories)
    for i in range(max_len):
        linhas += "     "
        for category in categories:
            linhas += category.categoria[i].title() if i == 0 else category.categoria[i] if i < len(category.categoria) else ' '
            linhas += '  '
        linhas += '\n'

    return linhas.rstrip('\n')
