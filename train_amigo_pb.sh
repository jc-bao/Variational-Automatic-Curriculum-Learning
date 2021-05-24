#!/bin/sh
ulimit -n 32768
env="MPE"
scenario="push_ball_goal_conditioned"
num_landmarks=4
num_agents=4
algo="amigo_pb_teacherhorizon10"
# algo="check"
seed=3

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed}"

CUDA_VISIBLE_DEVICES=0 python train_amigo_pb.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 8 --episode_length 120 --episode_length_teacher 10 --teacher_lr 1e-3 --num_env_steps 80000000 --ppo_epoch 15 --recurrent_policy --use_popart --lr 5e-4 --use_accumulate_grad 