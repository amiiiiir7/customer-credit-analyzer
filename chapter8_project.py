# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:37:25 2026

@author: Amir
"""


def risk_category(score):
    if score >= 800:
        return 'Low Risk'
    elif score >= 700:
        return 'Medium Risk'
    else:
        return 'High Risk'


def average_score(scores):
    total = sum(scores)
    length = len(scores)
    return total / length


def highest_score(scores):
    return max(scores)


def customer_report(name, score):
    rank = risk_category(score)
    return f"{name.title()} | Score: {score} | Risk: {rank}"


customers_list = {
    "alex": 720,
    "sara": 810,
    "reza": 650,
    "mina": 900,
    "john": 785
}

for cus_name, cus_score in customers_list.items():
    print(customer_report(cus_name, cus_score))


scoress = (customers_list.values())


print(f"Average Score: {average_score(scoress)}")
print(f"Highest Score: {highest_score(scoress)}")
