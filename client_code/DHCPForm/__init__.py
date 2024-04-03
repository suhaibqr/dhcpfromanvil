from ._anvil_designer import DHCPFormTemplate
from anvil import *
import anvil.server
from .. import Handlers
from datetime import datetime


# data keys will contain a button "reserve, revoke"
# available IPs table, will contain a button "static"

class DHCPForm(DHCPFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def update_data_btn_click(self, **event_args):
    with Notification("Please Wait While Updating"):
      self.clear_all_selection()
      aa = self.dhcp_grid.columns[-1]["id"]
      Handlers.save_actions_id(aa)
      r = anvil.server.call('get_available_ips')
      self.repeating_panel_statistics.items = r
      self.interface_drop_menu.items = [x["interface"] for x in r]
      self.interface_drop_menu.selected_value = None
      self.dt = datetime.now()
      self.last_update.content = f"Last Update was at: {self.dt} UTC"
      self.last_update.visible = True
      # if self.show_statistics_checkbox.checked
      self.statistics_grid.visible = True
      self.export_date = self.dt.strftime("%Y-%m-%d-%Hh-%Mm-%Ss")
    Notification("Update Was Successful")
    
    # print(self.repeating_panel_statistics.items)
    
    """This method is called when the button is clicked"""


  def check_ip_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    s = anvil.server.call('u_check_ip_availability', self.ip_address_input_box.text)
    alert(s,large= True)

  def interface_drop_menu_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.interface_drop_menu.selected_value == None: return
    self.clear_all_selection()
    # print(self.interface_drop_menu.selected_value)
    dhcp = anvil.server.call('anvil_grid_dhcp_details', self.interface_drop_menu.selected_value)
    arp =  anvil.server.call('anvil_grid_arp', self.interface_drop_menu.selected_value)
    self.repeating_panel_dhcp.items = dhcp
    self.repeating_panel_arp.items = arp
    self.available_from_dhcp, self.available_from_subnet = anvil.server.call('u_get_available_ips', self.interface_drop_menu.selected_value)
    
    
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

  def available_from_dhcp_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    d = self.available_from_dhcp_grid.columns[0]
    self.available_from_dhcp_grid.columns = [d]
    self.available_from_dhcp_grid.columns = self.available_from_dhcp_grid.columns 
    # print(self.available_from_dhcp_grid.columns[0])
    self.available_from_dhcp_repeating_panel.items = self.available_from_dhcp
    self.available_from_dhcp_grid.visible = True if self.available_from_dhcp_checkbox.checked else False
    pass

  def available_outside_dhcp_checkbox_change(self, **event_args):
    s = self.available_from_subnet_grid.columns[0]
    self.available_from_subnet_grid.columns = [s]
    self.available_from_subnet_grid.columns = self.available_from_subnet_grid.columns
    print(self.available_from_subnet_grid.columns[0])
    self.available_from_subnet_repeating_panel.items = self.available_from_subnet
    self.available_from_subnet_grid.visible = True if self.available_outside_dhcp_checkbox.checked else False
    """This method is called when this checkbox is checked or unchecked"""
    pass


  def clear_all_selection(self):
    self.available_from_dhcp_checkbox.checked = False
    self.available_outside_dhcp_checkbox.checked = False
    self.show_arp_checkbox.checked = False
    self.show_dhcp_checkbox.checked = False
    # self.show_statistics_checkbox.checked = True
    self.dhcp_grid.visible = False 
    self.arp_grid.visible = False
    # self.statistics_grid.visible = False
    self.available_from_dhcp_grid.visible = False
    self.available_from_subnet_grid.visible = False

  def export_arp_table_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.repeating_panel_arp.items != None and len(self.repeating_panel_arp.items) >= 1:
      t = self.export_date
      Handlers.download_as_csv(self.repeating_panel_arp.items, f'arp_table_{t}.csv')
    else:
      Notification('Can not export, No Data Available, Try to Update or Select Interface').show()
    pass

  def export_summary_table_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.repeating_panel_statistics.items != None and len(self.repeating_panel_statistics.items) >= 1:
      t = self.export_date
      Handlers.download_as_csv(self.repeating_panel_statistics.items, f'arp_table_{t}.csv')
    else:
      Notification('Can not export, No Data Available, Try to Update or Select Interface').show()
    pass

  def export_dhcp_table_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    
    if self.repeating_panel_dhcp.items != None and len(self.repeating_panel_dhcp.items) >= 1:
      t = self.export_date
      Handlers.download_as_csv(self.repeating_panel_dhcp.items, f'arp_table_{t}.csv')
    else:
      Notification('Can not export, No Data Available, Try to Update or Select Interface').show()
    pass

  def export_unused_dhcp_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
       
    if self.repeating_panel_dhcp.items != None and len(self.repeating_panel_dhcp.items) >= 1:
      t = self.export_date
      Handlers.download_as_csv(self.repeating_panel_dhcp.items, f'arp_table_{t}.csv')
    else:
      Notification('Can not export, No Data Available, Try to Update or Select Interface').show()
    pass

  def export_unused_ips_outside_dhcp_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    if self.available_from_subnet_repeating_panel.items != None and len(self.available_from_subnet_repeating_panel.items) >= 1:
      t = self.export_date
      Handlers.download_as_csv(self.available_from_subnet_repeating_panel.items, f'arp_table_{t}.csv')
    else:
      Notification('Can not export, No Data Available, Try to Update or Select Interface').show()
    pass
    
  def revoke_lease_btn_click(self, **event_args):
    print(event_args)

  def make_it_static_btn_click(self, **event_args):
    print(event_args)

  def remove_static_btn_click(self, **event_args):
    print(event_args)
      
    


    