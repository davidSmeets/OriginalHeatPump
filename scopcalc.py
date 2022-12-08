import pandas as pd
import inputs
import numpy as np


def getscop(cop):
    data_bins = pd.read_csv("bin.csv", header=None)
    data_bins.columns = ["j", "Tj", "Warm", "Average", "Cold", "Tsource", "outs"]

    if inputs.detailed_source_type == "Air/other":
        data_bins.Tsource = data_bins.Tj + 0
    elif inputs.detailed_source_type == "Ground (closed, vertical)":
        data_bins.Tsource = data_bins.Tj + 0.5
    elif inputs.detailed_source_type == "Ground (closed, horizontal)":
        data_bins.Tsource = data_bins.Tj + 0.5
    elif inputs.detailed_source_type == "Groundwater":
        for j in data_bins.j:
            if data_bins.Tj[j] > 0:
                data_bins.Tsource = data_bins.Tj + 0.5
                data_bins.Tsource[0:31] = 0
    elif inputs.detailed_source_type == "Surface water":
        for j in data_bins.j:
            if data_bins.Tj[j] > 0:
                data_bins.Tsource = data_bins.Tj + 0.5
                data_bins.Tsource[0:31] = 0

    Tbins = data_bins.Tsource
    plr = (Tbins - 16) / ((inputs.source_temp) - 16)
    data_bins.outs = plr
    Ptj = inputs.capacity * plr

    if inputs.climate_profile == "Average":
        Hj = data_bins.Average.loc[20:]
        Ptj = Ptj.loc[20:]
        plr = plr.loc[20:]
        if inputs.source_temp > -10:
            print(
                "\033[93m Warning: design source temp. higher than lowest seasonal source temp. (assumed supplementary heater)"
            )
    if inputs.climate_profile == "Warmer":
        Hj = data_bins.Warmer.loc[32:]
        Ptj = Ptj.loc[32:]
        plr = plr.loc[32:]
        if inputs.source_temp > -2:
            print(
                "\033[93m Warning: design source temp. higher than lowest seasonal source temp. (assumed supplementary heater)"
            )
    if inputs.climate_profile == "Warmer":
        Hj = data_bins.Colder.loc[8:]
        Ptj = Ptj.loc[8:]
        plr = plr.loc[8:]
        if inputs.source_temp > -22:
            print(
                "\033[93m Warning: design source temp. higher than lowest seasonal source temp. (assumed supplementary heater)"
            )

    if (
        inputs.source_type == "Air"
        and inputs.sink_type == "Air"
        and inputs.capacity <= 12
    ):
        if inputs.climate_profile == "Average":
            HHe = 1400
            Hoff = 3672
            Hto = 179
            Hsb = 0
            Hck = 3851
        if inputs.climate_profile == "Warmer":
            HHe = 1400
            Hoff = 4345
            Hto = 755
            Hsb = 0
            Hck = 4476
        if inputs.climate_profile == "Colder":
            HHe = 2100
            Hoff = 2189
            Hto = 131
            Hsb = 0
            Hck = 2944
    elif (
        (inputs.source_type == "Air" or inputs.source_type == "Water")
        and inputs.sink_type == "Water"
        and inputs.capacity < 400
    ):
        if inputs.climate_profile == "Average":
            HHe = 2066
            Hoff = 3672
            Hto = 178
            Hsb = 0
            Hck = 3850
        if inputs.climate_profile == "Warmer":
            HHe = 1336
            Hoff = 4416
            Hto = 754
            Hsb = 0
            Hck = 5170
        if inputs.climate_profile == "Colder":
            HHe = 2465
            Hoff = 2208
            Hto = 106
            Hsb = 0
            Hck = 2314
    elif (
        inputs.source_type == "Air"
        and inputs.sink_type == "Air"
        and inputs.capacity > 12
    ) or (inputs.source_type == "Water" and inputs.sink_type == "Air"):
        if inputs.climate_profile == "Average":
            HHe = 1400
            Hoff = 3672
            Hto = 179
            Hsb = 0
            Hck = 3851
        if inputs.climate_profile == "Warmer":
            HHe = 1400
            Hoff = 2189
            Hto = 131
            Hsb = 0
            Hck = 5100
        if inputs.climate_profile == "Colder":
            HHe = 2100
            Hoff = 4345
            Hto = 755
            Hsb = 0
            Hck = 2320
    else:
        if inputs.climate_profile == "Average":
            HHe = 1400
            Hoff = 3672
            Hto = 179
            Hsb = 0
            Hck = 3851
        if inputs.climate_profile == "Warmer":
            HHe = 1400
            Hoff = 4345
            Hto = 755
            Hsb = 0
            Hck = 4476
        if inputs.climate_profile == "Colder":
            HHe = 2100
            Hoff = 2189
            Hto = 131
            Hsb = 0
            Hck = 2944
        print("\033[93m Waring: SCOP calculation unhealthy")

    Pto = 0.003 * inputs.capacity
    Psb = 0.003 * inputs.capacity
    Pck = 0.003 * inputs.capacity
    Poff = 0.005 * inputs.capacity

    COPlr100 = cop
    COPmax = cop + 0.3
    COPmin = cop - 0.5

    LRmin = 0.2
    LRopt = 0.6
    cd = 0.2

    COPbin = np.zeros(len(plr))

    m = 0

    for k in plr:
        if k > 1:
            COPbin[m] = 1
        elif k == 1.0:
            COPbin[m] = COPlr100
        elif k < 1 and k >= LRopt:
            COPbin[m] = COPmax + (COPlr100 - COPmax) * ((k - LRopt) / 1 - LRopt)
        elif k < LRopt and k > LRmin:
            COPbin[m] = COPmin + (COPmax - COPmin) * ((k - LRmin) / (LRopt - LRmin))
        elif k <= LRmin:
            ir = k / LRmin
            COPbin[m] = COPmin * (ir / ((cd * ir) + (1 - cd)))

        if COPbin[m] <= 1:
            COPbin[m] = COPlr100
        m = m + 1

    myrange = np.arange(0, 1.05, 0.05)
    COPbin_toplot = np.zeros(len(myrange))

    indx = 0

    for w in myrange:
        if w > 1:
            COPbin_toplot[indx] = 1
        elif w == 1.0:
            COPbin_toplot[indx] = COPlr100
        elif w < 1 and w >= LRopt:
            COPbin_toplot[indx] = COPmax + (COPlr100 - COPmax) * (
                (w - LRopt) / 1 - LRopt
            )
        elif w < LRopt and w > LRmin:
            COPbin_toplot[indx] = COPmin + (COPmax - COPmin) * (
                (w - LRmin) / (LRopt - LRmin)
            )
        elif w <= LRmin:
            ir = w / LRmin
            COPbin_toplot[indx] = COPmin * (ir / ((cd * ir) + (1 - cd)))
        indx = indx + 1

    sigma1 = sum(Hj * Ptj)
    sigma2 = sum(Hj * (Ptj / COPbin))
    SCOPon = sigma1 / sigma2

    qh = inputs.capacity * HHe
    sum_aux = Hto * Pto + Hsb * Psb + Hck * Pck + Hoff * Poff
    QHe = qh / SCOPon + sum_aux
    scop = qh / QHe

    return (COPbin_toplot, myrange, scop)
