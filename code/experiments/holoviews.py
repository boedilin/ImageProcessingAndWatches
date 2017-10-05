import holoviews as hv
hv.extension('bokeh')
import numpy as np
import pandas as pd

def f(param1, param2, opt_param=0):
    result = param1 + param2
    result += np.random.randn() * opt_param
    return {'param1': param1, 'param2': param2,
            'result': result, 'opt_param': opt_param}

param1 = np.logspace(0, 1)
param2 = np.logspace(0, 1)
opt_param = np.linspace(0, 1, num=5)

data = [f(p1, p2, opt_param=op)
        for p1 in param1 for p2 in param2 for op in opt_param]
df = pd.DataFrame(data)

# ignore extra columns to holoviews doesn't show extra sliders
to_keep = ['param1', 'param2', 'result', 'opt_param']
table = hv.Table(df[to_keep])

%%opts HeatMap (cmap='viridis') [tools=['hover'] xticks=10 yticks=5 colorbar=True toolbar='above' logx=True show_title=False]
%%output filename="holoviews" fig="html"
table.to.heatmap(kdims=['param1', 'param2'], vdims='result')