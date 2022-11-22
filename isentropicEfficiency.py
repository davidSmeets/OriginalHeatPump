import inputs
import math

def get_efficiency(pressureratio):
    if inputs.isentropicEfficiency == 'Estimate':
        if inputs.compressorType == 'Screw':
            isentropicEfficiency_max = 0.75
        elif inputs.compressorType == 'Scroll':
            isentropicEfficiency_max = 0.73
        elif inputs.compressorType == 'Reciprocating':
            isentropicEfficiency_max = 0.72
        elif inputs.compressorType == 'Centrifugal':
            isentropicEfficiency_max = 0.77
        elif inputs.compressorType == 'Unknown':
            isentropicEfficiency_max = 0.70

        isentropicEfficiency = -0.01*math.sqrt(pressureratio 
                               - inputs.idealPressureRatio) \
                               + isentropicEfficiency_max

    elif inputs.isentropicEfficiency == 'Value':
        isentropicEfficiency = inputs.isentropicEfficiencyVal/100

    elif inputs.isentropicEfficiency == 'Do not include in calculation':
        isentropicEfficiency = 1

    return isentropicEfficiency