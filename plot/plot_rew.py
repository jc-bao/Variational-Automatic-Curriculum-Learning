import matplotlib.pyplot as plt
import json
import pdb
import numpy as np
import os
import csv

def main():
    scenario = 'simple_spread_3rooms'
    save_dir = './' + scenario + '/'
    save_name = 'sp3_asym'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    plt.style.use('ggplot')

    # # uniform_add_easy_sp
    # exp_name = 'sp_addeasy'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.json'
    # with open(data_dir,'r') as csvfile:
    #     plots = json.load(csvfile)
    #     for env in plots['results/MPE/simple_spread/sp_add_easy/run1/logs/agent/cover_rate_5step/cover_rate_5step']:
    #         x_step1.append(env[1])
    #         y_seed1.append(env[2])
    # data_dir =  './' + exp_name + '_seed2' + '.json'
    # with open(data_dir,'r') as csvfile:
    #     plots = json.load(csvfile)
    #     for env in plots['results/MPE/simple_spread/sp_add_easy/run2/logs/agent/cover_rate_5step/cover_rate_5step']:
    #         x_step2.append(env[1])
    #         y_seed2.append(env[2])
    # data_dir =  './' + exp_name + '_seed3' + '.json'
    # with open(data_dir,'r') as csvfile:
    #     plots = json.load(csvfile)
    #     for env in plots['results/MPE/simple_spread/sp_add_easy/run3/logs/agent/cover_rate_5step/cover_rate_5step']:
    #         x_step3.append(env[1])
    #         y_seed3.append(env[2])
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    # for i in range(len(y_seed1)):
    #     y_seed1[i] = np.float(y_seed1[i])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    # for i in range(len(y_seed2)):
    #     y_seed2[i] = np.float(y_seed2[i])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    # for i in range(len(y_seed3)):
    #     y_seed3[i] = np.float(y_seed3[i])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)[0:1150]
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1)[0:1150]
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label='uniform + easy case',color='tab:brown')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # reverse_eval1
    # exp_name = 'reverse_eval1_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label='reverse goal generation')
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # reverse_novelty
    # exp_name = 'reverse_novelty_sp'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label='novelty_exploration')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('novelty_exploration')

    # # main_results
    # exp_name = 'diversified_novelty_parentsampling_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label='ours')
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('main results')

    # # reverse_eval3
    # exp_name = 'reverse_eval3_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label='eval3')
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('eval_times')

    # # reverse_diversified
    # exp_name = 'reverse_diversified_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label='diversified_active_set')
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('diversified_active_set')

    # # solved_eval1
    # exp_name = 'solved_eval1_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label='SampleNearby from solved set')
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('SampleNearby')

    # # reverse_diversified
    # exp_name = 'reverse_parentsampling_sp'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label='With parentsampling')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('parentsampling')


    begin = 0
    # sp3
    # queue
    exp_name = 'solved_sp3'
    # data_dir =  './' + exp_name + '.csv'
    x_step1 = []
    y_seed1 = []
    x_step2 = []
    y_seed2 = []
    x_step3 = []
    y_seed3 = []
    x_step4 = []
    y_seed4 = []
    # load data ranking by seed
    data_dir =  './' + exp_name + '_seed1' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step1.append(row[0])
            y_seed1.append(row[1:])
    data_dir =  './' + exp_name + '_seed2' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step2.append(row[0])
            y_seed2.append(row[1:])
    data_dir =  './' + exp_name + '_seed3' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step3.append(row[0])
            y_seed3.append(row[1:])
    data_dir =  './' + exp_name + '_seed4' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step4.append(row[0])
            y_seed4.append(row[1:])
    x_step1 = x_step1[1:]
    y_seed1 = y_seed1[1:]
    x_step2 = x_step2[1:]
    y_seed2 = y_seed2[1:]
    x_step3 = x_step3[1:]
    y_seed3 = y_seed3[1:]
    x_step4 = x_step4[1:]
    y_seed4 = y_seed4[1:]
    length = min((len(x_step1),len(x_step2),len(x_step3),len(x_step4)))
    for i in range(len(x_step1)):
        x_step1[i] = np.float(x_step1[i])
        for j in range(len(y_seed1[i])):
            y_seed1[i][j] = np.float(y_seed1[i][j])
    for i in range(len(x_step2)):
        x_step2[i] = np.float(x_step2[i])
        for j in range(len(y_seed2[i])):
            y_seed2[i][j] = np.float(y_seed2[i][j])
    for i in range(len(x_step3)):
        x_step3[i] = np.float(x_step3[i])
        for j in range(len(y_seed3[i])):
            y_seed3[i][j] = np.float(y_seed3[i][j])
    for i in range(len(x_step4)):
        x_step4[i] = np.float(x_step4[i])
        for j in range(len(y_seed4[i])):
            y_seed4[i][j] = np.float(y_seed4[i][j])
    x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length],x_step4[0:length]),axis=1)[begin:]
    y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length],y_seed4[0:length]),axis=1).squeeze(2)[begin:]
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    timesteps = np.mean(x_step,axis=1)
    plt.plot(timesteps,mean_seed,label='tech1: sample from solved set')
    plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # diversified_sp3
    exp_name = 'diversified_sp3'
    # data_dir =  './' + exp_name + '.csv'
    x_step1 = []
    y_seed1 = []
    x_step2 = []
    y_seed2 = []
    x_step3 = []
    y_seed3 = []
    x_step4 = []
    y_seed4 = []
    # load data ranking by seed
    data_dir =  './' + exp_name + '_seed1' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step1.append(row[0])
            y_seed1.append(row[1:])
    data_dir =  './' + exp_name + '_seed2' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step2.append(row[0])
            y_seed2.append(row[1:])
    data_dir =  './' + exp_name + '_seed3' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step3.append(row[0])
            y_seed3.append(row[1:])
    data_dir =  './' + exp_name + '_seed4' + '.csv'
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step4.append(row[0])
            y_seed4.append(row[1:])
    x_step1 = x_step1[1:]
    y_seed1 = y_seed1[1:]
    x_step2 = x_step2[1:]
    y_seed2 = y_seed2[1:]
    x_step3 = x_step3[1:]
    y_seed3 = y_seed3[1:]
    x_step4 = x_step4[1:]
    y_seed4 = y_seed4[1:]
    length = min((len(x_step1),len(x_step2),len(x_step3),len(x_step4)))
    for i in range(len(x_step1)):
        x_step1[i] = np.float(x_step1[i])
        for j in range(len(y_seed1[i])):
            y_seed1[i][j] = np.float(y_seed1[i][j])
    for i in range(len(x_step2)):
        x_step2[i] = np.float(x_step2[i])
        for j in range(len(y_seed2[i])):
            y_seed2[i][j] = np.float(y_seed2[i][j])
    for i in range(len(x_step3)):
        x_step3[i] = np.float(x_step3[i])
        for j in range(len(y_seed3[i])):
            y_seed3[i][j] = np.float(y_seed3[i][j])
    for i in range(len(x_step4)):
        x_step4[i] = np.float(x_step4[i])
        for j in range(len(y_seed4[i])):
            y_seed4[i][j] = np.float(y_seed4[i][j])
    x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length],x_step4[0:length]),axis=1)[begin:]
    # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length],y_seed4[0:length]),axis=1).squeeze(2)[begin:]
    # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    timesteps = np.mean(x_step,axis=1)
    plt.plot(timesteps,mean_seed,label='tech2: diversified active set')
    plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # tech3
    exp_name = 'diversified_novelty_parentsampling_sp3'
    data_dir =  './' + exp_name + '.csv'
    x_step = []
    y_seed = []
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step.append(row[0])
            y_seed.append(row[1:])
    x_step = x_step[1:]
    y_seed = y_seed[1:]
    for i in range(len(x_step)):
        x_step[i] = np.float(x_step[i])
        for j in range(len(y_seed[i])):
            y_seed[i][j] = np.float(y_seed[i][j])
    x_step = np.array(x_step)[begin:]
    y_seed = np.array(y_seed)[begin:]
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    plt.plot(x_step,mean_seed,label='tech3: novelty exploration + parentsampling')
    plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    plt.title('simple_spread_3rooms')

    # # mix
    # exp_name = 'mix_sp'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)[0:200]
    # std_seed = np.std(y_seed,axis=1)[0:200]
    # timesteps = np.mean(x_step,axis=1)[0:200]
    # plt.plot(timesteps,mean_seed,label='mix')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # mix_decay
    # exp_name = 'mixdecay_sp'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label='mix decay')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # mix_decay
    # exp_name = 'mixdecay_sp_0to1'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))-190
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label='mix decay 0to1')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # phase_sp
    # exp_name = 'phase_sp'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label='phase')
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)
    # plt.title('Massive entities')

    # # withoutwarmup
    # exp_name = 'withoutwarmup_sp'
    # # data_dir =  './' + exp_name + '.csv'
    # x_step1 = []
    # y_seed1 = []
    # x_step2 = []
    # y_seed2 = []
    # x_step3 = []
    # y_seed3 = []
    # # load data ranking by seed
    # data_dir =  './' + exp_name + '_seed1' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step1.append(row[0])
    #         y_seed1.append(row[1:])
    # data_dir =  './' + exp_name + '_seed2' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step2.append(row[0])
    #         y_seed2.append(row[1:])
    # data_dir =  './' + exp_name + '_seed3' + '.csv'
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step3.append(row[0])
    #         y_seed3.append(row[1:])
    # x_step1 = x_step1[1:]
    # y_seed1 = y_seed1[1:]
    # x_step2 = x_step2[1:]
    # y_seed2 = y_seed2[1:]
    # x_step3 = x_step3[1:]
    # y_seed3 = y_seed3[1:]
    # length = min((len(x_step1),len(x_step2),len(x_step3)))
    # for i in range(len(x_step1)):
    #     x_step1[i] = np.float(x_step1[i])
    #     for j in range(len(y_seed1[i])):
    #         y_seed1[i][j] = np.float(y_seed1[i][j])
    # for i in range(len(x_step2)):
    #     x_step2[i] = np.float(x_step2[i])
    #     for j in range(len(y_seed2[i])):
    #         y_seed2[i][j] = np.float(y_seed2[i][j])
    # for i in range(len(x_step3)):
    #     x_step3[i] = np.float(x_step3[i])
    #     for j in range(len(y_seed3[i])):
    #         y_seed3[i][j] = np.float(y_seed3[i][j])
    # x_step = np.stack((x_step1[0:length],x_step2[0:length],x_step3[0:length]),axis=1)
    # # x_step = np.stack((x_step1[0:length],x_step3[0:length]),axis=1)[0:190]
    # x_step = x_step-x_step[0] # 从0开始计数
    # y_seed = np.stack((y_seed1[0:length],y_seed2[0:length],y_seed3[0:length]),axis=1).squeeze(2)
    # # y_seed = np.stack((y_seed1[0:length],y_seed3[0:length]),axis=1).squeeze(2)[0:190]
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # timesteps = np.mean(x_step,axis=1)
    # plt.plot(timesteps,mean_seed,label=exp_name)
    # plt.fill_between(timesteps,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # plt.xlabel('timesteps')
    # plt.ylabel('coverage rate')
    # plt.legend()
    # plt.savefig(save_dir + save_name + '.jpg')

    # scenario = 'simple_spread'
    # save_dir = './' + scenario + '/'
    # save_name = 'sp_tricks'
    # if not os.path.exists(save_dir):
    #     os.makedirs(save_dir)

    # # solved_sp
    # exp_name = 'solved_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # diversified_sp
    # exp_name = 'diversified_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # diversified_novelty_sp
    # exp_name = 'diversified_novelty_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # diversified_novelty_parentsampling_sp
    # exp_name = 'diversified_novelty_parentsampling_sp'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # plt.xlabel('timesteps')
    # plt.ylabel('coverage rate')
    # plt.legend()
    # plt.savefig(save_dir + save_name + '.jpg')


    plt.xlabel('timesteps')
    plt.ylabel('coverage rate')
    plt.legend()
    plt.savefig(save_dir + save_name + '.jpg')

if __name__ == "__main__":
    main()