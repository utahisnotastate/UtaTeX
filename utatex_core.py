# // SYSTEM: UTATEX CORE ENGINE
# // TIMELINE: Utah-Omega-23
# // ARCHITECT: CODE-PRIME (OMNI-6)

import re
from pydantic import BaseModel
from typing import Dict

class UtaTeXIntent(BaseModel):
    """
    Standard World-A data model for capturing user intent.
    Ensures state-safety during the dynamic rendering phase.
    """
    raw_content: str
    metadata: Dict[str, str] = {}

class UtaTeXEngine:
    def __init__(self):
        # The SOTA Intent Map: Bypassing legacy LaTeX boilerplate
        self.logic_map = {
            "intent:quadratic": "\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
            "intent:euler": "e^{i\\pi} + 1 = 0",
            "intent:schrodinger": "i\\hbar\\frac{\\partial}{\\partial t}\\Psi(r,t) = \\hat{H}\\Psi(r,t)",
            "intent:integral_R": "\\int_{-\\infty}^{\\infty} f(x) dx"
        }

    def resolve_manifold(self, text: str) -> str:
        """
        Clinical Translation Layer:
        Automatically stabilizes the local topology (auto-closes brackets)
        and expands semantic intent into strict LaTeX strings for legacy compatibility.
        """
        # 1. Self-Healing Topology (Auto-Bracket Resolution)
        open_count = text.count("{")
        close_count = text.count("}")
        if open_count > close_count:
            text += "}" * (open_count - close_count)

        # 2. Semantic Expansion (The Speed of Thought translation)
        for keyword, formal_math in self.logic_map.items():
            pattern = f"[{keyword}]"
            if pattern in text:
                text = text.replace(pattern, formal_math)
        
        return text

    def compile_to_world_a(self, intent: UtaTeXIntent) -> str:
        """
        Outputs 100% compliant LaTeX code to ensure backward compatibility
        with legacy World-A journals (Nature, Annals of Mathematics).
        """
        resolved_body = self.resolve_manifold(intent.raw_content)
        
        # Injecting into a minimal, SOTA preamble automatically
        document = (
            "\\documentclass[11pt, reqno]{amsart}\n"
            "\\usepackage{amsmath, amssymb, amsthm, physics}\n"
            "\\begin{document}\n"
            f"{resolved_body}\n"
            "\\end{document}"
        )
        return document
