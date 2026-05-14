#################################################################################
# WaterTAP Copyright (c) 2020-2026, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National Laboratory,
# Laboratory of the Rockies, and National Energy Technology
# Laboratory (subject to receipt of any required approvals from the U.S. Dept.
# of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/reaktoro_enabled_watertap"
#################################################################################

import pytest
from pyomo.environ import units as pyunits, value

from reaktoro_enabled_watertap.utils.crystallizer_reaktoro_utils import (
    ViablePrecipitants,
)


@pytest.mark.core
def test_viable_precipitants_defaults_present():
    vp = ViablePrecipitants()

    assert set(vp.keys()) == {"Calcite", "Gypsum", "Brucite"}


@pytest.mark.core
@pytest.mark.parametrize(
    "solid, expected_primary_ion, expected_stoich, expected_modifier",
    [
        (
            "Calcite",
            "Ca_2+",
            {"Ca_2+": 1, "HCO3_-": 1},
            {"Ca": -1, "C": -1, "O": -3},
        ),
        (
            "Gypsum",
            "Ca_2+",
            {"Ca_2+": 1, "SO4_2-": 1},
            {"Ca": -1, "S": -1, "O": -4},
        ),
        (
            "Brucite",
            "Mg_2+",
            {"Mg_2+": 1, "H2O": 2},
            {"Mg": -1, "O": -2, "H": -2},
        ),
    ],
)
def test_viable_precipitants_registration_data(
    solid, expected_primary_ion, expected_stoich, expected_modifier
):
    vp = ViablePrecipitants()

    assert vp[solid]["primary_ion"] == expected_primary_ion
    assert vp[solid]["precipitation_stoichiometric"] == expected_stoich
    assert vp[solid]["reaktoro_modifier"] == expected_modifier


@pytest.mark.core
@pytest.mark.parametrize(
    "solid, expected_mw_g_per_mol",
    [
        ("Calcite", 100.09),
        ("Gypsum", 172.17),
        ("Brucite", 58.3197),
    ],
)
def test_viable_precipitants_molecular_weight(solid, expected_mw_g_per_mol):
    vp = ViablePrecipitants()

    mw = value(pyunits.convert(vp[solid]["mw"], to_units=pyunits.g / pyunits.mol))
    assert pytest.approx(mw, rel=1e-8) == expected_mw_g_per_mol
