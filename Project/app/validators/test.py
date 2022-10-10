from json_checker import Checker

request = {
    "userName": "zaidan123",
    "userPassword": "rahasia"
}

def test(request):
    try:
        schema = {
        "userName": str,
        "userPassword": str,
        "userEmail": str
    }
        checker = Checker(schema)
        checker.validate(request)
        return False
    except Exception as err:
        return err
        #print(err)
test(request)