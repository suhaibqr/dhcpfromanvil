from ._anvil_designer import DHCPFormTemplate
from anvil import *
import anvil.server
from .. import Handlers


# data keys will contain a button "reserve, revoke"
# available IPs table, will contain a button "static"

class DHCPForm(DHCPFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def update_data_btn_click(self, **event_args):
    with Notification("Please Wait While Updating"):
      aa = self.dhcp_grid.columns[-1]["id"]
      Handlers.save_actions_id(aa)
      r = anvil.server.call('get_available_ips')
      self.repeating_panel_statistics.items = r
      self.interface_drop_menu.items = [x["interface"] for x in r]
      self.interface_drop_menu.selected_value = None
    Notification("Update Was Successful")
    
    # print(self.repeating_panel_statistics.items)
    
    """This method is called when the button is clicked"""


  def check_ip_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    s = anvil.server.call('u_check_ip_availability', self.ip_address_input_box.text)
    alert(s)

  def interface_drop_menu_change(self, **event_args):
    """This method is called when an item is selected"""
    dhcp = anvil.server.call('anvil_grid_dhcp_details', self.interface_drop_menu.selected_value)
    arp =  anvil.server.call('anvil_grid_arp', self.interface_drop_menu.selected_value)
    self.repeating_panel_dhcp.items = dhcp
    self.repeating_panel_arp.items = arp
    pass

  def show_statistics_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    # print(self.show_statistics_checkbox.)
    self.statistics_grid.visible = True if self.show_statistics_checkbox.checked else False
    pass

  def show_dhcp_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.dhcp_grid.visible = True if self.show_dhcp_checkbox.checked else False
    pass

  def show_arp_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.arp_grid.visible = True if self.show_arp_checkbox.checked else False
    
    pass

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

