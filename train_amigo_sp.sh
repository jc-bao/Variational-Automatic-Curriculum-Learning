#!/bin/sh
ulimit -n 32768
env="MPE"
scenario="simple_spread_goal_conditioned"
num_landmarks=8
num_agents=8
# algo="check"
algo='amigo_map6_teacherhorizon10_agent8'
seed=3

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed}"

# for seed in `seq ${seed_max}`;
# do
#     echo "seed is ${seed}:"
#     CUDA_VISIBLE_DEVICES=3 python train_mpe_curriculum_sp.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 70 --num_env_steps 40000000 --ppo_epoch 15 --recurrent_policy --use_popart --use-max-grad-norm
#     echo "training is done!"
# done
CUDA_VISIBLE_DEVICES=0 python train_amigo_sp.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 8 --episode_length 70 --episode_length_teacher 10 --teacher_lr 1e-3 --num_env_steps 40000000 --ppo_epoch 15 --recurrent_policy --use_popart 
