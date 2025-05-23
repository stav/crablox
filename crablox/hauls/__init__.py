from typing import List, Any, Callable
from types import ModuleType

from . import (
    # h_cmc_btc,
    gdp,
    ism_mfg,
    ism_srv,
    jobs_payroll,
    lei,
    sentiment,
    h_ticker,
    building_permits,
)


class Haul:
    def __init__(self, module: ModuleType):
        self.id: str = getattr(module, "id", module.__name__.replace(".", "_"))
        self.path: str = getattr(module, "path", f"/{self.id}")
        self.title: str = getattr(module, "title", self.id)
        self.short: str = getattr(module, "short", self.title[:3])
        self.style: str = getattr(module, "style", "")
        self.caption: str = getattr(module, "caption", "")
        self.summary: str = getattr(module, "summary", "")
        self.content: Callable[[], Any] = getattr(module, "content", lambda: None)
        self.details: Callable[[], Any] = getattr(module, "details", lambda: None)
        self.history: Callable[[], Any] = getattr(module, "history", lambda: None)


blocks: List[Haul] = [
    Haul(ism_mfg),
    Haul(ism_srv),
    Haul(sentiment),
    Haul(jobs_payroll),
    Haul(building_permits),
    Haul(gdp),
    Haul(lei),
    Haul(h_ticker),
    # Haul(h_cmc_btc),
]
