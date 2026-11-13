# Developer Guide

How to work on `asimov-rl`.

> **Status.** The project is in its design phase. There is no build, no test suite and no entry point yet. This guide documents what exists today and marks the rest **planned**. It will grow with the code.

> **Audience:** people modifying `asimov-rl`. For the project overview, read [`README.md`](./README.md).

## Table of contents

1. [Repository layout](#repository-layout)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Build, run and test](#build-run-and-test)
5. [Checks before a commit](#checks-before-a-commit)
6. [Workflow](#workflow)
7. [Conventions](#conventions)

## Repository layout

```
asimov-rl/
├── sim/
│   ├── mujoco/                  # MuJoCo / MJX simulation
│   │   ├── main.py              # entry point (empty)
│   │   ├── requirements.txt     # dependencies (empty)
│   │   ├── models/asimov.xml    # humanoid model (empty)
│   │   └── worlds/scene.xml     # scene (empty)
│   └── gazebo/                  # models, plugins, worlds (placeholders only)
├── src/
│   ├── nodes/                   # control, perception, navigation, localization, diagnostics
│   ├── shared/
│   ├── utils/
│   └── pyproject.toml           # (empty)
├── .devcontainer/               # dev container (see Known inconsistencies)
├── .github/                     # issue templates, PR template (empty), workflows (empty)
└── LICENSE                      # GNU GPL v3
```

Python packages under `src/nodes/` contain only `__init__.py` files.

## Prerequisites

Not pinned yet. Planned stack: Python, MuJoCo with MJX (JAX), PyTorch, LeRobot, and a compatible GPU. Versions will be pinned in `sim/mujoco/requirements.txt` and `src/pyproject.toml` when they exist.

## Setup

```bash
git clone https://github.com/synobotix/asimov-rl
cd asimov-rl
```

No dependency installation is available: `sim/mujoco/requirements.txt` and `src/pyproject.toml` are empty.

## Build, run and test

Not available (planned): running the simulation from `sim/mujoco/main.py`, training the walking policy, and a test suite. Add the command to this section in the same change that makes it work.

## Checks before a commit

`.pre-commit-config.yaml` defines the hooks. Install them with:

```bash
pip install pre-commit
pre-commit install
```

The config also has `commitlint` settings in `.commitlint.config.js` (preset `gitmoji`, header up to 100 characters). Commit message rules are in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Workflow

- Branch from `main`: `feat/`, `bugfix/`, `hotfix/`, `refactor/`, `docs/`, `test/`, `ci/`.
- Commit with a gitmoji and Conventional Commits, in English.
- Keep history linear: update with `git rebase origin/main`, push with `--force-with-lease`.
- Open a pull request against `main`. Merge by rebase or fast-forward only.
- Every commit builds and passes tests on its own, and mixes no refactor with a behavior change.

### ADRs

Structural decisions go through an ADR before code lands.

See existing ADRs → [docs/explanation/adr/](./docs/explanation/adr/index.md)

### Release process

```bash
git tag v0.4.0
```

## Conventions

### Priority order

When principles conflict, apply this order:

1. **Safety**: never weaken a limit, a safe default or a fault reaction.
2. **Correctness**: the code does what the requirement says, including failure modes.
3. **Simplicity**: the simplest design that meets 1 and 2.
4. **Performance**: measure before optimizing.
5. **Reuse and elegance**: DRY, abstractions, generality.

### Clean code

- Name things by intent. Put the unit in the name when a value has one: `max_speed_mps`, `control_period_s`. Use SI units everywhere.
- Keep functions small, with one level of abstraction and few arguments. Keep McCabe complexity at 10 or less (the `flake8` setting in `.pre-commit-config.yaml`).
- Comment the why, not the what. Delete dead code and commented-out code. Git keeps history.
- Add type hints to public functions and data structures. Prefer dataclasses and enums to loose dicts and string flags.
- Make illegal states unrepresentable: validate at the boundary (config, commands, observations) and fail fast on invalid input.
- No magic numbers. Name every constant and keep one source of truth for it (reward weights, limits, control rates, joint order).

### YAGNI

- Build what the current step of the pipeline needs. No speculative parameters, plugin systems or generic frameworks.
- Do not abstract for hardware or a model that is not real and scheduled. Gazebo stays a placeholder until someone needs it.

### KISS

- Prefer a plain function and a direct call to a class hierarchy or an indirection.
- Prefer the design a new contributor understands in one reading. Prefer explicit configuration to implicit behavior.

### DRY

- Remove duplicated **knowledge** (a limit, a conversion, an observation layout), not code that only looks alike.
- Extract an abstraction at the third occurrence, not before.

### SOLID, applied here

- **Single responsibility:** one module, one reason to change. Keep environment dynamics, reward, policy, training loop and logging in separate modules.
- **Open/closed:** add a task, a reward term or an observation by adding code behind an existing interface, not by editing validated code.
- **Liskov substitution:** a simulated, mocked and real implementation of the same interface behave the same within the contract (units, shapes, timing, errors).
- **Interface segregation:** small role-based interfaces, for example a policy that only maps observation to action.
- **Dependency inversion:** training and control logic depend on abstractions. The entry point (`sim/mujoco/main.py`) binds concrete implementations.
- Prefer composition to inheritance.

### Errors and unimplemented behavior

- Unimplemented behavior fails loudly. Do not return a fake success or a placeholder value. Mark the spot with `NOT-IMPLEMENTED(#issue): reason` and open the issue in the same change.
- Never swallow an exception. Catch only what you can handle. Log or re-raise with context.

### Reproducibility

- Seed every source of randomness and record the seed with each run.
- Keep hyperparameters and configuration in files under version control, not hard-coded in scripts.
- Record the library versions, the config and the commit of every training run.

### Tests

- Test behavior, not implementation. Use the Arrange, Act, Assert pattern.
- A bug fix comes with a regression test.
- Skipped tests for unimplemented behavior reference the issue.

### Simulation honesty

- Simulation results never imply real-robot performance. Sim-to-real is not validated.
- Do not commit secrets, keys or large binaries.
