"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self,):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='e_Acum',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum=0
        
    def work(self, input_items, output_items):
        x=input_items[0]
        y= output_items[0]


        y[:]=self.acum+np.cumsum(x)
        self.acum=y[-1]
        return len(y)
