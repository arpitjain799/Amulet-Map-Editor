import pickle
from typing import Any, TYPE_CHECKING
import os
import wx
import weakref

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas
    from amulet.api.world import World


class OperationUI:
    """The base class that all operations must inherit from."""
    def __init__(self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str):
        self._parent = weakref.ref(parent)
        self._canvas = weakref.ref(canvas)
        self._world = weakref.ref(world)
        self._options_path = options_path

    @property
    def parent(self) -> wx.Window:
        return self._parent()

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    @property
    def world(self) -> "World":
        return self._world()

    def _load_options(self, default=None) -> Any:
        """Load previously saved options from disk or return the default options."""
        try:
            with open(self._options_path, "rb") as f:
                return pickle.load(f)
        except:
            return default

    def _save_options(self, options: Any):
        """Save the given options to disk so that they persist in the next session."""
        os.makedirs(os.path.basename(self._options_path), exist_ok=True)
        with open(self._options_path, "wb") as f:
            return pickle.dump(options, f)
