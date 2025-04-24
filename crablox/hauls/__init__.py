from typing import List, Any, Callable, Protocol

from . import h_bls_esr, h_ism_mfg, h_ism_srv, h_bld_permits, h_cmc_btc, h_gdp, h_um_ics


class Haul(Protocol):
    id: str
    path: str
    title: str
    caption: str
    summary: str
    content: Callable[[], Any]
    details: Callable[[], Any]
    history: Callable[[], Any]


blocks: List[Haul] = [  # type: ignore
    h_ism_mfg,
    h_ism_srv,
    h_um_ics,
    h_bld_permits,
    h_bls_esr,
    h_gdp,
    h_cmc_btc,
]
