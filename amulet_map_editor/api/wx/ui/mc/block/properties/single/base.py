import wx

from amulet.api.block import PropertyType


class BaseSingleProperty(wx.Panel):
    """
    A UI from which a user can choose one value for each property.

    This is base class for both flavours of single property selection UIs.
    Subclasses must implement the logic.
    """

    def __init__(self, parent: wx.Window):
        super().__init__(parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    @property
    def properties(self) -> PropertyType:
        """
        A dictionary mapping string property names to the selected NBT values.
        """
        raise NotImplementedError

    @properties.setter
    def properties(self, properties: PropertyType):
        raise NotImplementedError