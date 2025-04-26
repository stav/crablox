from typing import List, Any, Callable
from types import ModuleType

from . import (
    h_bls_esr,
    h_ism_mfg,
    h_ism_srv,
    h_bld_permits,
    h_cmc_btc,
    h_gdp,
    h_um_ics,
    h_lei_us,
)


class Haul:
    def __init__(self, module: ModuleType):
        self.id: str = getattr(module, "id", "")
        self.path: str = getattr(module, "path", "")
        self.title: str = getattr(module, "title", "")
        self.style: str = getattr(module, "style", "")
        self.caption: str = getattr(module, "caption", "")
        self.summary: str = getattr(module, "summary", "")
        self.content: Callable[[], Any] = getattr(module, "content", lambda: None)
        self.details: Callable[[], Any] = getattr(module, "details", lambda: None)
        self.history: Callable[[], Any] = getattr(module, "history", lambda: None)


blocks: List[Haul] = [
    Haul(h_ism_mfg),
    Haul(h_ism_srv),
    Haul(h_um_ics),
    Haul(h_bld_permits),
    Haul(h_bls_esr),
    Haul(h_gdp),
    Haul(h_lei_us),
    Haul(h_cmc_btc),
]
