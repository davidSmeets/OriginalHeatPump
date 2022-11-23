import refdata as ref
import inputs
import numpy
from scipy import interpolate
from isentropic_efficiency import getefficiency
import pandas as pd
import matplotlib.pyplot as plt

# Get evaporator temperature

if inputs.source_type == 'Air':
    evaporator_temp = inputs.source_temp - 6
elif inputs.source_type == 'Water':
    evaporator_temp = inputs.source_temp - 6
elif inputs.source_type == 'Advanced':
    evaporator_temp = inputs.source_temp - inputs.delta_T_source_evaporator

# Get condensor temperature

if inputs.sink_type == 'Air':
    condensor_temp = inputs.sink_temp + 12

elif inputs.sink_type == 'Water':
    delta_T_sink_condensor = 5
    supply_temp = inputs.sink_temp
    return_temp = inputs.sink_temp_return

    condensor_temp = (-(return_temp-supply_temp*numpy.exp((supply_temp
                      - return_temp)/delta_T_sink_condensor)) / (numpy.exp(
                      (supply_temp-return_temp) / delta_T_sink_condensor)-1)) \
                       + delta_T_sink_condensor

elif inputs.sinkType == 'Advanced':
    condensor_temp = inputs.sink_temp + inputs.delta_T_sink_condensor

# Compressor intake (suction line)
p1 = ref.pressure_saturated_liq_func(evaporator_temp)
t1 = evaporator_temp + inputs.delta_T_superheat_suction
h1 = ref.enthalpy_superheated_func(inputs.delta_T_superheat_suction, p1)[0]
s1 = ref.entropy_superheated_func(inputs.delta_T_superheat_suction, p1)[0]

if inputs.delta_T_superheat_suction == 0:
    x1 = 1
else:
    x1 = '-'

# Compressor output (isentropic)
p2s = ref.pressure_saturated_gas_func(condensor_temp)
s2s = s1
dt2s = interpolate.bisplev(s2s, p2s, ref.dt_s_superheated_func)
t2s = condensor_temp + dt2s
x2s = '-'
h2s = ref.enthalpy_superheated_func(dt2s, p2s)[0]

# Compressor output ('real')
isentropic_efficiency = getefficiency(p2s/p1)

p2 = p2s
h2 = h1 + (h2s-h1) / isentropic_efficiency
dt2 = interpolate.bisplev(h2, p2, ref.dt_h_superheated_func)
t2 = condensor_temp + dt2
s2 = ref.entropy_superheated_func(dt2, p2)[0]
x2 = '-'

# Expansion valve intake
p3 = p2
t3 = condensor_temp
h3 = ref.enthalpy_liquid_saturated_func(p3)
s3 = ref.entropy_liquid_saturated_func(p3)
x3 = 0

# Expansion valve outlet
p4 = p1
t4 = evaporator_temp
h4 = h3

hf = ref.enthalpy_liquid_saturated_func(p4)
hg = ref.enthalpy_gas_saturated_func(p1)
x4 = (h4-hf) / (hg-hf)

sf = ref.entropy_liquid_saturated_func(p4)
sg = ref.entropy_gas_saturated_func(p1)
s4 = sf + x4 * (sg-sf)

# Cop calculation
delta_h_compressor = (h2-h1) / (inputs.motor_efficiency/100)
delta_h_condensor = h2-h3
cop = delta_h_condensor/delta_h_compressor

# Creating table
table = pd.DataFrame([['1',t1, p1, h1, s1, x1], 
                    ['2s', t2s, p2s, h2s, s2s, x2s], 
                    ['2', t2, p2, h2, s2, x2], 
                    ['3', t3, p3, h3, s3, x3], 
                    ['4', t4, p4, h4, s4, x4]])
table.columns = ['point', 'T (deg. C)', 'p (bar)', 'h (kJ/kg)', 's (kJ/kgK)', 'x']

# print(cop)
print(table)


#plot log p-h saturation curve

toplot_h_liq = ref.enthalpy_liquid_saturated_func(ref.pressure_saturated)
toplot_h_gas = ref.enthalpy_gas_saturated_func(ref.pressure_saturated)
toplot_p = ref.pressure_saturated

plt.plot(toplot_h_liq, toplot_p, color='k')
plt.plot(toplot_h_gas, toplot_p, color='k')
plt.yscale('log')
plt.xlabel("Enthalpy (kJ/kg)")
plt.ylabel("Pressure (bar)")
# plt.title("Log p-h diagram for refrigerant " + inputs.refrigerant)
plt.plot(table['h (kJ/kg)'] , table['p (bar)'], '*b')
plt.plot([h1,h2,h3,h4,h1] , [p1,p2,p3,p4,p1], 'b')
plt.plot(h2s,p2s, '*r')
plt.grid()
plt.show()