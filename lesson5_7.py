#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import mean
import json

# =================
print(">> Task 7")

def calculation_of_company_analytics(file_in, file_out):

    average_profit_list = list()
    average_profit_dict = dict()
    companies_profit_dict = dict()
    company_analytics_total_list = list()

    try:
        with open(file_in, "r") as companies_table_file:
            for line in companies_table_file:
                if not line.strip() == "":
                    company_name, company_type, gain, expenses = line.split()
                    #print(f"Firm: {company_name}")
                    company_profit = float(gain) - float(expenses)
                    if company_profit > 0:
                        average_profit_list.append(company_profit)

                    companies_profit_dict[company_name] = company_profit

    except IOError as e:
        print(f"Oops! got exception: {e}")

    print(f"Companies profit: {companies_profit_dict}")

    average_profit_dict["average_profit"] = mean(average_profit_list)
    print(f"Average profit is: {average_profit_dict}")

    company_analytics_total_list.append(companies_profit_dict)
    company_analytics_total_list.append(average_profit_dict)

    print(f"Total company analytics: {company_analytics_total_list}")

    company_analytics_total_json = json.dumps(company_analytics_total_list)

    print(f"Total company analytics in json format: {company_analytics_total_json}")

    try:
        with open(file_out, "w") as company_analytics_in_json_file:
            company_analytics_in_json_file.write(company_analytics_total_json)

    except IOError as e:
        print(f"Oops! got exception: {e}")

    return 0


calculation_of_company_analytics("text_file_for_task_7.txt", "company_analytics_json_task_7.txt")
print("It's all done")
