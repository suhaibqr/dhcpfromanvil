from ._anvil_designer import dhcpTemplateTemplate
from anvil import *
import anvil.server
from .. import Handlers



class dhcpTemplate(dhcpTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    id = Handlers.get_actions_id()
    print(self.item)
    if self.item["reserved"] == True:
      self.item["is_static"] = "Static" 
      btn = Button(text="Remove Static")
      btn.tag = [self.item["ip"]]
      btn.add_event_handler('click', get_open_form().remove_static_btn_click)
      self.add_component(btn, column=id)
    else:
      self.item["is_static"] = "Dynamic" 
      btn = Button(text="Make Static")
      btn.add_event_handler('click', get_open_form().make_it_static_btn_click)
      btn.tag = [self.item["ip"],self.item["mac"]]
      self.item["is_static"] = "Dynamic"
      self.add_component(btn, column=id )
      
      btn2 = Button(text="Revoke Lease")
      btn2.add_event_handler('click', get_open_form().revoke_lease_btn_click)
      btn2.tag =[self.item["ip"]]
      self.add_component(btn2, column=id )
    
    
      
  

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    # print(self.item)
    pass
