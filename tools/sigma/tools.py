# Sigma library tools
# Copyright 2016-2018 Thomas Patzke

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def deep_update_dict(dest, src):
    """Update dict deeply, e.g. also update contained dicts instead of overwriting them."""
    for key, value in src.items():
        if isinstance(value, dict) and key in dest and isinstance(dest[key], dict):     # source is dict, destination key already exists and is dict: merge
                deep_update_dict(dest[key], value)
        else:
            dest[key] = value
