"""Comprobación mínima de la guía interactiva de la Semana 01."""
from pathlib import Path


HERE = Path(__file__).parent
SOURCE = HERE / "Guía de estudio - Semana 01.html"
PUBLISHED = HERE.parents[1] / "docs" / "semana-01" / "index.html"


def normalized(text: str) -> str:
    return text.replace("../../docs/assets/brand/ep-wordmark-light.svg", "LOGO").replace(
        "../assets/brand/ep-wordmark-light.svg", "LOGO"
    )


source = SOURCE.read_text(encoding="utf-8")
published = PUBLISHED.read_text(encoding="utf-8")
assert normalized(source) == normalized(published), "Las dos versiones de la guía difieren"
assert source.count("<fieldset>") == 8, "El control debe tener ocho preguntas"
assert "q8:['b'" in source and "0.28" in source, "Faltan respuestas verificables del control"
assert all(cell in source for cell in ("<td>5</td><td>0.333</td><td>5</td>", "<td>1</td><td>0.067</td><td>15</td>")), "Falta la tabla verificable del ejercicio integrado"
print("Guía Semana 01: estructura y publicación verificadas.")
