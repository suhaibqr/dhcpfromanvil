from ._anvil_designer import dhcpTemplateTemplate
from anvil import *
import anvil.server
from .. import DHCPForm
from .. import Handlers


class dhcpTemplate(dhcpTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # repeating_panel_dhcp.items
    # repeating_panel_dhcp.items
    id = Handlers.get_actions_id()
    print(self.item)
    if self.item["reserved"] == False:
      self.item["is_static"] = "Static" 
      btn = Button(text="Revoke")
      self.add_component(btn, column=id)
      # print(self.item)
    else: 
      btn = Button(text="Reserve")
      self.item["is_static"] = "Dynamic"
      self.add_component(btn, column=id )
      # print(self.item)

    
      
  

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    # print(self.item)
    pass
