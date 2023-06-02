"""
This file puts constraints on the cost of production.
Only samples that are less than 982.97 (By manufacturer) Rub per sample are considered.
"""

def evaluate_constraint(x):
    """
    Evaluates the cost constraint for a given input vector x.
    """
    time, gas, power, speed, hatch, energy, angle = x
    V = 8 * 8 * 10  # sample volume, mm3
    Tl = 0.14  # recoating time per sample, sec
    H = 10  # height of part, mm
    Cmc = 3206  # hourly operating cost $RUB/h
    Emc = 3.244  # energy consumption by machine, kW
    Ce = 7.15  # electricity rate $RUB/kWh
    t = 0.02  # layer thickness, mm

    denominator = speed * hatch * t
    if denominator != 0:
        Cost = (V / denominator + H / t * Tl * Cmc / 3600) + (V / denominator + H / t * Tl) * Emc * Ce / 3600
    else:
        Cost = 1e10  # Set Cost to infinity when denominator is zero

    g = Cost - 982.97  # Cost <= 982.97
    return g  # non-positive value satisfies the constraint

