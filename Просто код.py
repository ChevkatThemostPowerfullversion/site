  {
        "id": "777e21d8fb7005c6",
        "type": "json",
        "z": "88da2bec208da9fc",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 190,
        "y": 140,
        "wires": [
            [
                "9f828d0c941740ff"
            ]
        ]
    },
    {
        "id": "9f828d0c941740ff",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "var value=JSON.parse(JSON.stringify(msg.payload));\nvalue=msg;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 320,
        "y": 220,
        "wires": [
            [
                "fe6fc76d0b7ed705",
                "3aea9c82799acd44",
                "edf7c2341a1b106b"
            ]
        ]
    },
    {
        "id": "fe6fc76d0b7ed705",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "msg.payload=msg.payload.Li;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 500,
        "y": 140,
        "wires": [
            [
                "1ada5da722d25cc3"
            ]
        ]
    },
    {
        "id": "edf7c2341a1b106b",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "msg.payload=msg.payload.Hum;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 500,
        "y": 300,
        "wires": [
            [
                "a8b9a012f0bcd88a"
            ]
        ]
    },
    {
        "id": "3aea9c82799acd44",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "msg.payload=msg.payload.Temp;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 500,
        "y": 220,
        "wires": [
            [
                "94261317f1debd03"
            ]
        ]
    },
    {
        "id": "94261317f1debd03",
        "type": "ui_chart",
        "z": "88da2bec208da9fc",
        "name": "",
        "group": "218fb04944bee58f",
        "order": 8,
        "width": 15,
        "height": 4,
        "label": "Temprature",
        "chartType": "line",
        "legend": "false",
        "xformat": "HH:mm:ss",
        "interpolate": "linear",
        "nodata": "",
        "dot": false,
        "ymin": "",
        "ymax": "",
        "removeOlder": 1,
        "removeOlderPoints": "",
        "removeOlderUnit": "3600",
        "cutout": 0,
        "useOneColor": false,
        "useUTC": false,
        "colors": [
            "#1f77b4",
            "#aec7e8",
            "#ff7f0e",
            "#2ca02c",
            "#98df8a",
            "#d62728",
            "#ff9896",
            "#9467bd",
            "#c5b0d5"
        ],
        "outputs": 1,
        "useDifferentColor": false,
        "className": "",
        "x": 690,
        "y": 220,
        "wires": [
            []
        ]
    },
    {
        "id": "a8b9a012f0bcd88a",
        "type": "ui_gauge",
        "z": "88da2bec208da9fc",
        "name": "",
        "group": "218fb04944bee58f",
        "order": 1,
        "width": 8,
        "height": 4,
        "gtype": "wave",
        "title": "Humidity",
        "label": "units",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 700,
        "y": 300,
        "wires": []
    },
    {
        "id": "1ada5da722d25cc3",
        "type": "ui_gauge",
        "z": "88da2bec208da9fc",
        "name": "",
        "group": "218fb04944bee58f",
        "order": 3,
        "width": 9,
        "height": 4,
        "gtype": "gage",
        "title": "Light intensity",
        "label": "units",
        "format": "{{value}}",
        "min": 0,
        "max": "1023",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 700,
        "y": 140,
        "wires": []
    },
    {
        "id": "46a301b8aa20f403",
        "type": "serial in",
        "z": "88da2bec208da9fc",
        "name": "",
        "serial": "632ce51bae434d89",
        "x": 90,
        "y": 240,
        "wires": [
            [
                "777e21d8fb7005c6"
            ]
        ]
    },
    {
        "id": "218fb04944bee58f",
        "type": "ui_group",
        "name": "Arduino Uno Station",
        "tab": "b10389acabce7f3b",
        "order": 1,
        "disp": true,
        "width": "20",
        "collapse": false,
        "className": ""
    },
    {
        "id": "632ce51bae434d89",
        "type": "serial-port",
        "serialport": "COM6",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "waitfor": "",
        "dtr": "none",
        "rts": "none",
        "cts": "none",
        "dsr": "none",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": "",
        "responsetimeout": "10000"
    },
    {
        "id": "b10389acabce7f3b",
        "type": "ui_tab",
        "name": "Node-Red Weather Station",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
