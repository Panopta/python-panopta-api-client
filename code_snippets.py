from panopta_rest_api import api_client

api_url = 'http://api2.panopta.com'
api_token = 'testing'
version = '2'

#-- initialize the client
client = api_client.api_client(api_url, 
                               api_token,
                               version=version,
                               log_level=api_client.LOG_DEBUG,
                               log_path='./')

#-- set a partner key
partner_customer_key = 'mycustomer'

#-- create a customer with partner key set to 'mycustomer'
data = {
    'name': 'John Smith',
    'email_address': 'john.smith@panopta.com',
    'package': 'panopta.bootstrap',
    'partner_customer_key': partner_customer_key
} 
results = client.post('/customer', request_data=data)
assert results['status_reason'] == 'success'

#-- create a notification schedule for 'mycustomer'
data = {
    'name': 'Basic'
} 
results = client.post('/notification_schedule?partner_customer_key=%s' % partner_customer_key, request_data=data)
assert results['status_reason'] == 'success'
notification_schedule_url = results['response_headers']['location'].rstrip("/")
notification_schedule_id = notification_schedule_url[notification_schedule_url.rindex("/") + 1:]

#-- create a server group for 'mycustomer'
data = {
    'name': 'Panopta Servers', 
    'notification_schedule': '%s/v%s/notification_schedule/%s' % (api_url, version, notification_schedule_id)
} 
results = client.post('/server_group?partner_customer_key=%s' % partner_customer_key, request_data=data)
assert results['status_reason'] == 'success'
server_group_url = results['response_headers']['location'].rstrip("/")
server_group_id = server_group_url[server_group_url.rindex("/") + 1:]

#-- create a server for 'mycustomer'
data = {
    'fqdn': 'panopta.com', 
    'name': 'Panopta', 
    'notification_schedule': '%s/v%s/notification_schedule/%s' % (api_url, version, notification_schedule_id), 
    'server_group': '%s/v%s/server_group/%s' % (api_url, version, server_group_id),
    'primary_monitoring_node': '%s/v%s/monitoring_node/202' % (api_url, version)
} 
results = client.post('/server?partner_customer_key=%s' % partner_customer_key, request_data=data)
assert results['status_reason'] == 'success'
server_url = results['response_headers']['location'].rstrip("/")
server_id = server_url[server_url.rindex("/") + 1:]

#-- create a HTTP network service for the new server
data = {
  'frequency': 60, 
  'service_type': '%s/v%s/network_service_type/31' % (api_url, version)
}
results = client.post('/server/%s/network_service?partner_customer_key=%s' % (server_id, partner_customer_key), request_data=data)
assert results['status_reason'] == 'success'

#-- create a Ping network service for the new server
data = {
  'frequency': 60, 
  'service_type': '%s/v%s/network_service_type/11' % (api_url, version)
}
results = client.post('/server/%s/network_service?partner_customer_key=%s' % (server_id, partner_customer_key), request_data=data)
assert results['status_reason'] == 'success'

#-- create a CPU SNMP resource for the new server
data = {
    'base_oid': '1.2.3.4',
    'frequency': 60,
    'name': 'CPU',
    'notification_threshold_duration': 60,
    'notification_threshold_type': 'gt',
    'notification_threshold_value': 0.01,
    'type': 'gauge'
}
results = client.post('/server/%s/snmp_resource?partner_customer_key=%s' % (server_id, partner_customer_key), request_data=data)
assert results['status_reason'] == 'success'

#-- create a Memory SNMP resource for the new server
data = {
    'base_oid': '8.1.3.4',
    'frequency': 60,
    'name': 'Memory',
    'notification_threshold_duration': 60,
    'notification_threshold_type': 'gt',
    'notification_threshold_value': 0.01,
    'type': 'gauge'
}
results = client.post('/server/%s/snmp_resource?partner_customer_key=%s' % (server_id, partner_customer_key), request_data=data)
assert results['status_reason'] == 'success'

#-- create a Disk Usage SNMP resource for the new server
data = {
    'base_oid': '6.1.4.3',
    'frequency': 60,
    'name': 'Disk Usage',
    'notification_threshold_duration': 60,
    'notification_threshold_type': 'gt',
    'notification_threshold_value': 0.01,
    'type': 'counter'
}
results = client.post('/server/%s/snmp_resource?partner_customer_key=%s' % (server_id, partner_customer_key), request_data=data)
assert results['status_reason'] == 'success'
