#####################################################################################################################
# Copyright(C) 2011-2025 IT4Innovations National Supercomputing Center, VSB - Technical University of Ostrava
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

import re

def str_to_var_name(text):
    """Convert a string into a valid variable name."""
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace spaces and hyphens with underscores
    text = text.replace(' ', '_').replace('-', '_')
    
    # Remove all invalid characters (keep only a-z, 0-9, _)
    text = re.sub(r'[^a-z0-9_]', '', text)
    
    # If it starts with a digit, prepend an underscore
    if text and text[0].isdigit():
        text = '_' + text
    
    # If the resulting string is empty, return a default name
    if not text:
        text = 'var'
    
    return text
