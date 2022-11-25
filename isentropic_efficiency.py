import inputs
import math


def getefficiency(pressureratio):
    if inputs.isentropic_efficiency == "Estimate":
        if inputs.compressor_type == "Screw":
            isentropic_efficiency_max = 0.75
        elif inputs.compressor_type == "Scroll":
            isentropic_efficiency_max = 0.73
        elif inputs.compressor_type == "Reciprocating":
            isentropic_efficiency_max = 0.72
        elif inputs.compressor_type == "Centrifugal":
            isentropic_efficiency_max = 0.77
        elif inputs.compressor_type == "Unknown":
            isentropic_efficiency_max = 0.70

        delta = pressureratio - inputs.ideal_pressure_ratio
        isentropic_efficiency = -0.01 * math.pow(delta, 2) + isentropic_efficiency_max

    elif inputs.isentropic_efficiency == "Value":
        isentropic_efficiency = inputs.isentropic_efficiency_val / 100

    elif inputs.isentropic_efficiency == "Do not include in calculation":
        isentropic_efficiency = 1

    return isentropic_efficiency
