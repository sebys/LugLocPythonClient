# LugLoc API Client

Simple LugLoc API client for python developers.

## Installation

To install the module, run the following command:

    pip install git+https://github.com/sebys/LugLocPythonClient

## Usage

To create a LugLoc API client you need create a LugLoc object:

    from luglocapiclient import LugLoc
    my_client = LugLoc("user@lugloc.com", "password", "client_id", "client_secret")

The methods of the API client return information about the user and your devices, for example:

    my_client.get_devices()

Return the following json:

    [
        {
            "ActivationDate":"2016-08-09T21:52:14.543Z",
            "AllwaysOn":false,
            "Battery":"100%",
            "BluetoothID":"Bluetooth_Id",
            "CustomerId":1,
            "DeviceId":1,
            "DeviceName":"My LugLoc I",
            "FreeUTraces":true,
            "FreeUTracesExpirationDate":"2016-09-09T13:22:55.987Z",
            "HasBluetooth":true,
            "HasRfOffMode":false,
            "HasTraces":true,
            "IconUrl":"",
            "LastAccuracy":2592.0,
            "LastBatteryUpdate":"2016-09-20T12:12:09.733Z",
            "LastLatitude":-31.261106099999996,
            "LastLocationGeneralDescription":"Santa Fe Province, Argentina",
            "LastLocationPhotoUrl":"https://lh4.googleusercontent.com/-YqafncPgAXQ/VqqnpnSRS9I/AAAAAAAABVA/ebQVEpR4TcgjM2mBiYb-a33RooI8JFuDQ/s1600-w600/",
            "LastLocationSpecificDescription":"Rafaela",
            "LastLongitude":-61.4994242,
            "LastPositionUpdate":"2016-09-20T12:11:11.597Z",
            "Status":"Rf_Off",
            "TracesExpirationDate":"2019-09-26T18:51:56.743Z"
        },
        {
            "ActivationDate":"2016-03-19T11:49:30.910Z",
            "AllwaysOn":true,
            "Battery":"100%",
            "BluetoothID":"Bluetooth_Id",
            "CustomerId":1,
            "DeviceId":2,
            "DeviceName":"My LugLoc II",
            "FreeUTraces":true,
            "FreeUTracesExpirationDate":"2016-04-05T22:03:27.430Z",
            "HasBluetooth":true,
            "HasRfOffMode":true,
            "HasTraces":true,
            "IconUrl":"",
            "LastAccuracy":2612.0,
            "LastBatteryUpdate":"2017-03-07T14:13:09.397Z",
            "LastLatitude":-31.256418099999998,
            "LastLocationGeneralDescription":"Santa Fe Province, Argentina",
            "LastLocationPhotoUrl":"https://lh3.googleusercontent.com/-W7_1ctpj-ig/V8irsCQXsAI/AAAAAAAAAKQ/KUro8xxLJvARMlBnElxJruabbykyT5dPwCJkC/s1600-w600/",
            "LastLocationSpecificDescription":"Rafaela",
            "LastLongitude":-61.4930775,
            "LastPositionUpdate":"2017-03-10T16:12:12.553Z",
            "Status":"Normal",
            "TracesExpirationDate":"2017-06-01T00:00:00.000Z"
        }
    ]

## Methods

* get_user_info
* get_devices
* get_device
* get_location_history
* refresh_location
* turn_off

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sebys/LugLocPythonClient.