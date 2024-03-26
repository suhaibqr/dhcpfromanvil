from ._anvil_designer import DHCPFormTemplate
from anvil import *

from .. import DemoVariables

# data keys will contain a button "reserve, revoke"
# available IPs table, will contain a button "static"

class DHCPForm(DHCPFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def update_data_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    DemoVariables.update_dhcp()
    pass
