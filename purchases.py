purchases = int(input("Number of purchases: "))
tax = float(input("Sales tax: "))

customer_list = []
cost_list = []

for i in range(purchases):
    customer = input("Customer: ")
    customer_list.append(customer)
    cost = float(input("Cost: "))
    cost_list.append(cost)

def add_tax():
    taxed_list = []
    for cost in cost_list:
        taxed_list.append(cost * tax)
    return taxed_list

final_costs = {}

for i in range(purchases):
    customer = customer_list[i]
    cost = cost_list[i]
    
    taxed_cost = cost * (1 + tax)
    
    if customer in final_costs:
        final_costs[customer] += taxed_cost
    else:
        final_costs[customer] = taxed_cost

print(final_costs)


