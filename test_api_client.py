import api_client
import json

api_url = 'http://api2.panopta.com'
api_token = 'testing'
version = '2'

if __name__ == '__main__':
    #-- initialize the client
    client = api_client.api_client(api_url, 
                                   api_token,
                                   version=version,
                                   log_level=api_client.LOG_DEBUG,
                                   log_path='./')

    #-- get a server
    query_params = { 'fqdn': 'panopta.com', 'limit': 10, 'offset': 0 }
    results = client.get('/server', query_params=query_params)
    print json.dumps(results, indent=2) 

    #-- create a contact
    data = { 'name': 'john', 'timezone': '%s/v%s/timezone/America/Chicago' % (api_url, version) } 
    results = client.post('/contact', request_data=data)
    print json.dumps(results, indent=2)
