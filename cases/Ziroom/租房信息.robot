*** Settings ***

Library  租房信息.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Library  租房信息.AutoCollectRoomsData   WITH NAME  AutoCollectRoomsData



*** Test Cases ***

自动获得租房信息

  AutoCollectRoomsData.teststeps
