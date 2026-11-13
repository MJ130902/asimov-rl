# asimov-rl

A humanoid simulated in MuJoCo (MJX, on GPU). A low-level reinforcement-learning policy keeps it balanced and walking. A high-level vision-language-action model understands the scene and the instruction. The goal: everyday tasks such as fetching an object and moving through an environment shared with simulated humans.

!!! warning "Design phase"
    This documentation describes design decisions and a plan, not shipped code. No training run, test or result exists. No performance is claimed, and sim-to-real is **not validated**. Anything marked **planned** is not implemented.

## How it works

Two levels, running at different rates:

| Level | Role | Approach | Target rate | Inputs | Outputs |
|---|---|---|---|---|---|
| Low level | Balance, walking, push robustness | RL policy (PPO), trained in MJX | 100 to 500 Hz | Speed, turn rate, pelvis height, hand targets | Joint torques or targets |
| High level | Understand the scene and the instruction | SmolVLA (LeRobot) | ~5 to 10 Hz | Cameras and a text instruction | 3D hand positions, walking velocity vector |

The high level never outputs raw joint angles. It sends simple commands to the low level.

## Where to go next

The documentation is organized by component.

| Section | What you find there | Status |
|---|---|---|
| Overview | System architecture, two-level control, glossary | Planned |
| Simulation (MuJoCo / MJX) | Humanoid model, scenes, running the simulation | Planned |
| Low-level policy (PPO) | Observations, actions, reward, training, evaluation | Planned |
| High-level planner (SmolVLA) | Language commands, interface with the policy | Planned |
| Sim-to-real | Noise and latency models, randomization, gap log | Planned |
| Project | Dev container, repository layout, decisions (ADR) | Planned |

## Training plan (planned)

1. Walking with RL only.
2. Whole-body control: arms reach a 3D target.
3. Connect SmolVLA to virtual cameras.
4. Supervised fine-tuning on about 50 demonstrations in LeRobot format.
5. RL fine-tuning with moving obstacles.

## Known risks

- **Camera rendering cost.** Rendering at 128x128 or 224x224 with Madrona and MJX is considered. Latency and GPU memory are to be verified. No measurement exists.
- **Sim-to-real gap.** No real-robot test is planned at this stage.

## Contributing

See `README.md`, `DEV.md` and `CONTRIBUTING.md` at the repository root.
