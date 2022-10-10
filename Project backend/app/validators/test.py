from json_checker import Checker

def TesCre(request):
    try:
        schema = {
            "nama": str,
            "deskripsi": str
        }
        checker = Checker(schema)
        checker.validate(request)
        return False 
    except Exception as err:
        return err

def TesUp(data):
    try:
        checker = Checker({
            "nama": str,
            "deskripsi": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err