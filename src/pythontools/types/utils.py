from dataclasses import dataclass
from typing import Any


@dataclass
class GeneratorResult:
    result: Any
    done: bool

    def __getitem__(self, item):
        if item == "result":
            return self.result
        elif item == "done":
            return self.done
        else:
            raise KeyError(item)
