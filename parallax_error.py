#parallax error program
#
#Max parallax error = 0.5 * ObjectiveDiameter * (RangeToTarget - ScopeParallaxRange) / ScopeParallaxRange)
#
#Example
#
#30mm 60y scope, shooting at 100y = 10mm
#40mm 100y scope, shooting at 50y = 10mm
#30mm 60y scope, shooting at 200y = 47mm



def parallax_error(diameter, range_to_target, parallax_range):
  dia_print = diameter
  range_print = range_to_target
  par_print = parallax_range
  max_error = 0.5 * diameter * ((range_to_target - parallax_range) / parallax_range)
  print("for a %s mm diameter scope with a set parallax of %s yards, at a range of %s yards the max error is %s mm" % (dia_print, par_print, range_print,max_error))

parallax_error(40, 50, 100)

answer = 'y'
while answer == 'y':

  obj_diameter = int(input("please enter the bell diameter: "))
  range_to_target = int(input("please enter the range in yards: "))
  parallax_range = int(input("please enter the range the parallax is set at: "))

  parallax_error(obj_diameter, range_to_target, parallax_range)

  answer = input("do you wish to calculate another scope? y/n: ")
