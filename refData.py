import pickle
from scipy import interpolate
import inputs

dict_saturatedRefrigerant = pickle.load(open('saturated_RefrigerantData', 'rb'))
dict_superheatedRefrigerant = pickle.load(open('superheated_RefrigerantData', 'rb'))
saturatedRefrigerantData = dict_saturatedRefrigerant[inputs.refrigerant] 
supereheatedRefrigerantData = dict_superheatedRefrigerant[inputs.refrigerant]
saturatedRefrigerantData.columns = ['Pressure', 'Temp_liq', 'Enthalpy_liq', 'Entropy_liq', 'Temp_gas', 'Enthalpy_gas', 'Entropy_gas']
supereheatedRefrigerantData.columns = ['dT_superheat', 'Pressure', 'Entropy', 'Enthalpy']

## saturated region ##

#defining variables from columns

Data_saturatedPressure = saturatedRefrigerantData['Pressure']            #pressure (equal for gasseous and liquid saturated state )

Data_saturatedTemp_liq = saturatedRefrigerantData['Temp_liq']            #temperature of saturated liquid
Data_saturatedEnthalpy_liq = saturatedRefrigerantData['Enthalpy_liq']    #enthalpy of saturated liquid
Data_saturatedEntropy_liq = saturatedRefrigerantData['Entropy_liq']      #entropy of saturated liquid

Data_saturatedTemp_gas = saturatedRefrigerantData['Temp_gas']            #temperature of saturated gas (in most cases (azeotropic) equal to temp. of saturated liquid)
Data_saturatedEnthalpy_gas = saturatedRefrigerantData['Enthalpy_gas']    #enthalpy of saturated gas
Data_saturatedEntropy_gas = saturatedRefrigerantData['Entropy_gas']      #entropy of saturated gas

#defining formulas through interpolation (1d)

saturatedPressure = interpolate.interp1d(Data_saturatedTemp_liq, Data_saturatedPressure)    #saturated pressure = f(saturated temperature liquid)
saturatedPressure = interpolate.interp1d(Data_saturatedTemp_gas, Data_saturatedPressure)

saturatedTemp_liq = interpolate.interp1d(Data_saturatedPressure, Data_saturatedTemp_liq)
saturatedEnthalpy_liq = interpolate.interp1d(Data_saturatedPressure, Data_saturatedEnthalpy_liq)
saturatedEntropy_liq = interpolate.interp1d(Data_saturatedPressure, Data_saturatedEntropy_liq)

saturatedTemp_gas = interpolate.interp1d(Data_saturatedPressure, Data_saturatedTemp_gas)                
saturatedEnthalpy_gas = interpolate.interp1d(Data_saturatedPressure, Data_saturatedEnthalpy_gas)
saturatedEntropy_gas = interpolate.interp1d(Data_saturatedPressure, Data_saturatedEntropy_gas)

## superheated region ## 

#defining variables from columns

Data_superheatTemp = supereheatedRefrigerantData['dT_superheat']       #defined as degrees of superheating above satured gas temperature
Data_superheatPressure = supereheatedRefrigerantData['Pressure']
Data_superheatEntropy = supereheatedRefrigerantData['Entropy']
Data_superheatEnthalpy = supereheatedRefrigerantData['Enthalpy']

#defining formulas through interpolation (2d)

superheatEnthalpy = interpolate.interp2d(Data_superheatTemp, Data_superheatPressure, Data_superheatEnthalpy)    #this one works
superheatEntropy = interpolate.interp2d(Data_superheatTemp, Data_superheatPressure, Data_superheatEntropy)

superheatTemp_s = interpolate.bisplrep(Data_superheatEntropy, Data_superheatPressure, Data_superheatTemp, s = 25)
superheatTemp_h = interpolate.bisplrep(Data_superheatEnthalpy, Data_superheatPressure, Data_superheatTemp, s = 25)