# LugLoc API Client

Simple LugLoc API client for python.

## Installation

...

## Usage

For create a LugLoc client you need create a LugLoc object:

    myClient = LugLoc("user@lugloc.com", "password", "client_id", "client_secret")

The methods of the client return information about the user and devices, for example:

    myClient.getUserInfo()

## Methods

get_user_info
get_devices
get_device
get_location_history
refresh_location
turn_off

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sebys/LugLocPythonClient.