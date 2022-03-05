import plotly.figure_factory as pff
import plotly.express as pe
import plotly.graph_objects as go
import random
import statistics
import csv
import pandas as pd

df = pd.read_csv('medium_data.csv')
data_list = df["reading_time"].to_list()

population_mean = statistics.mean(data_list)
print("The poplulation mean is", population_mean)

population_sdev = statistics.stdev(data_list)
print("The standard deviation of the population is", population_sdev)

fir_stan_dev_star = population_mean-population_sdev
fir_stan_dev_en = population_mean+population_sdev

list_of_data_within_1_std_deviation = [
    result for result in data_list if result > fir_stan_dev_star and result < fir_stan_dev_en
]

sec_stan_dev_star = population_mean-(2*population_sdev)
sec_stan_dev_en = population_mean+(2*population_sdev)

list_of_data_within_2_std_deviation = [
    result for result in data_list if result > sec_stan_dev_star and result < sec_stan_dev_en
]

thi_stan_dev_star = population_mean-(3*population_sdev)
thi_stan_dev_en = population_mean+(3*population_sdev)

list_of_data_within_3_std_deviation = [
    result for result in data_list if result > thi_stan_dev_star and result < thi_stan_dev_en
]

sample_mean = (int(list_of_data_within_1_std_deviation) + int(list_of_data_within_2_std_deviation) + int(list_of_data_within_3_std_deviation)) / 3
print("The sample mean is", sample_mean)

z_score = (sample_mean - population_mean) / population_sdev
print("The z score is", z_score)

print("{}% of data lies within the 1st standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data_list)))
print("{}% of data lies within the 2nd standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data_list)))
print("{}% of data lies within the 3rd standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data_list)))

figure = pff.create_distplot([data_list],["Reading Time"], show_hist=False)
figure.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="Mean"))
figure.add_trace(go.Scatter(x=[population_sdev,population_sdev],y=[0,1],mode="lines",name="Standard Deviation"))

figure.add_trace(go.Scatter(x=[fir_stan_dev_star,fir_stan_dev_star],y=[0,0.17],mode="lines",name="First Standard Deviation Start"))
figure.add_trace(go.Scatter(x=[fir_stan_dev_en,fir_stan_dev_en],y=[0,0.17],mode="lines",name="First Standard Deviation End"))
figure.add_trace(go.Scatter(x=[sec_stan_dev_star,sec_stan_dev_star],y=[0,0.17],mode="lines",name="Second Standard Deviation Start"))
figure.add_trace(go.Scatter(x=[sec_stan_dev_en,sec_stan_dev_en],y=[0,0.17],mode="lines",name="Second Standard Deviation End"))
figure.add_trace(go.Scatter(x=[thi_stan_dev_star,thi_stan_dev_star],y=[0,0.17],mode="lines",name="Third Standard Deviation Start"))
figure.add_trace(go.Scatter(x=[thi_stan_dev_en,thi_stan_dev_en],y=[0,0.17],mode="lines",name="Third Standard Deviation End"))

figure.show()

def random_set_mean(counter): 
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data_list))
        value = data_list[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_figure(mean_list):
    df = mean_list
    figure = pff.create_distplot([df],["Responses"],show_hist=False)
    figure.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_mean(30)
        mean_list.append(set_of_means)
    show_figure(mean_list)

setup()