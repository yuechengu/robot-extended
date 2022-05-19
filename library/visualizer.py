import sys
import pandas as pd
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, GeoType
from pyecharts import options as opts

class DomesticGeo:
    # 读取excel数据
    def get_data(file_name):
        df = pd.read_excel(sys.path[0] + fr'\data\{file_name}')
        return df

    # 国内疫情地图
    def domestic_geo(data) -> Geo:
        # 地名
        name_data = list(data['地区'])
        # 新增本土
        local_add_data_str = list(data['新增本土'])
        local_add_data = []
        # 新增无症状
        no_symptom_add_data_str = list(data['新增无症状'])
        no_symptom_add_data = []
        # 风险地区
        risk_area_data_str = list(data['风险区域'])
        risk_area_data = []

        # str[]转int[] + clear
        name_data_1 = []
        name_data_2 = []
        name_data_3 = []
        for i in range(0, len(local_add_data_str)):
            if int(local_add_data_str[i]) != 0:
                local_add_data.append(int(local_add_data_str[i]))
                name_data_1.append(name_data[i])
            if no_symptom_add_data_str[i] != '-' and no_symptom_add_data_str[i] != '0':
                no_symptom_add_data.append(int(no_symptom_add_data_str[i]))
                name_data_2.append(name_data[i])
            if int(risk_area_data_str[i]) != 0:
                risk_area_data.append(int(risk_area_data_str[i]))
                name_data_3.append(name_data[i])

        # 使用zip压缩为元组形式
        local_add_map = [tuple(z) for z in zip(name_data_1, local_add_data)]
        no_symptom_add_map = [tuple(z) for z in zip(name_data_2, no_symptom_add_data)]
        risk_area_map = [tuple(z) for z in zip(name_data_3, risk_area_data)]

        sum_local_add = 0
        sum_no_symptom_add = 0
        for i in range(len(local_add_map)):
            sum_local_add += local_add_map[i][1]
            # sum_no_symptom_add += no_symptom_add_data[i]

        geo = (
            Geo(
                init_opts=opts.InitOpts(width="1280px", height="800px")
            )
                .add_schema(
                maptype="china",
            )
                .add(
                "新增本土",
                local_add_map,
                # type_=GeoType.HEATMAP,
                is_selected=True,
            )
                .add(
                "新增无症状",
                no_symptom_add_map,
                # type_=GeoType.HEATMAP,
                is_selected=False,
            )
                .add(
                "风险区域",
                risk_area_map,
                # type_=GeoType.HEATMAP,
                is_selected=False,
            )
                .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=False,
                    color='#fff',
                    font_size=18,
                    position='left'
                )
            )
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                    is_show=False,
                    type_="size",
                    range_size=[5, 80],
                    range_opacity=0.7,
                    min_=0,
                    max_=int(sum_local_add) / 5,
                    pos_bottom="100",
                    pos_left="150",
                    is_piecewise=False
                ),
                title_opts=opts.TitleOpts(
                    title="国内疫情坐标",
                    pos_left="50",
                    pos_top="5%",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                    subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18, color='#222')
                ),
                legend_opts=opts.LegendOpts(
                    selected_mode='single',
                    pos_top="50",
                    pos_bottom="5%",
                    textstyle_opts=opts.TextStyleOpts(font_size=18)
                )
            )
        )

        return geo