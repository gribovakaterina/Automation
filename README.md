./.venv/Scripts/activate
pytest .\tests\elements_test.py::TestElements::TestCheckBox -sv
pytest .\tests\elements_test.py::TestElements::TestCheckBox -sv  --alluredir reportallure
allure serve .\reportallure\
