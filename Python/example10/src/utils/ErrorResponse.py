def Error(message="Error",code=0, subcode=0, subvalue=''):
    types = {
        "400": "Bad Request",
        "404": "Not Found",
        "409": "Conflict",
        "500": "Internal Server Error",
    }
    if not str(code) in types:
        raise Exception('Error(992.624896674387)::Undefined "code"')
    _type = ''
    if str(code) in types:
        _type = types[str(code)]
    r = {
        "error":{
            "type" : _type,
            "message":message,
            "code":code,
        }
    }
    subtypes = {
        "4090" : "Duplicate"
    }
    if subcode != 0 and str(subcode) in subtypes:
        subtype = ''
        subtype = subtypes[str(subcode)]
        r['error']['subcode'] = subcode
        r['error']['subtype'] = subtype
        r['error']['subvalue'] = subvalue
    return r,code

'''
# References:
- https://www.baeldung.com/rest-api-error-handling-best-practices
- https://sendgrid.api-docs.io/v3.0/how-to-use-the-sendgrid-v3-api/api-responses
'''