from ._anvil_designer import Form2Template
from anvil import *

# data keys will contain a button "reserve, revoke"
# available IPs table, will contain a button "static"

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
