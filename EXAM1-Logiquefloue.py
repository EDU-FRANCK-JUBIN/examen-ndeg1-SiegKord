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

percent_output['Cool'] = fuzz.trimf(percent_output.universe, [-100, -50, 0])
percent_output['Do_nothing'] = fuzz.trimf(percent_output.universe, [-50, 0, 50])
percent_output['Heat'] = fuzz.trimf(percent_output.universe, [0, 50, 100])


percent_output.view()


rule1 = ctrl.Rule(error['Too_hot'] | error_dot['Getting_colder'], percent_output['Cool'])
rule2 = ctrl.Rule(error['Just_right'] | error_dot['Getting_colder'], percent_output['Cool'])
rule3 = ctrl.Rule(error['Too_cold'] | error_dot['Getting_colder'], percent_output['Cool'])
rule4 = ctrl.Rule(error['Too_hot'] | error_dot['No_change'], percent_output['Cool'])
rule5 = ctrl.Rule(error['Jus_right'] | error_dot['No_change'], percent_output['Cool'])
rule6 = ctrl.Rule(error['Too_cold'] | error_dot['No_change'], percent_output['Cool'])
rule7 = ctrl.Rule(error['Too_hot'] | error_dot['Getting_hotter'], percent_output['Cool'])
rule8 = ctrl.Rule(error['Just_right'] | error_dot['Getting_hotter'], percent_output['Cool'])
rule9 = ctrl.Rule(error['Too_cold'] | error_dot['Getting_hotter'], percent_output['Cool'])



percent_output_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
percent = ctrl.ControlSystemSimulation(percent_output_ctrl)

percent.input['error'] = -1.5
percent.input['error_dot'] = -4

percent.compute()

percent.input['error'] = -1.5
percent.input['error_dot'] = -1

percent.compute()

percent.input['error'] = 0.5
percent.input['error_dot'] = 1

percent.compute()

percent.input['error'] = 0.5
percent.input['error_dot'] = 4

percent.compute()

print(percent.output['percent_output'])
percent_output.view(sim=percent)
