import refData
import inputs
import numpy
from isentropicEfficiency import getEfficiency

#get evaporator temperature

if inputs.sourceType == 'Air':
    evaporatorTemp = inputs.sourceTemp - 6
elif inputs.sourceType == 'Water':
    evaporatorTemp = inputs.sourceTemp - 6
elif inputs.sourceType == 'Advanced':
    evaporatorTemp = inputs.sourceTemp - inputs.deltaT_sourceEvaporator

#get condensor temperature

if inputs.sinkType == 'Air':
    condensorTemp = inputs.sinkTemp + 12
elif inputs.sinkType == 'Water':
    deltaT_sinkCondensor = 5
    supplyTemp = inputs.sinkTemp
    returnTemp = inputs.sinkTemp_return
    condensorTemp = (-(returnTemp-supplyTemp*numpy.exp((supplyTemp-returnTemp)/deltaT_sinkCondensor))/(numpy.exp((supplyTemp-returnTemp)/deltaT_sinkCondensor)-1)) + deltaT_sinkCondensor
elif inputs.sinkType == 'Advanced':
    condensorTemp = inputs.sinkTemp + inputs.deltaT_sinkCondensor





