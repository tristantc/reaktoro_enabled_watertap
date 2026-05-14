#################################################################################
# WaterTAP Copyright (c) 2020-2026, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National Laboratory,
# National Laboratory of the Rockies, and National Energy Technology
# Laboratory (subject to receipt of any required approvals from the U.S. Dept.
# of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/reaktoro_enabled_watertap"
#################################################################################

__author__ = "Alexander V. Dudchenko"

from pyomo.environ import (
    units as pyunits,
)
from reaktoro_enabled_watertap.utils.reaktoro_utils import (
    ViablePrecipitantsBase,
)


class ViablePrecipitants(ViablePrecipitantsBase):
    def __init__(self):
        self.register_solid(
            "Calcite",
            100.09 * pyunits.g / pyunits.mol,
            {"Ca_2+": 1, "HCO3_-": 1},
            "Ca_2+",
            reaktoro_modifier={"Ca": -1, "C": -1, "O": -3},
        )
        self.register_solid(
            "Gypsum",
            172.17 * pyunits.g / pyunits.mol,
            {"Ca_2+": 1, "SO4_2-": 1},
            "Ca_2+",
            reaktoro_modifier={"Ca": -1, "S": -1, "O": -4},
        )
        self.register_solid(
            "Brucite",
            58.3197 * pyunits.g / pyunits.mol,
            {"Mg_2+": 1, "H2O": 2},
            "Mg_2+",
            reaktoro_modifier={"Mg": -1, "O": -2, "H": -2},
        )
