# chains/chain.py

from typing import List
from .baseComponent import Component


class Chain:

    def __init__(self, components: List[Component]):
        self.components = components
    def run(self, input_data):
        for component in self.components:
            input_data = component.run(input_data)
        return input_data