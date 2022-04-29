*** Settings ***

Library  自动采集.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Library  自动采集.AutoCollectCovidNews   WITH NAME  AutoCollectCovidNews

Library  自动采集.AutoCollectCovidData   WITH NAME  AutoCollectCovidData



*** Test Cases ***

自动采集疫情速报

  AutoCollectCovidNews.teststeps


自动采集疫情数据

  AutoCollectCovidData.teststeps
