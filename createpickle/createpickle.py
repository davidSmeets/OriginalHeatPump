import pandas as pd
import pickle

# saturated (sat) refrigerant data
df_sat_r23 = pd.read_csv("r23_saturated.csv", header=None)
df_sat_r32 = pd.read_csv("r32_saturated.csv", header=None)
df_sat_r134a = pd.read_csv("r134a_saturated.csv", header=None)
df_sat_r236fa = pd.read_csv("r236fa_saturated.csv", header=None)
df_sat_r245fa = pd.read_csv("r245fa_saturated.csv", header=None)
df_sat_r290 = pd.read_csv("r290_saturated.csv", header=None)
df_sat_r404a = pd.read_csv("r404a_saturated.csv", header=None)
df_sat_r407a = pd.read_csv("r407a_saturated.csv", header=None)
df_sat_r410a = pd.read_csv("r410a_saturated.csv", header=None)
df_sat_r438a = pd.read_csv("r438a_saturated.csv", header=None)
df_sat_r449a = pd.read_csv("r449a_saturated.csv", header=None)
df_sat_r452a = pd.read_csv("r452a_saturated.csv", header=None)
df_sat_r455a = pd.read_csv("r455a_saturated.csv", header=None)
df_sat_r507a = pd.read_csv("r507a_saturated.csv", header=None)
df_sat_r508b = pd.read_csv("r508b_saturated.csv", header=None)
df_sat_r513a = pd.read_csv("r513a_saturated.csv", header=None)
df_sat_r600a = pd.read_csv("r600a_saturated.csv", header=None)
df_sat_r717 = pd.read_csv("r717_saturated.csv", header=None)
df_sat_r744 = pd.read_csv("r744_saturated.csv", header=None)
df_sat_r1233zd = pd.read_csv("r1233zd_saturated.csv", header=None)
df_sat_r1234yf = pd.read_csv("r1234yf_saturated.csv", header=None)

sat_refrigerantDict = {
    "r23": df_sat_r23,
    "r32": df_sat_r32,
    "r134a": df_sat_r134a,
    "r236fa": df_sat_r236fa,
    "r245fa": df_sat_r245fa,
    "r290": df_sat_r290,
    "r404a": df_sat_r404a,
    "r407a": df_sat_r407a,
    "r410a": df_sat_r410a,
    "r438a": df_sat_r438a,
    "r449a": df_sat_r449a,
    "r452a": df_sat_r452a,
    "r455a": df_sat_r455a,
    "r507a": df_sat_r507a,
    "r508b": df_sat_r508b,
    "r513a": df_sat_r513a,
    "r600a": df_sat_r600a,
    "r717": df_sat_r717,
    "r744": df_sat_r744,
    "r1233zd": df_sat_r1233zd,
    "r1234yf": df_sat_r1234yf,
}

# superheated (sup) refrigerant data

df_sup_r23 = pd.read_csv("r23_superheated.csv", header=None)
df_sup_r32 = pd.read_csv("r32_superheated.csv", header=None)
df_sup_r134a = pd.read_csv("r134a_superheated.csv", header=None)
df_sup_r236fa = pd.read_csv("r236fa_superheated.csv", header=None)
df_sup_r245fa = pd.read_csv("r245fa_superheated.csv", header=None)
df_sup_r290 = pd.read_csv("r290_superheated.csv", header=None)
df_sup_r404a = pd.read_csv("r404a_superheated.csv", header=None)
df_sup_r407a = pd.read_csv("r407a_superheated.csv", header=None)
df_sup_r410a = pd.read_csv("r410a_superheated.csv", header=None)
df_sup_r438a = pd.read_csv("r438a_superheated.csv", header=None)
df_sup_r449a = pd.read_csv("r449a_superheated.csv", header=None)
df_sup_r452a = pd.read_csv("r452a_superheated.csv", header=None)
df_sup_r455a = pd.read_csv("r455a_superheated.csv", header=None)
df_sup_r507a = pd.read_csv("r507a_superheated.csv", header=None)
df_sup_r508b = pd.read_csv("r508b_superheated.csv", header=None)
df_sup_r513a = pd.read_csv("r513a_superheated.csv", header=None)
df_sup_r600a = pd.read_csv("r600a_superheated.csv", header=None)
df_sup_r717 = pd.read_csv("r717_superheated.csv", header=None)
df_sup_r744 = pd.read_csv("r744_superheated.csv", header=None)
df_sup_r1233zd = pd.read_csv("r1233zd_superheated.csv", header=None)
df_sup_r1234yf = pd.read_csv("r1234yf_superheated.csv", header=None)

sup_refrigerantDict = {
    "r23": df_sup_r23,
    "r32": df_sup_r32,
    "r134a": df_sup_r134a,
    "r236fa": df_sup_r236fa,
    "r245fa": df_sup_r245fa,
    "r290": df_sup_r290,
    "r404a": df_sup_r404a,
    "r407a": df_sup_r407a,
    "r410a": df_sup_r410a,
    "r438a": df_sup_r438a,
    "r449a": df_sup_r449a,
    "r452a": df_sup_r452a,
    "r455a": df_sup_r455a,
    "r507a": df_sup_r507a,
    "r508b": df_sup_r508b,
    "r513a": df_sup_r513a,
    "r600a": df_sup_r600a,
    "r717": df_sup_r717,
    "r744": df_sup_r744,
    "r1233zd": df_sup_r1233zd,
    "r1234yf": df_sup_r1234yf,
}

# pickle

pickle.dump(sat_refrigerantDict, open("saturated_RefrigerantData", "wb"))
pickle.dump(sup_refrigerantDict, open("superheated_RefrigerantData", "wb"))
