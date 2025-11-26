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

import bpy
import subprocess
import importlib
import sys
import os

ADDON_NAME = 'braas_hpc_pynari_composer'
from collections import namedtuple

####################Dependency##############################

Dependency = namedtuple("Dependency", ["module", "package", "name"])
python_dependencies = (Dependency(module="pyanari", package="anari", name=None),
                       )

internal_dependencies = []

def import_module(module_name, global_name=None, reload=True):
    if global_name is None:
        global_name = module_name

    if global_name in globals():
        importlib.reload(globals()[global_name])
    else:
        globals()[global_name] = importlib.import_module(module_name)


def install_pip():
    try:
        if bpy.app.version < (2, 90, 0):
            python_exe = bpy.app.binary_path_python
        else:
            python_exe = sys.executable

        subprocess.run([python_exe, "-m", "pip", "--version"], check=True)

        # Upgrade
        subprocess.run([python_exe, "-m", "pip", "install",
                       "--upgrade", "pip"], check=True)

    except subprocess.CalledProcessError:
        import ensurepip

        ensurepip.bootstrap()
        os.environ.pop("PIP_REQ_TRACKER", None)


def install_and_import_module(module_name, package_name=None, global_name=None):
    if package_name is None:
        package_name = module_name

    if global_name is None:
        global_name = module_name

    environ_copy = dict(os.environ)
    environ_copy["PYTHONNOUSERSITE"] = "1"

    if bpy.app.version < (2, 90, 0):
        python_exe = bpy.app.binary_path_python
    else:
        python_exe = sys.executable

    subprocess.run([python_exe, "-m", "pip", "install",
                   package_name], check=True, env=environ_copy)

    import_module(module_name, global_name)

########################PYNARI_COMPOSER_OT##########################################

class PYNARI_COMPOSER_OT_install_dependencies(bpy.types.Operator):
    bl_idname = 'braas_hpc_pynari_composer.install_dependencies'
    bl_label = 'Install dependencies'

    def execute(self, context):
        try:
            install_pip()
            for dependency in python_dependencies:
                install_and_import_module(module_name=dependency.module,
                                          package_name=dependency.package,
                                          global_name=dependency.name)

        except (subprocess.CalledProcessError, ImportError) as err:
            self.report({"ERROR"}, str(err))
            return {"CANCELLED"}

        preferences().dependencies_installed = True

        self.report({'INFO'}, "'%s' finished" % (self.bl_label))
        return {"FINISHED"}


class PYNARI_COMPOSER_OT_update_dependencies(bpy.types.Operator):
    bl_idname = 'braas_hpc_pynari_composer.update_dependencies'
    bl_label = 'Update dependencies'

    def execute(self, context):
        try:
            install_pip()
            for dependency in python_dependencies:
                install_and_import_module(module_name=dependency.module,
                                          package_name=dependency.package,
                                          global_name=dependency.name)

        except (subprocess.CalledProcessError, ImportError) as err:
            self.report({"ERROR"}, str(err))
            return {"CANCELLED"}

        preferences().dependencies_installed = True

        self.report({'INFO'}, "'%s' finished" % (self.bl_label))
        return {"FINISHED"}


#######################PYNARIComposerPreferences#########################################

class PYNARIComposerPreferences(bpy.types.AddonPreferences):
    bl_idname = ADDON_NAME

    # dependencies_installed: bpy.props.BoolProperty(
    #     default=False
    # ) # type: ignore

    braas_hpc_pynari_composer_remote: bpy.props.BoolProperty(
        name="Enable Remote Access",
        description="Enable remote file access via SSH",
        default=False
    )  # type: ignore

    # ssh_server_name: bpy.props.StringProperty(
    #     name="SSH Server",
    #     description="SSH server name or address (e.g., user@hostname)",
    #     default=""
    # )  # type: ignore

    def draw(self, context):
        layout = self.layout

        # boxD = layout.box()
        # boxD.label(text='Dependencies:')

        # dependencies_installed = preferences().dependencies_installed

        # if not dependencies_installed:
        #     try:
        #         # for dependency in python_dependencies:
        #         #     importlib.import_module(dependency.module)
        #         import pynari

        #         preferences().dependencies_installed = True
        #     except ImportError:
        #         print("Dependency package pynari is not installed!")
        #         dependencies_installed = False

        # if not dependencies_installed:
        #     boxD.label(text='Dependencies are not installed', icon='ERROR')

        # if not dependencies_installed:
        #     boxD.operator(PYNARI_COMPOSER_OT_install_dependencies.bl_idname,
        #                   icon="CONSOLE")
        # else:
        #     boxD.operator(PYNARI_COMPOSER_OT_update_dependencies.bl_idname,
        #                   icon="CONSOLE")

        #Remote access settings
        boxR = layout.box()
        boxR.label(text='Remote Access (Required BRaaS-HPC addon):')
        boxR.prop(self, "braas_hpc_pynari_composer_remote")
        if self.braas_hpc_pynari_composer_remote:
            boxR.prop(self, "ssh_server_name")


def ctx_preferences():
    try:
        return bpy.context.preferences
    except AttributeError:
        return bpy.context.user_preferences

def preferences() -> PYNARIComposerPreferences:
    return ctx_preferences().addons[ADDON_NAME].preferences

def register():
    bpy.utils.register_class(PYNARIComposerPreferences)
    bpy.utils.register_class(PYNARI_COMPOSER_OT_install_dependencies)
    bpy.utils.register_class(PYNARI_COMPOSER_OT_update_dependencies)

def unregister():
    bpy.utils.unregister_class(PYNARIComposerPreferences)
    bpy.utils.unregister_class(PYNARI_COMPOSER_OT_install_dependencies)
    bpy.utils.unregister_class(PYNARI_COMPOSER_OT_update_dependencies)
