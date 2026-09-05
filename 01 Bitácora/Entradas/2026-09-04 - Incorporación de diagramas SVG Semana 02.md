---
fecha: 2026-09-04
tipo: mejora visual de material
semana: 2
estado: completado
---

# 2026-09-04 — Incorporación de diagramas SVG Semana 02

## Solicitud

El usuario solicitó, mediante el flujo de alineación `/grill-me`, rediseñar las visualizaciones existentes y agregar diagramas vectoriales SVG pedagógicos en el material de la Semana 02 (Medidas de Tendencia Central), con micro-interacciones hover CSS, replicación en `docs/semana-02/index.html` y actualización de enlaces en el índice web.

## Hecho

- **Rediseño e incorporación de 6 diagramas SVG pedagógicos:**
  1. **Balanza de la media (Propiedad $\sum(x_i - \bar{x}) = 0$):** Rediseñada con palanca graduada en distancias métricas relativas ($\Delta = 65\text{ px}$), fulcro central con indicador de equilibrio, pesas proporcionales suspendidas en coral (desviaciones negativas: $-3, -1$) y verde menta (desviaciones positivas: $+1, +3$), y tarjetas de balance que demuestran el momento nulo $(\sum = 0)$.
  2. **Tríptico de asimetría y sesgo:** Panel comparativo de las tres formas de distribución (Sesgo a la izquierda: $\bar{x} < Me < Mo$; Simétrica: $\bar{x} = Me = Mo$; Sesgo a la derecha: $Mo < Me < \bar{x}$), con curvas suaves de densidad, líneas guía punteadas para cada estadístico y explicación pedagógica de por qué la media es sensible a las colas.
  3. **Arquitectura y mecanismos de cálculo de la media (Descriptivo de Media):** Panel triple que desglosa: (1) datos simples como nivelación física donde el exceso rellena el déficit hasta igualarse en $\mu$; (2) media ponderada con las secciones A, B y C de economía mostrando que los grupos más numerosos ejercen mayor atracción gravitacional ($\mu = 8.22 \ne 8.27$ simple); y (3) datos agrupados mostrando la convergencia del intervalo de clase $[4, 8)$ hacia su punto medio geométrico $PM = 6$ como representante de masa.
  4. **Posición central de la mediana y robustez:** Inspirado en la lámina 14 de clase. Muestra un conjunto ordenado impar ($N=7$) con siluetas humanas estilizadas destacando la posición central $(N+1)/2$, y un panel de demostración de robustez ante un valor atípico extremo (la media se distorsiona mientras la mediana permanece inmutable).
  5. **Ojiva interactiva del Examen de Admisión ESEN:** Reconstrucción vectorial de la lámina 18 (curva sigmoide de frecuencias acumuladas vs. notas de 0 a 8), con cuadrícula milimétrica, marcas de referencia y tarjetas de resolución para los 4 incisos de clase ($x < 3 \to 20\%$, $x = 4 \to 50\%$ mediana, $x > 6 \to 15\%$, y entre 4 y 6 $\to 35\%$).
  6. **Histograma vectorial ampliado de libros leídos (Moda en formato grande, $980 \times 480$):** Histograma espacioso a pantalla completa con cuadrícula graduada en $fi$, barras amplias de 74 px con badges y conteos tipográficos grandes, barra modal destacada en oro ($x=0, f=6, 30\%$), líneas guía verticales de Mediana ($Me=1$) y Media ($\bar{x}=1.75$), y tarjetas inferiores de diagnóstico del sesgo positivo.
- **Estilos y micro-interacciones:** Se incorporaron estilos `.svg-interactive` y `.svg-group` con elevación, iluminación al hover y transiciones fluidas.
- **Publicación web:** Se sincronizó `docs/semana-02/index.html` garantizando paridad total con `Entregables/Semana 02/Guía de estudio - Semana 02.html` (con rutas de marca relativas adaptadas a `../assets/brand/`).
- **Enlace en índice web:** Se actualizó la tarjeta de la Semana 02 y el encabezado de su sección en `docs/index.html` para enlazar directamente a la nueva guía web interactiva.
- **Trazabilidad:** Se actualizó `02 Unidades/Semana 02 - Ayudantía práctica en R.md` con los nuevos entregables y diagramas.

## Verificación

- Validación de sintaxis XML estricta ejecutada exitosamente para todos los 5 SVGs con `xml.etree.ElementTree` (0 errores).
- Verificación de paridad `diff -u` entre la guía entregable y la versión en `docs/semana-02/index.html`: idénticas salvo la ruta relativa a la marca.
- Comprobación de que no quedaron referencias rotas a rutas inexistentes.
