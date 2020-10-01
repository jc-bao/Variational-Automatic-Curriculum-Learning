#!/bin/sh
env="MPE"
scenario_name="simple_spread"
# scenario_name="push_ball"
seed_max=1

echo "env is ${env}"
for seed in `seq ${seed_max}`
do
    CUDA_VISIBLE_DEVICES=2 python eval_mpe.py --env_name ${env} --seed ${seed} --scenario_name ${scenario_name} --episode_length 120 --eval_episodes 50 --recurrent_policy --num_landmarks 16 --num_agents 16 --model_dir "/home/tsing73/curriculum/results/MPE/simple_spread/optimizer2_true/" # --save_gifs
done
