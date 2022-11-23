import refdata as ref
import inputs
import numpy
from scipy import interpolate
from isentropic_efficiency import getefficiency
import pandas as pd
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
p1 = ref.pressure_saturated_liq_func(evaporator_temp)
t1 = evaporator_temp + inputs.delta_T_superheat_suction
h1 = ref.enthalpy_superheated_func(inputs.delta_T_superheat_suction, p1)
s1 = ref.entropy_superheated_func(inputs.delta_T_superheat_suction, p1)
if inputs.delta_T_superheat_suction == 0:
    x1 = 1
else:
    x1 = '-'
p2s = ref.pressure_saturated_gas_func(condensor_temp)
s2s = s1
dt2s = interpolate.bisplev(s2s, p2s, ref.dt_s_superheated_func)
t2s = condensor_temp + dt2s
x2s = '-'
h2s = ref.enthalpy_superheated_func(dt2s, p2s)
isentropic_efficiency = getefficiency(p2s/p1)

p2 = p2s
h2 = h1 + (h2s-h1) / isentropic_efficiency
dt2 = interpolate.bisplev(h2, p2, ref.dt_h_superheated_func)
t2 = condensor_temp + dt2
s2 = ref.entropy_superheated_func(dt2, p2)
x2 = '-'

p3 = p2
t3 = condensor_temp
h3 = ref.enthalpy_liquid_saturated_func(p3)
s3 = ref.entropy_liquid_saturated_func(p3)
x3 = 0

p4 = p1
t4 = evaporator_temp
h4 = h3

hf = ref.enthalpy_liquid_saturated_func(p4)
hg = ref.enthalpy_gas_saturated_func(p1)
x4 = (h4-hf) / (hg-hf)

sf = ref.entropy_liquid_saturated_func(p4)
sg = ref.entropy_gas_saturated_func(p1)
s4 = sf + x4 * (sg-sf)

delta_h_compressor = (h2-h1) / (inputs.motor_efficiency/100)
delta_h_condensor = h2-h3
COP = delta_h_condensor/delta_h_compressor

table = pd.DataFrame([['1',t1, p1, h1, s1, x1], 
                    ['2s', t2s, p2s, h2s, s2s, x2s], 
                    ['2', t2, p2, h2, s2, x2], 
                    ['3', t3, p3, h3, s3, x3], 
                    ['4', t4, p4, h4, s4, x4]])
table.columns = ['point', 'T (deg. C)', 'p (bar)', 'h (kJ/kg)', 's (kJ/kgK)', 'x']
print(COP)
print(table)