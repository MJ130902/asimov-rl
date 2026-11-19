import os
from pathlib import Path

import mujoco
import pytest

from mujoco_sim.humanoid import StandingController, build_asimov, place_on_floor

XML = os.environ.get("ASIMOV_XML", "")
pytestmark = pytest.mark.skipif(not Path(XML).is_file(), reason="set ASIMOV_XML to asimov_1_25dof.xml")


def test_model_has_one_servo_per_joint():
    model = build_asimov(XML)
    assert model.nu == 25
    assert model.njnt == 26  # 25 hinges + the floating base


def test_stands_for_eight_seconds():
    model = build_asimov(XML)
    data = mujoco.MjData(model)
    place_on_floor(model, data)
    controller = StandingController(model)
    while data.time < 8.0:
        controller(data)
        mujoco.mj_step(model, data)
    assert data.qpos[2] > 0.55


def test_falls_without_balance_controller():
    model = build_asimov(XML)
    data = mujoco.MjData(model)
    place_on_floor(model, data)
    while data.time < 4.0:
        mujoco.mj_step(model, data)
    assert data.qpos[2] < 0.5
