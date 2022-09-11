var myMusic = [
    {
        "artist": "Billy Joel",
        "title": "Piano Man",
        "release_year": 1973,
        "formats": [
            "CD",
            "8T",
            "LP"
        ],
        "gold": true,
        "innerObg": {
            "iop1": "iOProp1",
            "iop2": [
                "a",
                "b",
                "c",
                {
                    "key1": "key01",
                    "key 2": "key02"
                }
            ]
        }
    },
    {
        "innerObg": {
            "iop1": "iOProp1",
            "iop2": [
                "a",
                "b",
                "c",
                {
                    "key1": "key11",
                    "key 2": "key12"
                }
            ]
        }
    }
];

console.log(myMusic[1].innerObg.iop2[3]["key 2"]);