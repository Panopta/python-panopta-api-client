Panopta API Python Package
==========================
The Panopta API provides full access to all configuration, status and outage
management functionality of the Panopta monitoring service, including the
ability to create and modify monitoring checks that are being performed, manage
notification configuration, respond to active outages and to pull availability
statistics for monitored servers. This package makes it simple to interact with
the Panopta API.

# API Documentation
Full documentation for the API is available at
[https://api2.panopta.com/v2/api-docs/](https://api2.panopta.com/v2/api-docs/).
By entering your API token you can view full details on all of the API methods
and issue API requests from the documentation page.

# Installation
```bash
pip install panopta_api
```

# Usage 
The library provides a wrapper around the Panopta API, making it easy to issue 
GET, POST, PUT and DELETE operations to the API. The `Client` is an adapter
built on top of [Requests](http://python-requests.org), so anything you can do
with a `requests.Session`, you can with `panopta_api.Client`.

## Instantiate the Panopta API client
```python
from panopta_api import Client
client = Client('your-api-key',
                host='http://api2.panopta.com',
                version='2', 
                log_level=Client.LOG_INFO,
                log_path='logs/')
```

## Generate API urls
```python
resource = 'server'
id = '123'
collection = 'network_service'
server_network_services = client.url(resource, id, collection)
```

## GET
```python
five_contacts = client.get(client.url('contact'), params={'limit': 5});

servers_with_a_certain_fully_qualified_domain_name = client.get(
    client.url('server'),
    params={'fqdn': 'panopta.com'}
)

server_forty_two = client.get(client.url('server', '42'))
```

## POST
```python
new_notification_schedule = client.post(
    client.url('notification_schedule'),
    json={'name': 'New Notification Schedule',
          'targets': [server_forty_two['url']]}
)
```

## PUT
```python
updated_server_group = client.put(
    client.url('server_group'),
    json={'name': 'Updated Server Group',
          'notification_schedule': new_notification_schedule['url']}
)
```

## DELETE
```php
client.delete(client.url('contact', '1'))
```
