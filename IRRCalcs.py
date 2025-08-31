import numpy as np

def present_value_from_cashflows(cash_flows, discount_rate):
    """
    Calculate the present value of a series of cash flows given a discount rate.

    Parameters:
    cash_flows (list or np.array): A list or array of cash flows where the index represents the time period.
    discount_rate (float): The discount rate as a decimal (e.g., 0.05 for 5%).

    Returns:
    float: The present value of the cash flows.
    """
    cash_flows = np.array(cash_flows)
    periods = np.arange(len(cash_flows))
    present_value = np.sum(cash_flows / (1 + discount_rate) ** periods)

    return present_value

def present_value_by_rate (cash_flows, minimum_rate=0.0, maximum_rate=1.0, step=0.0001):
    """
    Calculate the present value of cash flows over a range of discount rates.

    Parameters:
    cash_flows (list or np.array): A list or array of cash flows where the index represents the time period.
    minimum_rate (float): The minimum discount rate to consider (default is 0.0).
    maximum_rate (float): The maximum discount rate to consider (default is 1.0).
    step (float): The increment step for the discount rate (default is 0.0001).

    Returns:
    dict: A dictionary with discount rates as keys and their corresponding present values as values.
    """
    rates = np.arange(minimum_rate, maximum_rate + step, step)
    present_values = {rate: present_value_from_cashflows(cash_flows, rate) for rate in rates}

    return present_values

