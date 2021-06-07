#!/usr/bin/env python

import sys
sys.path.append("/SNS/users/8cz/Workbench/Mantid/PD269_binningErrorInAlignAndFocusPowder/mantid_total_scattering")

import json
from total_scattering.reduction import TotalScatteringReduction

# calibration file d143068_2020_02_11
jsonfile = "/SNS/NOM/shared/User_story_test/NOM_US-269/mantidts_test/ceriaBulk_PAC06_at_10K_IDL_Calib.json"
# calibration file d131573_2019_08_18
# jsonfile = "/SNS/NOM/shared/User_story_test/NOM_US-269/mantidts_test_another_another/SrTiO3_CAP03_summed_at_300K_IDL_Calib.json"

with open(jsonfile, 'r') as jf:
    config = json.load(jf)

# execute
TotalScatteringReduction(config)
