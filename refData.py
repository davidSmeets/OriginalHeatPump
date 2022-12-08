import pickle
from scipy import interpolate
import inputs

dict_saturated_refrigerant = pickle.load(open("refrigerants_saturated", "rb"))
dict_superheated_refrigerant = pickle.load(open("refrigerants_superheated", "rb"))
saturated_refrigerant_data = dict_saturated_refrigerant[inputs.refrigerant]
superheated_refrigerant_data = dict_superheated_refrigerant[inputs.refrigerant]
saturated_refrigerant_data.columns = [
    "Pressure",
    "Temp_liq",
    "Enthalpy_liq",
    "Entropy_liq",
    "Temp_gas",
    "Enthalpy_gas",
    "Entropy_gas",
]
superheated_refrigerant_data.columns = [
    "dT_superheat",
    "Pressure",
    "Entropy",
    "Enthalpy",
    "Temperature",
]

## saturated region

# Defining variables from columns

pressure_saturated_liq = saturated_refrigerant_data["Pressure"]

pressure_saturated_gas_all = superheated_refrigerant_data["Pressure"]
pressure_saturated_gas = pressure_saturated_gas_all[0 : len(pressure_saturated_liq)]

temp_liquid_saturated = saturated_refrigerant_data["Temp_liq"]
enthalpy_liquid_saturated = saturated_refrigerant_data["Enthalpy_liq"]
entropy_liquid_saturated = saturated_refrigerant_data["Entropy_liq"]

temp_gas_saturated = saturated_refrigerant_data["Temp_gas"]
enthalpy_gas_saturated = saturated_refrigerant_data["Enthalpy_gas"]
entropy_gas_saturated = saturated_refrigerant_data["Entropy_gas"]

# Defining formulas through interpolation (1d)

pressure_saturated_liq_func = interpolate.interp1d(
    temp_liquid_saturated, pressure_saturated_liq
)  # Saturated pressure = f(saturated temperature liquid)
pressure_saturated_gas_func = interpolate.interp1d(
    temp_gas_saturated, saturated_refrigerant_data["Pressure"]
)

temp_liquid_saturated_func = interpolate.interp1d(
    pressure_saturated_liq, temp_liquid_saturated
)
enthalpy_liquid_saturated_func = interpolate.interp1d(
    pressure_saturated_liq, enthalpy_liquid_saturated
)
entropy_liquid_saturated_func = interpolate.interp1d(
    pressure_saturated_liq, entropy_liquid_saturated
)

temp_gas_saturated_func = interpolate.interp1d(
    pressure_saturated_gas, temp_gas_saturated
)
enthalpy_gas_saturated_func = interpolate.interp1d(
    pressure_saturated_gas, enthalpy_gas_saturated
)
entropy_gas_saturated_func = interpolate.interp1d(
    pressure_saturated_gas, entropy_gas_saturated
)

## superheated region ##

# Defining variables from columns

temp_superheated = superheated_refrigerant_data[
    "dT_superheat"
]  # Degrees of superheating above satured gas temperature

temperature_superheated = superheated_refrigerant_data[
    "Temperature"
]  # Saturation temperature + dT

pressure_superheated = superheated_refrigerant_data["Pressure"]
entropy_superheated = superheated_refrigerant_data["Entropy"]
enthalpy_superheated = superheated_refrigerant_data["Enthalpy"]

# Defining functions through interpolation (2d)

enthalpy_superheated_func = interpolate.interp2d(
    temp_superheated, pressure_superheated, enthalpy_superheated
)
entropy_superheated_func = interpolate.bisplrep(
    temp_superheated, pressure_superheated, entropy_superheated, s=25
)

# Defining functions through bi-spline

dt_s_superheated_func = interpolate.bisplrep(
    entropy_superheated, pressure_superheated, temp_superheated, s=25
)
dt_h_superheated_func = interpolate.bisplrep(
    enthalpy_superheated, pressure_superheated, temp_superheated, s=25
)

bounds = [min(temp_gas_saturated), max(temp_gas_saturated)]
