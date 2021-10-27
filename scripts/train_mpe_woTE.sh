#!/bin/sh
ulimit -n 32768
env="MPE"
scenario="push_ball"
num_landmarks=2
num_agents=2
# algo="woparentsampling_sp_4agents"
# algo="check"
algo='VACL_pb_final_check_woparent'
seed=1

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed}"

CUDA_VISIBLE_DEVICES=2 python train_mpe_woTE.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 120 --num_env_steps 100000000 --ppo_epoch 15 --recurrent_policy --use_popart --lr 5e-4 --use_accumulate_grad \
--buffer_length 2000 --epsilon 0.4 --delta 0.4 --sol_prop 0.0 --use_wandb

# CUDA_VISIBLE_DEVICES=0 python train_mpe_woTE.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 70 --num_env_steps 60000000 --ppo_epoch 15 --recurrent_policy --use_popart --lr 5e-4 --use_accumulate_grad \
# --buffer_length 2000 --use_wandb
