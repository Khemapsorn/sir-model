import matplotlib.pyplot as plt
import random as rn 
import numpy as np 
import statistics

n = 10_000
i0 = 5
s0 = n-i0
r = 0

a = 0.0002
b = 0.5

r0 = (a*s0)/b

def set_title():
    title = 'Comportamento delle 3 funzioni con r0:'+str(r0)
    plt.title(title)
    plt.xlabel('Giorni')
    plt.ylabel('Abitanti')

def abline(slope,x1,y1):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    for i in range(len(x_vals)):
        x_vals[i] += 2
    y_vals = slope*x_vals-slope*x1+y1
    plt.plot(x_vals, y_vals, '--')

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step

def nextSs(a,oldS,oldI,t):
    out = oldS - (a*oldS*oldI)*t
    return out 


def nextIs(a,b,oldS,oldI,t):
    out = oldI + (a*oldS*oldI)*t - (b*oldI)*t
    return out

def nextRs(b,r,oldI,t):
    out = r + (b*oldI)*t
    return out

def connect(old, new,i,c,step):
    plt.plot([i-step,i],[old,new],c)



def simple_plot():
    set_title()

    for i in range(25):
        if i == 0:
            S = s0
            I = i0
            R = r
            print('S0 is: ',S)
        else:
            print('-----------------')
            oldS = S
            print('old S: ',oldS)
            oldI = I
            print('old I: ',oldI)
            oldR = R
            print('old R: ',oldR)

            
            S = nextSs(a,oldS,oldI,1)
            I = nextIs(a,b,oldS,oldI,1)
            R = nextRs(b,oldR,oldI,1)
            print('S nuovo giorno: ', S)
            print('I nuovo giorno: ', I)

            connect(oldS,S,i,'r-',1)
            connect(oldI,I,i,'b-',1)
            connect(oldR,R,i,'g-',1)

        plt.plot(i,S,'ro')
        plt.plot(i,I,'Hb')
        plt.plot(i,R,'sg')

    plt.show()

#simple_plot()

step = 0.01
def disc_plot():
    set_title()
    step = 0.2

    for i in drange(0,25,step):
        if i == 0:
            S = s0
            I = i0
            R = r
            print('S0 is: ',S)
        else:
            print('-----------------')
            oldS = S
            print('old S: ',oldS)
            oldI = I
            print('old I: ',oldI)
            oldR = R
            print('old R: ',oldR)

            
            S = nextSs(a,oldS,oldI, step)
            I = nextIs(a,b,oldS,oldI, step)
            R = nextRs(b,oldR,oldI, step)
            print('S nuovo giorno: ', S)
            print('I nuovo giorno: ', I)

            connect(oldS,S,i,'r-',step)
            connect(oldI,I,i,'b-',step)
            connect(oldR,R,i,'g-',step)

        plt.plot(i,S,'ro')
        plt.plot(i,I,'Hb')
        plt.plot(i,R,'sg')

    plt.show()
#disc_plot()

def r0_variation():
    
    for i in range(10):
        print('Grafico n.',i+1)
        a = 0.0002
        print('initial a:', a)
        delta = rn.randrange(-19,19)
        delta = delta *10**-5
        print('random delta:', delta)
        a = a + delta
        print('final a:', a)
        print('---------------------------')

        r0 = (a*s0)/b
        disc_plot()


def plot_total_new():
    #plt.title('Variazione di S nel tempo')
    #plt.xlabel('Giorni')
    #plt.ylabel('Abitanti')

    step = 0.01

    for i in drange(0,15,step):
        
        if i == 0:
            S = s0
            I = i0
            R = r

            print('S0 is: ',S)


            tot_case = I+R
            #_r = r0
        else:
            print('-----------------')
            print('day: ',i)
            oldS = S
            print('old S: ',oldS)
            oldI = I
            print('old I: ',oldI)
            oldR = R
            print('old R: ',oldR)

            #oldTot = tot_case
            #old_r = _r

            S = nextSs(a,oldS,oldI, step)
            I = nextIs(a,b,oldS,oldI, step)
            R = nextRs(b,oldR,oldI, step)
            print('S nuovo giorno: ', S)
            print('I nuovo giorno: ', I)

            tot_case = I + R
            #_r = (a*S)/b

            #connect(oldTot,tot_case,i,'-r',step)
            #connect(oldI,I,i,'-b',step)
            #connect(oldS, S,i,'-g',step)
            #connect(old_r,_r,i,'-b',step)

            #plt.plot(i,tot_case, 'ro')
            #plt.plot(i,S, 'go')
            #plt.plot(i,I,'bo')
            #plt.plot(i,_r,'bo')

            
            if i == 6.009999999999916:
                #make pie
                labels = 'Infetti', 'Rimossi'
                colors = ['lightcoral', 'lightskyblue']
                sizes = [I,R]

                plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)



                plt.axis('equal')
                plt.show()
            
            
    plt.show()
plot_total_new()

def plot_total_and_der():
    step = 0.01
    casi_list = []
    derivate_list = []

    plt.title('Casi totali, Derivata e nuovi casi')
    plt.xlabel('Giorni')
    plt.ylabel('Abitanti')

    for i in drange(0,15,step):
        if i == 0:
            S = s0
            I = i0
            R = r
            print('S0 is: ',S)
            tot_case = I+R
            derivata = 0
        else:
            #print('-----------------')
            oldS = S
            #print('old S: ',oldS)
            oldI = I
            #print('old I: ',oldI)
            oldR = R
            #print('old R: ',oldR)

            oldTot = tot_case
            oldD = derivata

            S = nextSs(a,oldS,oldI, step)
            I = nextIs(a,b,oldS,oldI, step)
            R = nextRs(b,oldR,oldI, step)
            #print('S nuovo giorno: ', S)
            #print('I nuovo giorno: ', I)

            tot_case = I + R
            derivataI = (I-oldI)/step
            derivata = (tot_case-oldTot)/step

            #connect(oldTot,tot_case,i,'-r',step)
            connect(oldD,derivata,i,'-g',step)
            connect(oldI,I,i,'-b',step)

            #plt.plot(i,tot_case, 'ro')
            plt.plot(i,derivata,'go')
            plt.plot(i,I,'bo')

            '''
            #traccia rette con coef deriv
            if i==4.89999999999994:
                #print('here')
                abline(derivata,i,tot_case)
            if i==6.999999999999895:
                abline(derivata,i,tot_case)
            '''

            casi_list.append(tot_case)
            derivate_list.append(derivata)
            
    print('\n\n\n------ Risultati: --------')
    maxi = 0
    #trovare 'derivata massima'
    for i in range(len(derivate_list)):
        if i == 0:
            maxi = derivate_list[i]
        else:
            if derivate_list[i] >= maxi:
                maxi = derivate_list[i]
                corrispondente_i = i
    print('Coefficente in punto massimo della crescita:', maxi)
    print('X nel giorno di massima crescita:', corrispondente_i*10**-2)

    for i in range(len(casi_list)):
        if i!=0 and i!=1:
            grow = (casi_list[i]-casi_list[i-1])/(casi_list[i-1]-casi_list[i-2])
            #print(grow)
            if grow == 1.0000960554645488:
                print('X del punto di flesso : ',i*10**-2)

    '''
    moltiplicatori = []
    for i in range(200,300):
        moltiplicatore = casi_list[i+100]/casi_list[i]
        moltiplicatori.append(moltiplicatore)
    print(moltiplicatori)
    maximum = max(moltiplicatori)
    print(maximum)
    for i in drange(0,5,step):
        y=maximum**i
        plt.plot(i,y,'bo')
    '''

    plt.show()
plot_total_and_der()


#plt.show()