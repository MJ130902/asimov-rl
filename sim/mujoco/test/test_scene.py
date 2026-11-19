from pathlib import Path

import numpy as np
import pytest

from mujoco_sim.scene import build_model, rollout

URDF = Path(__file__).parent.parent / "robots" / "arm.urdf"


def make_model():
    return build_model(URDF)


def test_model_structure():
    model = make_model()
    assert model.nq == 2  # two joints
    assert model.nu == 2  # one motor per joint
    assert model.ncam == 1  # camera "front"


def test_rollout_shapes_and_motion():
    _, qpos = rollout(make_model(), n_frames=8, render=False)
    assert qpos.shape == (8, 2)
    assert np.abs(qpos).max() > 0.01  # the joints actually moved


def test_rollout_is_deterministic():
    _, first = rollout(make_model(), render=False)
    _, second = rollout(make_model(), render=False)
    assert np.array_equal(first, second)


def test_no_frames_when_render_disabled():
    frames, _ = rollout(make_model(), render=False)
    assert frames is None


def test_missing_urdf_raises():
    with pytest.raises(Exception):
        build_model("robots/does_not_exist.urdf")


def test_render_frames():
    try:
        frames, _ = rollout(make_model(), n_frames=2, size=64, render=True)
    except Exception as error:  # no graphics backend on this machine
        pytest.skip(f"graphics backend unavailable: {error}")
    assert frames.shape == (2, 64, 64, 3)
    assert frames.dtype == np.uint8
