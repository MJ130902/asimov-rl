"""Load a URDF, simulate it and print the joint positions.

Usage (from sim/mujoco/):
    python scripts/run_demo.py                      # robots/arm.urdf
    python scripts/run_demo.py --urdf robots/other.urdf
"""
import argparse

import numpy as np

from mujoco_sim.scene import build_model, rollout

parser = argparse.ArgumentParser()
parser.add_argument("--urdf", default="robots/arm.urdf")
args = parser.parse_args()

model = build_model(args.urdf)
print(f"bodies={model.nbody} joints={model.njnt} actuators={model.nu} cameras={model.ncam}")
_, qpos = rollout(model, n_frames=40, render=False)
print("joint positions per frame:\n", np.round(qpos, 3))
