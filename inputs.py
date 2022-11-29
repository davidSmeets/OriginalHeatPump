import pandas as pd

## General tab

# Type of sink ('Water', 'Air', 'Advanced')
sink_type = "Water"

# Type of source ('Water', 'Air', 'Advanced')
source_type = "Air"

# Temperature of sink (Celcius) in case of sinkType water: also water return temperature, default 10K (EN-14511 specifies only supply temp)
sink_temp = 47
sink_temp_return = 37

# Temperature of source (Celsius)
source_temp = 5

# Refrigerant ('r1233zd'	'r1234yf'	'r134a'	'r23'	'r236fa'	'r245fa'	'r290'	'r32'	'r404a'	'r407a'	'r407c'	'r410a'	'r438a'	'r449a'	'r452a'	'r455a'	'r507a'	'r508b'	'r513a'	'r600a'	'r717'	'r744')
refrigerant = "r410a"

# Capacity (kiloWatt), only to be used for SCOP calculation
capacity = 10


## Advanced tab

# Delta T source/evaporator (Kelvin), only to be used if sourceType = 'Advanced'
delta_T_source_evaporator = 6

# Delta T sink/condensor (Kelvin), only to be used if sinkType = 'Advanced'
delta_T_sink_condensor = 5

# Delta T superheating in suction line (K), default value 5K
delta_T_superheat_suction = 5

# Type of compressor ('Unknown', 'Screw', 'Scroll', 'Reciprocating', 'Centrifugal')
compressor_type = "Scroll"

# Isentropic efficiency ('Estimate', 'Value', 'Do not include in calculation')
isentropic_efficiency = "Estimate"
isentropic_efficiency_val = 65  # (%) in case of 'Value'

# Ideal pressure ratio (-), default value 3
ideal_pressure_ratio = 3

# Motor efficiency
motor_efficiency = 85  # (%)


## SCOP tab

# Climate profile ('Average', 'Warmer', 'Colder')
climate_profile = "Average"

# Detailed source type ('Air/other', 'Ground (closed, vertical)', 'Ground (closed, horizontal)', 'Groundwater', 'Surface water - Lake', 'Surface water - River', 'Surface water - Sea')
detailed_source_type = "Air/other"

inputtable = pd.DataFrame(
    [
        ["Sink", sink_type],
        ["Source", source_type],
        ["Sink temperature (°C)", sink_temp],
        ["Sink temperature (return) (°C)", sink_temp_return],
        ["Source temperature (°C)", source_temp],
        ["Refrigerant", refrigerant],
        ["Capacity (kW)", capacity],
    ]
)
