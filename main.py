from infoblox_client.connector import Connector
def infoblox_connection():
    host = '192.168.1.10'
    username = 'admin'
    password = 'admin'

    opts = {'host': host, 'username': username, 'password': password}
    conn = Connector(opts)
    return conn


def search_extensible_attribute(connection, place_to_check: str, extensible_attribute: str, value: str):
    """
    Find extensible attributes.
    :param connection: Infoblox connection
    :param place_to_check: Can be `network`, `networkcontainer` or `record:host` and so on.
    :param extensible_attribute: Which extensible attribute to search for. Can be `CustomerCode`, `Location`
    and so on.
    :param value: The value you want to search for.
    :return: result
    """
    extensible_args = [
        place_to_check,
        {
            f"*{extensible_attribute}:~": value,
        }
    ]
    kwargs = {
        'return_fields': [
            'default',
            'extattrs',
        ]
    }
    result = {"type": f"{place_to_check}", "objects": connection.get_object(*extensible_args, **kwargs)}
    return result


connection = infoblox_connection()

search_network = search_extensible_attribute(connection, "network", "CustomerCode", "Infoblox")
# Print the output:
print(search_network)
