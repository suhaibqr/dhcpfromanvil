from ._anvil_designer import availabledhcpTemplate
from anvil import *
import anvil.server

class availabledhcp(availabledhcpTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # print(self.item)

    # Any code you write here will run before the form opens.
