*** Settings ***

Library  绘制地图.py   WITH NAME  F

Library  绘制地图.DrawCovidGeo   WITH NAME  DrawCovidGeo



*** Test Cases ***

绘制国内疫情地图

  DrawCovidGeo.teststeps
