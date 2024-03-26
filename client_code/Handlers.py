import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

actions_id = None

def say_hello():
  print("Hello, world")

def save_actions_id(i):
  global actions_id
  actions_id = i

def get_actions_id():
  return actions_id