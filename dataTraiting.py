import pandas as pd
import matplotlib.pyplot as plt
import datetime

def FindBonneAffaire(data):
    now = datetime.datetime.now()

    data = data.filter(items=['title', 'price', 'temps'])
    data['price'] = data['price'].map(lambda x: x.replace('€', ''))\
                                    .map(lambda x: x.replace(' ', ''))\
                                        .map(lambda x: int(x))

    data=data[data.price<900 ]
    data=data[data.temps.str.contains("Aujourd'hui,")]
    data=data[data.temps.str.contains(str(now.hour)+":")]
    return data

