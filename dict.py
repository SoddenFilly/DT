data = {
    "Bitcoin-BTC":{
        "2021-06-30":{
            "price":3892389,
            "volume":2983984,
        },
        "2021-07-29":{
            "price":38922222,
            "volume":3333333,
        }
    },

    "Ethereum-ETH":{
        "2021-06-29":{
            "price":3899,
            "volume":2984,
        },
        "2021-07-31":{
            "price":4444,
            "volume":5555,
        }
    }
}
temp = {"date":{"price":99999,"volume":88888}}
data["Ethereum-ETH"].update(temp)
# data["Ethereum-ETH"].update({"p":{"pp":99}})

def unpack(data):
    print()
    print(data)
    for item in data:
        print()
        print("Slug/Symbol:",item)
        print("Symbol:",item.split("-")[0])
        print("Slug:",item.split("-")[1])
        print()
        for ite in data[item]:
            print("Date:",ite)
            for it,i in data[item][ite].items():
                print("Name:",it)
                print("Value:",i)

unpack(data)