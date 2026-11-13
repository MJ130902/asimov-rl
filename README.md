<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![Tech][tech-shield]][tech-url]
[![CI][ci-shield]][ci-url]
[![Coverage][coverage-shield]][coverage-url]

<br />
<div align="center">
<h3 align="center">asimov-rl</h3>

  <p align="center">
    A simulated humanoid in MuJoCo (MJX) driven by a low-level RL policy and a high-level vision-language-action model (status: design phase, nothing shipped)
    <br />
    <a href="https://github.com/Synobotix/asimov-rl"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Synobotix/asimov-rl/issues/new?labels=bug&template=bug-report---.yml">Report Bug</a>
    &middot;
    <a href="https://github.com/Synobotix/asimov-rl/issues/new?labels=enhancement&template=feature-request---.yml">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

A humanoid simulated in MuJoCo (MJX, on GPU) that must perform everyday tasks: fetch an object and move around in an environment shared with simulated humans.

> **Repository status.** What follows describes **design decisions and a plan**, not shipped code. The repository currently contains only the directory layout: `sim/mujoco/` (`main.py`, `models/asimov.xml`, `worlds/scene.xml` and `requirements.txt` are empty), empty Python packages under `src/nodes/` (`control`, `perception`, `navigation`, `localization`, `diagnostics`) and an empty `src/pyproject.toml`. No training, test or result exists, and no performance is claimed. Anything marked **planned** is not implemented.

**Hierarchical architecture (planned)**

| Level | Role | Approach | Target rate | Inputs | Outputs |
|---|---|---|---|---|---|
| Low level ("cerebellum") | Balance, walking, push robustness | Pure RL policy (PPO), trained in MJX | 100 to 500 Hz | Simple commands: forward/backward speed, turn rate, pelvis height, hand targets | Joint torques or joint targets |
| High level ("brain") | Understand the scene and the instruction | SmolVLA (~450M parameters, LeRobot): frozen VLM + trained Action Expert | ~5 to 10 Hz | Cameras + text instruction | Spatial targets: 3D hand positions, walking velocity vector |

- The low level is later extended to whole-body control (arms reaching a 3D target).
- The high level **never** outputs raw joint angles: SmolVLA is pre-trained on fixed arms (SO-100), not on a biped.

**Training pipeline (planned)**

1. Walking with RL only.
2. Whole-body control (arms reaching a 3D target).
3. Connect SmolVLA to virtual cameras.
4. SFT on ~50 demonstrations in LeRobot format.
5. RL fine-tuning with moving obstacles: DPPO / Flow-GRPO, or a residual RL layer (flow matching makes the action log-probability hard to use with PPO).

**Simulated humans (planned)**

Agents following a Social Force Model, represented by cylinders or mannequins in the scene XML.

**Known risks**

- Camera rendering cost: 128x128 or 224x224 resolution with Madrona + MJX is considered. Latency and GPU memory are **to be verified**; no measurement exists.
- Sim-to-real is **not validated**: no real-robot test is planned at this stage of the repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

Badges below show the intended stack. Only Python is used today; the rest is **planned** and not yet declared (`sim/mujoco/requirements.txt` is empty).

* [![Python][Python]][python-url]
* [![MuJoCo][MuJoCo]][mujoco-url]
* [![JAX][JAX]][jax-url]
* [![PyTorch][PyTorch]][pytorch-url]
* [![Hugging Face][HuggingFace]][huggingface-url] (SmolVLA, LeRobot)
* [![NumPy][NumPy]][numpy-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

No setup or run procedure is available: the dependency and entry-point files (`sim/mujoco/requirements.txt`, `sim/mujoco/main.py`, `src/pyproject.toml`) are empty. This section will be filled once a tested command exists.

### Prerequisites

To be defined (planned: Python, MuJoCo/MJX, a compatible GPU). Versions are not pinned.

### Installation

Not available (planned).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Not available: no entry point is implemented (planned: launching the simulation in `sim/mujoco/`, training the walking policy).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome, especially on the parts marked **planned**. For a suggestion, open an issue with the `enhancement` label or a pull request.

1. Fork the project
2. Create a branch (`git checkout -b feat/my-feature`), prefixes: `feat/`, `bugfix/`, `refactor/`, `docs/`, `test/`, `ci/`
3. Commit using gitmoji + Conventional Commits, in English (`git commit -m "✨ feat(sim): add humanoid scene"`)
4. Push the branch (`git push origin feat/my-feature`)
5. Open a Pull Request

Update your branch with rebase, not merge.

For more info please read [CONTRIBUTING.md](./CONTRIBUTING.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/Synobotix/asimov-rl/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Synobotix/asimov-rl" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

Distributed under the GNU GPL v3 license. See [`LICENSE`](./LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[tech-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[tech-url]: https://www.python.org/
[ci-shield]: https://img.shields.io/github/actions/workflow/status/synobotix/asimov-rl/ci.yml?style=for-the-badge&label=CI
[ci-url]: https://github.com/synobotix/asimov-rl/actions
[coverage-shield]: https://img.shields.io/codecov/c/gh/synobotix/asimov-rl?style=for-the-badge
[coverage-url]: https://codecov.io/gh/synobotix/asimov-rl
[contributors-shield]: https://img.shields.io/github/contributors/Synobotix/asimov-rl.svg?style=for-the-badge
[contributors-url]: https://github.com/Synobotix/asimov-rl/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Synobotix/asimov-rl.svg?style=for-the-badge
[forks-url]: https://github.com/Synobotix/asimov-rl/network/members
[stars-shield]: https://img.shields.io/github/stars/Synobotix/asimov-rl.svg?style=for-the-badge
[stars-url]: https://github.com/Synobotix/asimov-rl/stargazers
[issues-shield]: https://img.shields.io/github/issues/Synobotix/asimov-rl.svg?style=for-the-badge
[issues-url]: https://github.com/Synobotix/asimov-rl/issues
[license-shield]: https://img.shields.io/github/license/Synobotix/asimov-rl.svg?style=for-the-badge
[license-url]: https://github.com/Synobotix/asimov-rl/blob/main/LICENSE

[Python]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[MuJoCo]: https://img.shields.io/badge/MuJoCo-0B5CAD?style=for-the-badge
[mujoco-url]: https://mujoco.org/
[JAX]: https://img.shields.io/badge/JAX-5E97F6?style=for-the-badge&logo=jax&logoColor=white
[jax-url]: https://github.com/jax-ml/jax
[PyTorch]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[pytorch-url]: https://pytorch.org/
[HuggingFace]: https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black
[huggingface-url]: https://huggingface.co/lerobot
[NumPy]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[numpy-url]: https://numpy.org/
