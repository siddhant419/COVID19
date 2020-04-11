import COVID19Py
import matplotlib.pyplot as mpl
covid19=COVID19Py.COVID19()
data=covid19.getAll(timelines=True)
virusdetails=dict(data["latest"])
names=list(virusdetails.keys())
values=list(virusdetails.values())
mpl.bar(range(len(virusdetails)),values, tick_label=names)
mpl.show()
print(virusdetails)
