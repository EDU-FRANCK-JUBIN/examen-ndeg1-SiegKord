# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:58:40 2019

@author: Nicolas
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

error = ctrl.Antecedent(np.arange(-4, 4, 1), 'error')
error_dot= ctrl.Antecedent(np.arange-10, 10, 1), 'error_dot')
percent_output = ctrl.Consequent(np.arange(-100, 100, 1), 'percent_output')

error_name = ["Too_cold", "Just_right", "Too_hot"]
error_dot_name = ["Getting_colder", "No_change", "Getting_hotter"]

error.automf(names=error_name)
error_dot.automf(names=error_dot_name)

error.view()
error_dot.view()

percent_output['Cool'] = fuzz.trimf(percent_output.universe, [0, 8, 12])


percent_output.view()


rule1 = ctrl.Rule(degree_dirt['High'] | type_dirt['Fat'], wash_time['very_long'])



washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
washing = ctrl.ControlSystemSimulation(washing_ctrl)

washing.input['degree_dirt'] = 40
washing.input['type_dirt'] = 70

washing.compute()

print(washing.output['wash_time'])
percent_output.view(sim=washing)
