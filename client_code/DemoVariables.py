# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def say_hello():
  print("Hello, world")

def update_dhcp():
  # get_available_ips()
  # u_get_statistics()
  return statistics_demo, ip_details_demo








































statistics_demo = [
    {
        'interface': 'VLAN0010',
        'dhcp_pools': ['192.168.8.150-192.168.8.240'],
        'free_dhcp_ips_count': 60,
        'free_ips_outside_dhcp_count': 156
    },
    {
        'interface': 'VLAN0050',
        'dhcp_pools': ['172.16.50.100-172.16.50.199'],
        'free_dhcp_ips_count': 100,
        'free_ips_outside_dhcp_count': 153
    },
    {
        'interface': 'VLAN0040',
        'dhcp_pools': ['172.16.40.2-172.16.40.254'],
        'free_dhcp_ips_count': 141,
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'VLAN0060',
        'dhcp_pools': ['172.16.60.100-172.16.60.105'],
        'free_dhcp_ips_count': 6,
        'free_ips_outside_dhcp_count': 245
    },
    {
        'interface': 'wan2',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 4
    },
    {
        'interface': 'GRE-ZSCALER01',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'GRE-ZSCALER02',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'GRE-ZSCALER03',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'GRE-ZSCALER04',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'VLAN0020',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'VLAN0070',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'dmz',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'fortilink',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'internal',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'nameif VLAN0030',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'wan1',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 13
    }
]

ip_details_demo = defaultdict(None,
            {'GRE-ZSCALER01': defaultdict(None,
                                          {'all_subnet_ips': IPSet(['172.18.48.81/32']),
                                           'available_from_dhcp_subnet': IPSet([]),
                                           'available_from_subnet': IPSet(['172.18.48.81/32']),
                                           'dhcp_pool_length': 0,
                                           'free_ips_in_dhcp_count': 0,
                                           'free_ips_outside_dhcp_count': 0,
                                           'interface_arps': IPSet([]),
                                           'interface_dhcp_sets': IPSet([]),
                                           'interface_leased': IPSet([])}),
             'GRE-ZSCALER02': defaultdict(None,
                                          {'all_subnet_ips': IPSet(['172.18.48.85/32']),
                                           'available_from_dhcp_subnet': IPSet([]),
                                           'available_from_subnet': IPSet(['172.18.48.85/32']),
                                           'dhcp_pool_length': 0,
                                           'free_ips_in_dhcp_count': 0,
                                           'free_ips_outside_dhcp_count': 0,
                                           'interface_arps': IPSet([]),
                                           'interface_dhcp_sets': IPSet([]),
                                           'interface_leased': IPSet([])}),
             'GRE-ZSCALER03': defaultdict(None,
                                          {'all_subnet_ips': IPSet(['172.21.26.145/32']),
                                           'available_from_dhcp_subnet': IPSet([]),
                                           'available_from_subnet': IPSet(['172.21.26.145/32']),
                                           'dhcp_pool_length': 0,
                                           'free_ips_in_dhcp_count': 0,
                                           'free_ips_outside_dhcp_count': 0,
                                           'interface_arps': IPSet([]),
                                           'interface_dhcp_sets': IPSet([]),
                                           'interface_leased': IPSet([])}),
             'GRE-ZSCALER04': defaultdict(None,
                                          {'all_subnet_ips': IPSet(['172.21.26.149/32']),
                                           'available_from_dhcp_subnet': IPSet([]),
                                           'available_from_subnet': IPSet(['172.21.26.149/32']),
                                           'dhcp_pool_length': 0,
                                           'free_ips_in_dhcp_count': 0,
                                           'free_ips_outside_dhcp_count': 0,
                                           'interface_arps': IPSet([]),
                                           'interface_dhcp_sets': IPSet([]),
                                           'interface_leased': IPSet([])}),
             'VLAN0010': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['192.168.8.1/32', '192.168.8.2/31', '192.168.8.4/30', '192.168.8.8/29', '192.168.8.16/28', '192.168.8.32/27', '192.168.8.64/26', '192.168.8.128/26', '192.168.8.192/27', '192.168.8.224/28', '192.168.8.240/29', '192.168.8.248/30', '192.168.8.252/31', '192.168.8.254/32']),
                                      'available_from_dhcp_subnet': IPSet(['192.168.8.156/32', '192.168.8.159/32', '192.168.8.165/32', '192.168.8.167/32', '192.168.8.174/31', '192.168.8.177/32', '192.168.8.180/32', '192.168.8.186/31', '192.168.8.188/30', '192.168.8.192/31', '192.168.8.194/32', '192.168.8.196/30', '192.168.8.200/30', '192.168.8.204/31', '192.168.8.206/32', '192.168.8.208/28', '192.168.8.224/30', '192.168.8.228/31', '192.168.8.230/32', '192.168.8.232/29', '192.168.8.240/32']),
                                      'available_from_subnet': IPSet(['192.168.8.1/32', '192.168.8.2/31', '192.168.8.4/30', '192.168.8.8/29', '192.168.8.16/28', '192.168.8.32/32', '192.168.8.35/32', '192.168.8.36/30', '192.168.8.40/29', '192.168.8.48/28', '192.168.8.64/26', '192.168.8.128/28', '192.168.8.144/30', '192.168.8.148/31', '192.168.8.241/32', '192.168.8.242/31', '192.168.8.244/30', '192.168.8.248/32', '192.168.8.253/32', '192.168.8.254/32']),
                                      'dhcp_pool_length': 91,
                                      'free_ips_in_dhcp_count': 60,
                                      'free_ips_outside_dhcp_count': 156,
                                      'interface_arps': IPSet(['192.168.8.33/32', '192.168.8.34/32', '192.168.8.152/32', '192.168.8.154/32', '192.168.8.157/32', '192.168.8.158/32', '192.168.8.161/32', '192.168.8.162/32', '192.168.8.164/32', '192.168.8.166/32', '192.168.8.168/30', '192.168.8.172/32', '192.168.8.176/32', '192.168.8.179/32', '192.168.8.181/32', '192.168.8.184/31', '192.168.8.207/32', '192.168.8.249/32', '192.168.8.250/31', '192.168.8.252/32']),
                                      'interface_dhcp_sets': IPSet(['192.168.8.150/31', '192.168.8.152/29', '192.168.8.160/27', '192.168.8.192/27', '192.168.8.224/28', '192.168.8.240/32']),
                                      'interface_leased': IPSet(['192.168.8.150/31', '192.168.8.152/30', '192.168.8.157/32', '192.168.8.158/32', '192.168.8.160/30', '192.168.8.164/32', '192.168.8.166/32', '192.168.8.168/30', '192.168.8.172/31', '192.168.8.176/32', '192.168.8.178/31', '192.168.8.181/32', '192.168.8.182/31', '192.168.8.184/31', '192.168.8.195/32', '192.168.8.231/32']),
                                      'pools': [{'range': '192.168.8.150-192.168.8.240'}]}),
             'VLAN0020': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['172.16.20.1/32', '172.16.20.2/31', '172.16.20.4/30', '172.16.20.8/29', '172.16.20.16/28', '172.16.20.32/27', '172.16.20.64/26', '172.16.20.128/26', '172.16.20.192/27', '172.16.20.224/28', '172.16.20.240/29', '172.16.20.248/30', '172.16.20.252/31', '172.16.20.254/32']),
                                      'available_from_dhcp_subnet': IPSet([]),
                                      'available_from_subnet': IPSet(['172.16.20.1/32', '172.16.20.2/31', '172.16.20.4/30', '172.16.20.8/29', '172.16.20.16/28', '172.16.20.32/27', '172.16.20.64/26', '172.16.20.128/26', '172.16.20.192/27', '172.16.20.224/28', '172.16.20.240/29', '172.16.20.248/30', '172.16.20.252/31', '172.16.20.254/32']),
                                      'dhcp_pool_length': 0,
                                      'free_ips_in_dhcp_count': 0,
                                      'free_ips_outside_dhcp_count': 253,
                                      'interface_arps': IPSet([]),
                                      'interface_dhcp_sets': IPSet([]),
                                      'interface_leased': IPSet([])}),
             'VLAN0040': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['172.16.40.1/32', '172.16.40.2/31', '172.16.40.4/30', '172.16.40.8/29', '172.16.40.16/28', '172.16.40.32/27', '172.16.40.64/26', '172.16.40.128/26', '172.16.40.192/27', '172.16.40.224/28', '172.16.40.240/29', '172.16.40.248/30', '172.16.40.252/31', '172.16.40.254/32']),
                                      'available_from_dhcp_subnet': IPSet(['172.16.40.102/32', '172.16.40.115/32', '172.16.40.116/30', '172.16.40.120/29', '172.16.40.128/26', '172.16.40.192/27', '172.16.40.224/28', '172.16.40.240/29', '172.16.40.248/30', '172.16.40.252/31', '172.16.40.254/32']),
                                      'available_from_subnet': IPSet(['172.16.40.1/32']),
                                      'dhcp_pool_length': 253,
                                      'free_ips_in_dhcp_count': 141,
                                      'free_ips_outside_dhcp_count': 0,
                                      'interface_arps': IPSet(['172.16.40.2/32', '172.16.40.4/32', '172.16.40.7/32', '172.16.40.8/31', '172.16.40.11/32', '172.16.40.12/32', '172.16.40.16/32', '172.16.40.21/32', '172.16.40.25/32', '172.16.40.26/32', '172.16.40.29/32', '172.16.40.30/31', '172.16.40.35/32', '172.16.40.36/32', '172.16.40.41/32', '172.16.40.43/32', '172.16.40.44/32', '172.16.40.48/32', '172.16.40.50/31', '172.16.40.52/31', '172.16.40.54/32', '172.16.40.56/31', '172.16.40.64/32', '172.16.40.69/32', '172.16.40.70/31', '172.16.40.73/32', '172.16.40.81/32', '172.16.40.84/31', '172.16.40.88/31', '172.16.40.95/32', '172.16.40.100/32', '172.16.40.104/30', '172.16.40.114/32']),
                                      'interface_dhcp_sets': IPSet(['172.16.40.2/31', '172.16.40.4/30', '172.16.40.8/29', '172.16.40.16/28', '172.16.40.32/27', '172.16.40.64/26', '172.16.40.128/26', '172.16.40.192/27', '172.16.40.224/28', '172.16.40.240/29', '172.16.40.248/30', '172.16.40.252/31', '172.16.40.254/32']),
                                      'interface_leased': IPSet(['172.16.40.2/31', '172.16.40.4/30', '172.16.40.8/29', '172.16.40.16/28', '172.16.40.32/27', '172.16.40.64/27', '172.16.40.96/30', '172.16.40.100/31', '172.16.40.103/32', '172.16.40.104/29', '172.16.40.112/31', '172.16.40.114/32']),
                                      'pools': [{'range': '172.16.40.2-172.16.40.254'}]}),
             'VLAN0050': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['172.16.50.1/32', '172.16.50.2/31', '172.16.50.4/30', '172.16.50.8/29', '172.16.50.16/28', '172.16.50.32/27', '172.16.50.64/26', '172.16.50.128/26', '172.16.50.192/27', '172.16.50.224/28', '172.16.50.240/29', '172.16.50.248/30', '172.16.50.252/31', '172.16.50.254/32']),
                                      'available_from_dhcp_subnet': IPSet(['172.16.50.100/30', '172.16.50.104/29', '172.16.50.112/28', '172.16.50.128/26', '172.16.50.192/29']),
                                      'available_from_subnet': IPSet(['172.16.50.1/32', '172.16.50.2/31', '172.16.50.4/30', '172.16.50.8/29', '172.16.50.16/28', '172.16.50.32/27', '172.16.50.64/27', '172.16.50.96/30', '172.16.50.200/29', '172.16.50.208/28', '172.16.50.224/28', '172.16.50.240/29', '172.16.50.248/30', '172.16.50.252/31', '172.16.50.254/32']),
                                      'dhcp_pool_length': 100,
                                      'free_ips_in_dhcp_count': 100,
                                      'free_ips_outside_dhcp_count': 153,
                                      'interface_arps': IPSet([]),
                                      'interface_dhcp_sets': IPSet(['172.16.50.100/30', '172.16.50.104/29', '172.16.50.112/28', '172.16.50.128/26', '172.16.50.192/29']),
                                      'interface_leased': IPSet([]),
                                      'pools': [{'range': '172.16.50.100-172.16.50.199'}]}),
             'VLAN0060': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['172.16.60.1/32', '172.16.60.2/31', '172.16.60.4/30', '172.16.60.8/29', '172.16.60.16/28', '172.16.60.32/27', '172.16.60.64/26', '172.16.60.128/26', '172.16.60.192/27', '172.16.60.224/28', '172.16.60.240/29', '172.16.60.248/30', '172.16.60.252/31', '172.16.60.254/32']),
                                      'available_from_dhcp_subnet': IPSet(['172.16.60.100/30', '172.16.60.104/31']),
                                      'available_from_subnet': IPSet(['172.16.60.1/32', '172.16.60.2/31', '172.16.60.4/30', '172.16.60.8/29', '172.16.60.16/28', '172.16.60.32/27', '172.16.60.64/27', '172.16.60.96/30', '172.16.60.106/31', '172.16.60.108/30', '172.16.60.112/28', '172.16.60.128/29', '172.16.60.136/30', '172.16.60.140/32', '172.16.60.142/31', '172.16.60.144/30', '172.16.60.148/31', '172.16.60.150/32', '172.16.60.152/29', '172.16.60.160/27', '172.16.60.192/27', '172.16.60.224/28', '172.16.60.240/29', '172.16.60.248/30', '172.16.60.252/31', '172.16.60.254/32']),
                                      'dhcp_pool_length': 6,
                                      'free_ips_in_dhcp_count': 6,
                                      'free_ips_outside_dhcp_count': 245,
                                      'interface_arps': IPSet(['172.16.60.141/32', '172.16.60.151/32']),
                                      'interface_dhcp_sets': IPSet(['172.16.60.100/30', '172.16.60.104/31']),
                                      'interface_leased': IPSet([]),
                                      'pools': [{'range': '172.16.60.100-172.16.60.105'}]}),
             'VLAN0070': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['172.16.70.1/32', '172.16.70.2/31', '172.16.70.4/30', '172.16.70.8/29', '172.16.70.16/28', '172.16.70.32/27', '172.16.70.64/26', '172.16.70.128/26', '172.16.70.192/27', '172.16.70.224/28', '172.16.70.240/29', '172.16.70.248/30', '172.16.70.252/31', '172.16.70.254/32']),
                                      'available_from_dhcp_subnet': IPSet([]),
                                      'available_from_subnet': IPSet(['172.16.70.1/32', '172.16.70.2/31', '172.16.70.4/30', '172.16.70.8/29', '172.16.70.16/28', '172.16.70.32/27', '172.16.70.64/26', '172.16.70.128/26', '172.16.70.192/27', '172.16.70.224/28', '172.16.70.240/29', '172.16.70.248/30', '172.16.70.252/31', '172.16.70.254/32']),
                                      'dhcp_pool_length': 0,
                                      'free_ips_in_dhcp_count': 0,
                                      'free_ips_outside_dhcp_count': 253,
                                      'interface_arps': IPSet([]),
                                      'interface_dhcp_sets': IPSet([]),
                                      'interface_leased': IPSet([])}),
             'dmz': defaultdict(None,
                                {'all_subnet_ips': IPSet(['10.10.10.1/32', '10.10.10.2/31', '10.10.10.4/30', '10.10.10.8/29', '10.10.10.16/28', '10.10.10.32/27', '10.10.10.64/26', '10.10.10.128/26', '10.10.10.192/27', '10.10.10.224/28', '10.10.10.240/29', '10.10.10.248/30', '10.10.10.252/31', '10.10.10.254/32']),
                                 'available_from_dhcp_subnet': IPSet([]),
                                 'available_from_subnet': IPSet(['10.10.10.1/32', '10.10.10.2/31', '10.10.10.4/30', '10.10.10.8/29', '10.10.10.16/28', '10.10.10.32/27', '10.10.10.64/26', '10.10.10.128/26', '10.10.10.192/27', '10.10.10.224/28', '10.10.10.240/29', '10.10.10.248/30', '10.10.10.252/31', '10.10.10.254/32']),
                                 'dhcp_pool_length': 0,
                                 'free_ips_in_dhcp_count': 0,
                                 'free_ips_outside_dhcp_count': 253,
                                 'interface_arps': IPSet([]),
                                 'interface_dhcp_sets': IPSet([]),
                                 'interface_leased': IPSet([])}),
             'fortilink': defaultdict(None,
                                      {'all_subnet_ips': IPSet(['169.254.1.1/32', '169.254.1.2/31', '169.254.1.4/30', '169.254.1.8/29', '169.254.1.16/28', '169.254.1.32/27', '169.254.1.64/26', '169.254.1.128/26', '169.254.1.192/27', '169.254.1.224/28', '169.254.1.240/29', '169.254.1.248/30', '169.254.1.252/31', '169.254.1.254/32']),
                                       'available_from_dhcp_subnet': IPSet([]),
                                       'available_from_subnet': IPSet(['169.254.1.1/32', '169.254.1.2/31', '169.254.1.4/30', '169.254.1.8/29', '169.254.1.16/28', '169.254.1.32/27', '169.254.1.64/26', '169.254.1.128/26', '169.254.1.192/27', '169.254.1.224/28', '169.254.1.240/29', '169.254.1.248/30', '169.254.1.252/31', '169.254.1.254/32']),
                                       'dhcp_pool_length': 0,
                                       'free_ips_in_dhcp_count': 0,
                                       'free_ips_outside_dhcp_count': 253,
                                       'interface_arps': IPSet([]),
                                       'interface_dhcp_sets': IPSet([]),
                                       'interface_leased': IPSet([])}),
             'internal': defaultdict(None,
                                     {'all_subnet_ips': IPSet(['192.168.1.1/32', '192.168.1.2/31', '192.168.1.4/30', '192.168.1.8/29', '192.168.1.16/28', '192.168.1.32/27', '192.168.1.64/26', '192.168.1.128/26', '192.168.1.192/27', '192.168.1.224/28', '192.168.1.240/29', '192.168.1.248/30', '192.168.1.252/31', '192.168.1.254/32']),
                                      'available_from_dhcp_subnet': IPSet([]),
                                      'available_from_subnet': IPSet(['192.168.1.1/32', '192.168.1.2/31', '192.168.1.4/30', '192.168.1.8/29', '192.168.1.16/28', '192.168.1.32/27', '192.168.1.64/26', '192.168.1.128/26', '192.168.1.192/27', '192.168.1.224/28', '192.168.1.240/29', '192.168.1.248/30', '192.168.1.252/31', '192.168.1.254/32']),
                                      'dhcp_pool_length': 0,
                                      'free_ips_in_dhcp_count': 0,
                                      'free_ips_outside_dhcp_count': 253,
                                      'interface_arps': IPSet([]),
                                      'interface_dhcp_sets': IPSet([]),
                                      'interface_leased': IPSet([])}),
             'nameif VLAN0030': defaultdict(None,
                                            {'all_subnet_ips': IPSet(['172.16.30.1/32', '172.16.30.2/31', '172.16.30.4/30', '172.16.30.8/29', '172.16.30.16/28', '172.16.30.32/27', '172.16.30.64/26', '172.16.30.128/26', '172.16.30.192/27', '172.16.30.224/28', '172.16.30.240/29', '172.16.30.248/30', '172.16.30.252/31', '172.16.30.254/32']),
                                             'available_from_dhcp_subnet': IPSet([]),
                                             'available_from_subnet': IPSet(['172.16.30.1/32', '172.16.30.2/31', '172.16.30.4/30', '172.16.30.8/29', '172.16.30.16/28', '172.16.30.32/27', '172.16.30.64/26', '172.16.30.128/26', '172.16.30.192/27', '172.16.30.224/28', '172.16.30.240/29', '172.16.30.248/30', '172.16.30.252/31', '172.16.30.254/32']),
                                             'dhcp_pool_length': 0,
                                             'free_ips_in_dhcp_count': 0,
                                             'free_ips_outside_dhcp_count': 253,
                                             'interface_arps': IPSet([]),
                                             'interface_dhcp_sets': IPSet([]),
                                             'interface_leased': IPSet([])}),
             'wan1': defaultdict(None,
                                 {'all_subnet_ips': IPSet(['212.118.7.49/32', '212.118.7.50/31', '212.118.7.52/30', '212.118.7.56/30', '212.118.7.60/31', '212.118.7.62/32']),
                                  'available_from_dhcp_subnet': IPSet([]),
                                  'available_from_subnet': IPSet(['212.118.7.49/32', '212.118.7.50/31', '212.118.7.52/30', '212.118.7.56/30', '212.118.7.60/31', '212.118.7.62/32']),
                                  'dhcp_pool_length': 0,
                                  'free_ips_in_dhcp_count': 0,
                                  'free_ips_outside_dhcp_count': 13,
                                  'interface_arps': IPSet([]),
                                  'interface_dhcp_sets': IPSet([]),
                                  'interface_leased': IPSet([])}),
             'wan2': defaultdict(None,
                                 {'all_subnet_ips': IPSet(['92.253.92.41/32', '92.253.92.42/31', '92.253.92.44/31', '92.253.92.46/32']),
                                  'available_from_dhcp_subnet': IPSet([]),
                                  'available_from_subnet': IPSet(['92.253.92.42/31', '92.253.92.44/31', '92.253.92.46/32']),
                                  'dhcp_pool_length': 0,
                                  'free_ips_in_dhcp_count': 0,
                                  'free_ips_outside_dhcp_count': 4,
                                  'interface_arps': IPSet(['92.253.92.41/32']),
                                  'interface_dhcp_sets': IPSet([]),
                                  'interface_leased': IPSet([])})})


arp_demo = [
    {'ip': '192.168.8.176', 'age': 10, 'mac': '38:f3:ab:73:45:c9'},
    {'ip': '192.168.8.169', 'age': 3, 'mac': '28:ee:52:11:59:f0'},
    {'ip': '192.168.8.162', 'age': 15, 'mac': '7c:8a:e1:a0:5d:0c'},
    {'ip': '192.168.8.168', 'age': 2, 'mac': '7c:8a:e1:a0:5c:58'},
    {'ip': '192.168.8.181', 'age': 20, 'mac': 'b4:45:06:6b:d0:15'},
    {'ip': '192.168.8.207', 'age': 9, 'mac': '00:17:c8:26:9a:23'},
    {'ip': '192.168.8.161', 'age': 4, 'mac': '38:f3:ab:6c:bd:03'},
    {'ip': '192.168.8.154', 'age': 20, 'mac': '00:24:9b:75:22:ad'},
    {'ip': '192.168.8.252', 'age': 6, 'mac': '00:38:df:ca:d1:58'},
    {'ip': '192.168.8.166', 'age': 22, 'mac': '8c:ae:4c:f6:03:6e'},
    {'ip': '192.168.8.179', 'age': 2, 'mac': '00:e0:4c:68:39:cf'},
    {'ip': '192.168.8.251', 'age': 13, 'mac': 'c4:b9:cd:39:38:61'},
    {'ip': '192.168.8.172', 'age': 18, 'mac': '28:ee:52:11:5f:2d'},
    {'ip': '192.168.8.34', 'age': 22, 'mac': 'e0:cb:bc:8f:4d:66'},
    {'ip': '192.168.8.185', 'age': 14, 'mac': 'b4:45:06:6b:cf:9d'},
    {'ip': '192.168.8.152', 'age': 12, 'mac': 'b4:45:06:6b:d0:a9'},
    {'ip': '192.168.8.250', 'age': 0, 'mac': 'c4:b9:cd:39:3a:09'},
    {'ip': '192.168.8.158', 'age': 28, 'mac': 'ac:1a:3d:b2:b1:b5'},
    {'ip': '192.168.8.171', 'age': 15, 'mac': 'f8:75:a4:4d:30:c1'},
    {'ip': '192.168.8.184', 'age': 18, 'mac': 'f8:75:a4:ea:c7:16'},
    {'ip': '192.168.8.33', 'age': 3, 'mac': 'b0:fa:eb:3d:a4:2a'},
    {'ip': '192.168.8.164', 'age': 8, 'mac': 'f8:75:a4:ea:c8:0e'},
    {'ip': '192.168.8.249', 'age': 3, 'mac': '70:18:a7:44:81:f7'},
    {'ip': '192.168.8.157', 'age': 16, 'mac': 'b4:45:06:6b:d0:55'},
    {'ip': '192.168.8.170', 'age': 1, 'mac': 'f8:75:a4:ea:c1:47'}
]

demo_statistics = [
    {
        'interface': 'VLAN0010',
        'interface_network': '192.168.8.254/24',
        'dhcp_pools': ['192.168.8.150-192.168.8.240'],
        'free_dhcp_ips_count': 60,
        'free_ips_outside_dhcp_count': 156
    },
    {
        'interface': 'VLAN0050',
        'interface_network': '172.16.50.1/24',
        'dhcp_pools': ['172.16.50.100-172.16.50.199'],
        'free_dhcp_ips_count': 100,
        'free_ips_outside_dhcp_count': 153
    },
    {
        'interface': 'VLAN0040',
        'interface_network': '172.16.40.1/24',
        'dhcp_pools': ['172.16.40.2-172.16.40.254'],
        'free_dhcp_ips_count': 141,
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'VLAN0060',
        'interface_network': '172.16.60.1/24',
        'dhcp_pools': ['172.16.60.100-172.16.60.105'],
        'free_dhcp_ips_count': 6,
        'free_ips_outside_dhcp_count': 245
    },
    {
        'interface': 'wan2',
        'interface_network': '92.253.92.42/29',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 4
    },
    {
        'interface': 'GRE-ZSCALER01',
        'interface_network': '172.18.48.81/32',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'GRE-ZSCALER02',
        'interface_network': '172.18.48.85/32',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'GRE-ZSCALER03',
        'interface_network': '172.21.26.145/32',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'GRE-ZSCALER04',
        'interface_network': '172.21.26.149/32',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 'No Free IPs'
    },
    {
        'interface': 'VLAN0020',
        'interface_network': '172.16.20.1/24',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'VLAN0070',
        'interface_network': '172.16.70.1/24',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'dmz',
        'interface_network': '10.10.10.1/24',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'fortilink',
        'interface_network': '169.254.1.1/24',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'internal',
        'interface_network': '192.168.1.99/24',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'nameif VLAN0030',
        'interface_network': '172.16.30.1/24',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 253
    },
    {
        'interface': 'wan1',
        'interface_network': '212.118.7.50/28',
        'dhcp_pools': 'Not Configured',
        'free_dhcp_ips_count': '-',
        'free_ips_outside_dhcp_count': 13
    }
]
