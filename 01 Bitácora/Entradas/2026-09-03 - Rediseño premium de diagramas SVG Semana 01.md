---
fecha: 2026-09-03
tipo: mejora de material
semana: 1
estado: completado
---

# 2026-09-03 — Rediseño premium de diagramas SVG Semana 01

## Solicitud

El usuario solicitó mejorar los diagramas vectoriales SVG de los materiales de la semana, elevando su nivel visual y calidad pedagógica.

## Hecho

- **Diagrama de flujo de investigación estadística:** Rediseñado con tarjetas en gradiente, marcadores de flecha estilizados, etiquetas explícitas de Parámetro (N) vs. Estadístico (n), badges de fase y cintillo explicativo de fila (observación) y columna (variable).
- **Árbol de clasificación de variables:** Ampliado a un árbol jerárquico completo de dos niveles con conectores Bezier suaves, separando Categórica (Nominal vs. Ordinal) y Cuantitativa (Discreta vs. Continua) con sus escalas y ejemplos de clase.
- **Gráfico de barras y circular (Caso 25 estudiantes):**
  - Barras con cuadrícula, conteos exactos y porcentajes para las 7 categorías, destacando la moda (Blanco: 7, 28%).
  - Gráfico de dona con cálculo trigonométrico exacto para los 7 sectores, leyenda integrada y conteo total $n=25$ al centro.
- **Gráficos cuantitativos agrupados (Histograma, Polígono y Ojiva):**
  - Histograma con barras continuas adyacentes y límites reales de clase.
  - Polígono de frecuencias anclado a cero en puntos medios extendidos con sombreado de área.
  - Ojiva acumulada monótona con área sombreada y valores acumulados $F = 5, 9, 12, 14, 15$.
- **Serie de tiempo y Coropleta:** Rediseñados con cuadrícula, gradientes suaves, nodos iluminados, regiones vectoriales pulidas y barra continua de escala de color.
- **Ilustración hero de `docs/index.html`:** Histograma estilizado con gradientes suaves, curva gaussiana con brillo sutil y marcador de moda/media.
- Se mantuvieron sincronizadas las dos versiones: `docs/semana-01/index.html` y `Entregables/Semana 01/Guía de estudio - Semana 01.html`.

## Verificación

- Se ejecutó el script `verificar_guia.py`, confirmando la paridad estructural, contenido evaluable y presencia de los SVG.
- Validación de sintaxis XML/SVG completada sin errores.
