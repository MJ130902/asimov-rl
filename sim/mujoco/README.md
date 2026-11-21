# mujoco-sim

Robotics simulation with [MuJoCo](https://github.com/google-deepmind/mujoco): load a robot described in a URDF file, add what URDF cannot describe (floor, light, camera, motors) and simulate it.

## Setup

Run everything from `sim/mujoco/`.

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1      # Windows PowerShell (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
pip install -e .
```

Optional dependencies are in `requirements-rl.txt` (reinforcement learning) and `requirements-video.txt` (video recording), when present.

## Tests

```bash
python -m pytest -v
```

Each feature has its own page under `docs/`.
