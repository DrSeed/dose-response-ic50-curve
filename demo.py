import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(1)
def hill(x,ic50,h):return 1/(1+(x/ic50)**h)
conc=np.logspace(-3,2,12);true=0.8
resp=hill(conc,true,1.2)+rng.normal(0,0.04,len(conc))
(ic50,h),_=curve_fit(hill,conc,resp,p0=[1,1],maxfev=10000)
xs=np.logspace(-3,2,200)
plt.figure(figsize=(6,5));plt.scatter(conc,resp,c="k",zorder=3,label="measured")
plt.plot(xs,hill(xs,ic50,h),c="firebrick",label=f"fit IC50={ic50:.2f}")
plt.axvline(ic50,ls="--",c="grey");plt.xscale("log")
plt.xlabel("drug concentration (log)");plt.ylabel("viability");plt.title("Dose-response (demo data)");plt.legend()
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"IC50={ic50:.3f}\n");print("ok")