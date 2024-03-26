from ._anvil_designer import DHCPFormTemplate
from anvil import *
import anvil.server
from .. import DemoVariables

# data keys will contain a button "reserve, revoke"
# available IPs table, will contain a button "static"

class DHCPForm(DHCPFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def update_data_btn_click(self, **event_args):
    with Notification("Please Wait While Updating"):
      self.repeating_panel_dhcp.items = anvil.server.call('get_available_ips')
    Notification("Update Was Successful")
    """This method is called when the button is clicked"""


  def check_ip_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    s = anvil.server.call('u_check_ip_availability', self.ip_address_input_box.text)
    alert(s)

