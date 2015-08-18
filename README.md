==========================
Panopta API Python Package
==========================

The Panopta REST API provides full access to all configuration, status and outage management
functionality of the Panopta monitoring service, including the ability to create and modify
monitoring checks that are being performed, manage notification configuration, respond
to active outages and to pull availability statistics for monitored servers.

Installation
============

To install, just do a pip install of the package::

  pip install panopta_rest_api

The library depends on the httplib2 module, which will also be installed if it's not already
available.

API Documentation
=================
Full documentation for the API is available at https://api2.panopta.com/v2/api-docs/.  By 
entering your API token you can view full details on all of the API methods and issue API
requests from the documentation page.

Usage 
=====

The library provides a wrapper around the Panopta REST API, making it easy to issue 
GET, POST, PUT and DELETE operations to the API.  A sample use of the library is below.

::

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


