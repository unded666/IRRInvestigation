from fontTools.unicodedata import block

import IRRCalcs as IRC
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Example cash flows: Initial investment of -1000, followed by returns of 300, 400, 500 over 3 periods
    cash_flows = [-1000, 300, 400, 200, -300, 600, 700, 200, 200, 200]

    # Calculate present values over a range of discount rates
    min_rate = 0
    max_rate = 2
    step = 0.001
    pv_dict = IRC.present_value_by_rate(cash_flows, min_rate, max_rate, step)

    # Plot the results
    rates = list(pv_dict.keys())
    # convert rates to percentage representation
    rates = [rate * 100 for rate in rates]
    present_values = list(pv_dict.values())

    plt.figure(figsize=(10, 6))
    plt.plot(rates, present_values, label='Present Value', color='blue')
    plt.axhline(0, color='red', linestyle='--', label='Zero Present Value')
    plt.title('Present Value of Cash Flows vs. Discount Rate')
    plt.xlabel('Discount Rate (%)')
    plt.ylabel('Present Value')
    plt.legend()
    plt.grid(True)
    plt.show(block=True)

if __name__ == "__main__":
    main()

