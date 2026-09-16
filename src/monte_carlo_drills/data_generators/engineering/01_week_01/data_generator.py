"""Data generator for week 01 engineering exercises."""


from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(20260914)
years = np.arange(1996, 2026)
flows = rng.lognormal(mean=np.log(420), sigma=0.38, size=len(years))

df = pd.DataFrame(
    {
        "Water Year": years,
        "Peak Flow": np.round(flows, 1),
        "Units": "cfs",
        "Status": "Final",
    }
)

# Inject realistic defects. Peak Flow holds a stray string, so it must be
# object dtype -- pandas refuses to upcast float64 on assignment.
df["Peak Flow"] = df["Peak Flow"].astype(object)
df.loc[5, "Peak Flow"] = np.nan
df.loc[12, "Peak Flow"] = " 515.6 "
df.loc[18, "Units"] = "CFS"
df.loc[23, "Peak Flow"] = -45.0
df.loc[28, "Status"] = "Provisional"
df = pd.concat([df, df.iloc[[9]]], ignore_index=True)
df = df.sample(frac=1, random_state=41).reset_index(drop=True)

Path("data/raw/engineering/week_01").mkdir(parents=True, exist_ok=True)
df.to_csv("data/raw/engineering/week_01/annual_peak_flows_dirty.csv", index=False)
