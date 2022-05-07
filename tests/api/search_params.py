from dataclasses import dataclass, fields


@dataclass
class SearchParams:
    q: str
    viewmode: str = "grid"
    orderby: int = 0
    pagesize: int = 18
    advs: bool = True
    cid: int = 0
    isc: bool = False
    mid: int = 0
    vid: str = ""
    sid: bool = True

    def to_str(self):
        return "&".join(f"{field.name}={getattr(self, field.name)}"
                        for field in fields(self))
