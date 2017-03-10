# LugLoc API Client

Simple LugLoc API client for python.

## Installation

...

## Usage

Do create a LugLoc API client you need create a LugLoc object:

    my_client = LugLoc("user@lugloc.com", "password", "client_id", "client_secret")

The methods of the client return information about the user and devices, for example:

    my_client.getUserInfo()

## Methods

get_user_info
get_devices
get_device
get_location_history
refresh_location
turn_off

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sebys/LugLocPythonClient.