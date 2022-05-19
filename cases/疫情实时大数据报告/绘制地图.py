import sys
from library.visualizer import DomesticGeo as dg

class DrawCovidGeo:
    # 用例名
    name = '绘制国内疫情地图'

    # 用例步骤，即本用例的正式脚本
    def teststeps(self):
        excel_data = dg.get_data('CovidNews.xlsx')
        dg.domestic_geo(excel_data).render(path=sys.path[0] + r'\reports\国内疫情坐标.html')
        # 浏览器预览
        import webbrowser
        path = sys.path[0] + r'\reports\国内疫情坐标.html'
        webbrowser.open_new_tab(path)