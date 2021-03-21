import wx
from typing import Union

from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from ..canvas_toggle_element import CanvasToggleElement

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(EditCanvasContainer):
    """The abstract base class for all tools that are to be loaded into the canvas."""

    @property
    def name(self) -> str:
        """The name of the tool."""
        raise NotImplementedError

    def enable(self):
        """Set the state of the tool for being enabled."""
        pass

    def bind_events(self):
        """Bind all required events to the canvas.
        All events on the canvas will be automatically removed after the tool is disabled.
        """
        pass

    def disable(self):
        """Stop the tool. Unload any excessive data. May get resumed again with a call to enable."""
        pass
