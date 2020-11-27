import matplotlib.pyplot as plt
from collections import Counter
import requests
import json

class Plotter(object):
    """
    A Plotter object to help create graphics and visual representations of a given dataset
    """

    @staticmethod
    def pie_chart(data, attr, filepath):
        """
        Plots a pie chart based on a given data and a given atribbute of this data
        """
        my_data = list()
        for i in data:
            my_data.append(data[i][attr])

        my_data = Counter(my_data)

        labels = list()
        values = list()
        for i in my_data:
            r = requests.get('https://viacep.com.br/ws/' + i +'/json/')
            labels.append(r.json()['bairro'])
            values.append(my_data[i])

        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, startangle=90, autopct='%1.1f%%')
        ax1.axis('equal')

        plt.savefig(filepath)

    @staticmethod
    def bar_graph(data, attr, filepath):
        """
        Plots a bar graph based on date and a given attribute
        """
        my_data = list()
        for i in data:
            my_data.append(f'{data[i][attr]}\n{data[i]["date"]}')

        my_data = Counter(my_data)

        while(len(my_data) > 5):
            my_data.pop()

        labels = list()
        values = list()
        for i in my_data:
            labels.append(i)
            values.append(my_data[i])

        fig = plt.figure()

        plt.bar(labels, values, color='maroon',
                width=0.4)
        
        plt.savefig(filepath)


if __name__ == "__main__":

    r = requests.get('https://viacep.com.br/ws/' + '18055855' +'/json/')
    r.json()['bairro']