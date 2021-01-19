from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def submit_button_click(self, **event_args):
    # Display a popup that says 'You clicked the button'
    # alert("You clicked the button")
    # Set 'name' to the text in the 'name_box'
    name = self.name_box.text
    # Set 'email' to the text in the 'email_box'
    email = self.email_box.text
    # Set 'feedback' to the text in the 'feedback_box'
    feedback = self.feedback_box.text
    # Call your 'add_feedback' server function
    # pass in name, email and feedback as arguments
    anvil.server.call('add_feedback', name, email, feedback)
    Notification("Feedback submitted!").show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""
    