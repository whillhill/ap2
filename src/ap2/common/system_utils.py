"""Helper functions related to the system."""

DEBUG_MODE_INSTRUCTIONS = """
    This is really important! If the agent or user asks you to be verbose or if debug_mode is True, do the following:
      1. If this is the the start of a new task, explain who you are, what you are going to do, what tools you use, and what agents you delegate to.
      2. During the task, provide regular status updates on what you are doing, what you have done so far, and what you plan to do next.
      3. If you are delegating to another agent, ask the agent or tool to also be verbose.
      4. If at any point in the task you send or receive data, show the data in a clear, formatted way. Do not summarize it in english. Simple format the JSON objects.
      5. Step 4 is so important that I'm going to repeat it:
        a. If at any point in the task you create, send or receive data, show the data in a clear, formatted way. Do not summarize it in english. Simple format the JSON objects.
"""


