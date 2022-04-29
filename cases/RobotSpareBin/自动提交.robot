*** Settings ***

Library  自动提交.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Library  自动提交.AutoSubmitSalesData   WITH NAME  AutoSubmitSalesData



*** Test Cases ***

自动提交销售数据

  AutoSubmitSalesData.teststeps
