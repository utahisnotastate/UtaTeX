# // SYSTEM: UTATEX TRANSMUTER
# // FUNCTION: Legacy LaTeX Deprecation

import os
import re

def migrate_legacy_tex(filepath: str, output_path: str):
    """
    Strips bloated legacy LaTeX preambles and converts the core 
    mathematical logic into a streamlined UtaTeX Intent file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract only the mathematical intent (between begin/end document)
    body_match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    
    if body_match:
        pure_intent = body_match.group(1).strip()
        
        # Map old, verbose LaTeX commands to UtaTeX shorthand where applicable
        # (e.g., automatically detecting quadratic formulas and condensing them)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(pure_intent)
        print(f"// MIGRATION SUCCESSFUL: {filepath} -> {output_path}")
    else:
        print("// ERROR: NO VALID TOPOLOGY FOUND IN SOURCE FILE.")
