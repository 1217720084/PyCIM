#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM14r05.Core import IdentifiedObject
from CIM14r05.Core import IrregularIntervalSchedule



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SwitchState = Enum("close", "open")

#------------------------------------------------------------------------------
#  "ClearanceTag" class:
#------------------------------------------------------------------------------

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conducting equipment may have multiple clearance tags for authorized field work
    ConductingEquipment = Instance("CIM14r05.Core.ConductingEquipment",
        desc="Conducting equipment may have multiple clearance tags for authorized field work",
        transient=True,
        opposite="ClearanceTags",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    ClearanceTagType = Instance("CIM14r05.Outage.ClearanceTagType",
        transient=True,
        opposite="ClearanceTags",
        editor=InstanceEditor(name="_clearancetagtypes"))

    def _get_clearancetagtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Outage.ClearanceTagType" ]
        else:
            return []

    _clearancetagtypes = Property(fget=_get_clearancetagtypes)

    # Description of the work to be performed
    workDescription = Str(desc="Description of the work to be performed")

    # Set true if equipment phasing must be checked
    phaseCheckReqFlag = Bool(desc="Set true if equipment phasing must be checked")

    # The time at which the clearance tag is scheduled to be set.
    workStartTime = Str(desc="The time at which the clearance tag is scheduled to be set.")

    # The name of the person who is authorized to issue the tag
    authorityName = Str(desc="The name of the person who is authorized to issue the tag")

    # Set true if equipment must be deenergized
    deenergizeReqFlag = Bool(desc="Set true if equipment must be deenergized")

    # Set true if equipment must be grounded
    groundReqFlag = Bool(desc="Set true if equipment must be grounded")

    # The time at which the clearance tag is scheduled to be removed
    workEndTime = Str(desc="The time at which the clearance tag is scheduled to be removed")

    # The time at which the clearance tag was issued
    tagIssueTime = Str(desc="The time at which the clearance tag was issued")

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTag" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "workDescription", "phaseCheckReqFlag", "workStartTime", "authorityName", "deenergizeReqFlag", "groundReqFlag", "workEndTime", "tagIssueTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ConductingEquipment", "ClearanceTagType",
                label="References"),
            dock="tab"),
        id="CIM14r05.Outage.ClearanceTag",
        title="ClearanceTag",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ClearanceTag" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchingOperation" class:
#------------------------------------------------------------------------------

class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An OutageSchedule may operate many switches.
    OutageSchedule = Instance("CIM14r05.Outage.OutageSchedule",
        desc="An OutageSchedule may operate many switches.",
        transient=True,
        opposite="SwitchingOperations",
        editor=InstanceEditor(name="_outageschedules"))

    def _get_outageschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Outage.OutageSchedule" ]
        else:
            return []

    _outageschedules = Property(fget=_get_outageschedules)

    # A switch may be operated by many schedules.
    Switches = List(Instance("CIM14r05.Wires.Switch"),
        desc="A switch may be operated by many schedules.")

    # The switch position that shall result from this SwitchingOperation
    newState = SwitchState(desc="The switch position that shall result from this SwitchingOperation")

    # Time of operation in same units as OutageSchedule.xAxixUnits.
    operationTime = Str(desc="Time of operation in same units as OutageSchedule.xAxixUnits.")

    #--------------------------------------------------------------------------
    #  Begin "SwitchingOperation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "newState", "operationTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OutageSchedule", "Switches",
                label="References"),
            dock="tab"),
        id="CIM14r05.Outage.SwitchingOperation",
        title="SwitchingOperation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchingOperation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ClearanceTagType" class:
#------------------------------------------------------------------------------

class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ClearanceTags = List(Instance("CIM14r05.Outage.ClearanceTag"))

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTagType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ClearanceTags",
                label="References"),
            dock="tab"),
        id="CIM14r05.Outage.ClearanceTagType",
        title="ClearanceTagType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ClearanceTagType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageSchedule" class:
#------------------------------------------------------------------------------

class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A power system resource may have an outage schedule
    PSR = Instance("CIM14r05.Core.PowerSystemResource",
        desc="A power system resource may have an outage schedule",
        transient=True,
        opposite="OutageSchedule",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # An OutageSchedule may operate many switches.
    SwitchingOperations = List(Instance("CIM14r05.Outage.SwitchingOperation"),
        desc="An OutageSchedule may operate many switches.")

    #--------------------------------------------------------------------------
    #  Begin "OutageSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "value1Multiplier", "value2Unit", "value2Multiplier", "startTime", "value1Unit",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "PSR", "SwitchingOperations",
                label="References"),
            dock="tab"),
        id="CIM14r05.Outage.OutageSchedule",
        title="OutageSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageSchedule" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
