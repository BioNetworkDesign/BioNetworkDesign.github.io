from example.commons import Faker 
from pyecharts import options as opts 
from pyecharts.charts import Geo 
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Map

# c = (
#     Geo()
#     .add_schema(maptype="world")
#     # .add("geo", [list(z) for z in zip(['河南'], [22])])
#     .add_coordinate('TEST', -1.023194, 7.946527)
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(),
#         title_opts=opts.TitleOpts(title="Geo-基本示例"),
#     )
# )
# c.render()# 输出html格式
 
geo = Geo()
geo.add_schema(maptype="world") 
geo.add_coordinate('TEST', -1.023194, 7.946527) # 输入一个名为TEST的地址
geo.add("geo", [list(z) for z in zip(['TEST'], [22])]) # 把TEST放在列表里，加到地图里
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(),title_opts=opts.TitleOpts(title="Geo-基本示例"))

geo.render()# 显示地图
