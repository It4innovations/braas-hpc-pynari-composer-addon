#####################################################################################################################
# Copyright(C) 2025-2026 IT4Innovations National Supercomputing Center, VSB - Technical University of Ostrava
#
# This program is free software : you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#####################################################################################################################
bl_info = {
    "name": "BRaaS-HPC-PYNARIComposer",
    "author": "Milan Jaros, Petr Strakos, Lubomir Riha",
    "description": "",
    "blender": (4, 5, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Render"
}
#####################################################################################################################

def register():
    from . import pynari_pref
    from . import base_nodes
    from .bvtk_nodes import core as BVTK_Node

    pynari_pref.register()
    base_nodes.register()
    BVTK_Node.register()
    

def unregister():
    from . import pynari_pref
    from . import base_nodes
    from .bvtk_nodes import core as BVTK_Node
    
    try:        
        pynari_pref.unregister()
        base_nodes.unregister()
        BVTK_Node.unregister()

    except RuntimeError:
        pass 
