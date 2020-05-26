import csv
import pandas as pd 
import matplotlib.pyplot as plt

def set_title(title,xlab,ylab):
    
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

data = pd.read_csv(r'covid.csv')

focus = pd.DataFrame(data,columns=['data','totale_casi'])

print(focus)

calendario = []
tot_casis = []

def tot_casi_plot():
    for i in range(85):
        tot_casis.append(focus['totale_casi'][i])
        plt.plot(i,focus['totale_casi'][i],'ro')

    set_title('Casi totali di Covid-19 in italia', 'Giorni','Casi totali')
    plt.show()
tot_casi_plot()
def new_infetti():
    for i in range(85):
        if i !=0:
            plt.plot(i,focus['totale_casi'][i]-focus['totale_casi'][i-1],'bo')

    set_title('Nuovi infetti per giorno','Giorni','Nuovi casi')
    plt.show()


def tot_deriv_plot():
    for i in range(85):
        tot_casis.append(focus['totale_casi'][i])
        plt.plot(i,focus['totale_casi'][i],'ro')

        if i!=0:
            plt.plot(i,focus['totale_casi'][i]-focus['totale_casi'][i-1],'bo')

    plt.show()

tot_deriv_plot()