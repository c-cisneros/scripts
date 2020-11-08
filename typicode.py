import requests
import datetime


#Creates a class for all API interactions
class RequestsApi:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/posts/'
        self.session = requests.Session()

    def get(self, url, **kwargs):
        return self.session.get(self.base_url+url, **kwargs)

    def post(self, **kwargs):
        return self.session.post(self.base_url, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(self.base_url+url, **kwargs)


# Prints the value of the title for post number 99.
api = RequestsApi()
request = api.get('99')
request_json = request.json()
print(request_json['title'])

# Injects a field called time into the results for post number 100 and print
# the whole JSON record.
get_datetime = datetime.datetime.now()
time = get_datetime.strftime('%d/%m/%Y %H:%M:%S')
request = api.get('100')
request_json = request.json()
request_json['time'] = time
print(request_json)

# Creates new /posts entry then create a tuple of the "id" value, status
# code and "X-Powered-By" field in the headers.
api = RequestsApi()
request = api.post(json={'Title': 'Security Interview Post', 'UserId': '500',
                         'Body': 'This is an insertion test with a known API'})
request_json = request.json()
request_headers = request.headers
request_tuple = (request_json['id'], request.status_code, request_headers['x-Powered-By'])
print(request_tuple)

# Deletes the record previously created and return status code as well as
# x-content-type-options.
api = RequestsApi()
request = api.delete(f"r_json['id']")
print(request.status_code)
print(request.headers['x-content-type-options'])