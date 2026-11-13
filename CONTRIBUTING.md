# Contributing to asimov-rl

Thanks for considering a contribution. `asimov-rl` is a simulated humanoid in MuJoCo (MJX) driven by a low-level RL policy and a high-level vision-language-action model. The project is in its **design phase**: most files are empty placeholders (see [`README.md`](./README.md)). Contributions on the parts marked **planned** are especially welcome.

## Table of Contents

- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Contributing Code](#contributing-code)
- [Pull Request Process](#pull-request-process)
- [Commit Messages](#commit-messages)

## Reporting Bugs

Check existing issues first, then use the **bug report** template. Include:

- Steps to reproduce.
- Observed and expected behavior.
- Environment: OS, Python version, MuJoCo version, GPU and driver.

## Suggesting Enhancements

Use the **feature request** template. For research questions or experiments, use the **research and development** template. For documentation fixes, use the **documentation** template.

## Contributing Code

1. Fork the repository `synobotix/asimov-rl` and clone your fork.
2. Set up your environment with [`DEV.md`](./DEV.md).
3. Create a branch from `main`. Prefixes: `feat/`, `bugfix/`, `hotfix/`, `refactor/`, `docs/`, `test/`, `ci/`. Example: `feat/sim-humanoid-scene`.
4. Make your change. Add or update tests and docs with it.
5. Commit following [Commit Messages](#commit-messages).
6. Update your branch with `git rebase origin/main`. Do not merge `main` into it.
7. Push with `git push --force-with-lease` if you rewrote history, then open a pull request against `main`.

## Pull Request Process

The pull request template is empty for now. In the description, give the summary, the motivation, how you tested, and linked issues (`Closes #123`). Before you submit:

- [ ] The change is one topic.
- [ ] Pre-commit hooks pass (see [`DEV.md`](./DEV.md)).
- [ ] Tests exist for new behavior. Anything unimplemented is marked `NOT-IMPLEMENTED(#issue): reason`, with a linked issue.
- [ ] Docs are updated.
- [ ] The branch is rebased on `main`.
- [ ] You state what was **not** tested. Simulation results never imply real-robot performance.

Merge: rebase or fast-forward only.

## Commit Messages

Format: a gitmoji, then Conventional Commits, in English.

```
<gitmoji> <type>(<scope>)!: <description>

<body: why, not how>

<footer: BREAKING CHANGE: ..., Refs: #123>
```

Example:

```
✨ feat(sim): add humanoid scene

The simulation had no scene to load. Add a flat world and the
humanoid model entry point.

Refs: #12
```

- Types: `feat`, `fix`, `perf`, `refactor`, `test`, `docs`, `build`, `ci`, `chore`, `revert`, `style`.
- Imperative mood, lowercase description, no final period.
- `commitlint` (`.commitlint.config.js`, preset `gitmoji`) limits the header to 100 characters. The project rule is 72 characters, gitmoji included.

## Questions?

Open an issue for discussion.
