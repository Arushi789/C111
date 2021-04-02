import csv
import statistics
import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import random


df= pd.read_csv("data.csv")
data= df['Math_score'].tolist()

#plot the graph
fig= ff.create_distplot([data],['Math Scores'],show_hist=False)
fig.show()

mean= statistics.mean(data)
std_dev= statistics.stdev(data)
print('Mean of math scores= ',mean)
print('Standard Deviation of math scores= ',std_dev)

#mean of the samples
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean_of_sample1 = statistics.mean(dataset)
    return mean_of_sample1

#def show_fig(mean_list):
 #   df = mean_list
  #  fig = ff.create_distplot([df], ["average"], show_hist=False)
   # fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))
setup()
z_scores= (mean_of_sample1-mean)%std_dev
print(z_scores)