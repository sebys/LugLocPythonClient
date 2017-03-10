# LugLoc API Client

Simple LugLoc API client for python.

## Installation

...

## Usage

To create a LugLoc API client you need create a LugLoc object:

    from luglocapiclient import LugLoc
    my_client = LugLoc("user@lugloc.com", "password", "client_id", "client_secret")

The methods of the API client return information about the user and your devices, for example:

    my_client.get_devices()

Return 

...

## Methods

* get_user_info
* get_devices
* get_device
* get_location_history
* refresh_location
* turn_off

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sebys/LugLocPythonClient.