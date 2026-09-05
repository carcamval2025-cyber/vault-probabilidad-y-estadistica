---
semana: 2
estado: material generado
fuentes:
  - Media, mediana y moda - Semana 2.pdf
  - Guía S2 - Medidas de tendencia central.pdf
  - Fórmulas_Control 1.pdf
  - Ayudantia01.R
  - Ayudantia02.R
  - EncuestaCentroComercial_2025.csv
---

# Semana 02 — Medidas de tendencia central y ayudantía en R

Fechas de la semana: 31 ago–4 sep (ver [[00 Curso/Calendario de presentaciones]]). Esta semana incorpora la presentación de clase `Media, mediana y moda - Semana 2.pdf` ("Estudiando distribuciones") y la ayudantía práctica en R.

## Alcance confirmado (presentación de clase)

1. **Medidas de tendencia central en general**: resumen en un solo valor de un conjunto de datos; media, mediana y moda. P. 3.
2. **Media aritmética**: notación poblacional (μ) y muestral (x̄); fórmulas para datos simples, datos ponderados y datos agrupados (con el punto medio de clase como dato representativo). Propiedades: suma de desviaciones respecto a la media = 0; media de una constante = la constante; media de k·xi = k·x̄; media de xi±k = x̄±k. Pp. 5, 11.
3. **Mediana**: valor que ocupa la posición central de un conjunto ordenado. Fórmulas para N impar y N par en datos simples; fórmula con límite inferior de clase, ancho de clase y frecuencia acumulada anterior para datos agrupados. Pp. 14, 15, 19.
4. **Moda**: dato de mayor frecuencia; en datos no agrupados se obtiene por inspección directa; fórmula con límite inferior, frecuencia de la clase modal y de las clases adyacentes para datos agrupados. Pp. 22, 24.
5. **Ejercicios de clase** (sin solución impresa en el PDF): media/mediana/moda de un listado simple (número de libros leídos por 20 personas); media ponderada de tres secciones de un curso; media, mediana y moda de datos agrupados (edad de beneficiarios de un programa municipal; peso de bachilleres); casos de recomposición de grupos (jubilación y nuevas contrataciones, fusión de secciones, empleados que cambian de departamento); efecto de curvas (sumar puntos, incrementar porcentualmente, descartar outliers) sobre media, mediana y moda. Pp. 6-10, 12, 16-18, 20, 23, 25-26.

Nota de edición: la portada de esta presentación rotula "Ciclo II 2026 – Semana 2"; se registra como discrepancia de edición y no como dato de calendario (el Programa confirma Ciclo III/2026), igual que el caso ya documentado en Semana 01.

## Alcance confirmado (ayudantía en R)

1. Carga de datos con `read_csv()` (tidyverse) y exploración inicial: `dim()`, `nrow()`, `ncol()`, `names()`, `head()`, `str()`, `sapply(..., class)`.
2. Tabla de frecuencias de una variable categórica (`PupusasFav`) y gráfico circular (pie chart), primero con R base y luego con `ggplot2` (con etiquetas de frecuencia y luego de porcentaje).
3. Tabla de frecuencias de otra variable categórica (`Pasatiempo`) y gráfico de barras con `ggplot2` (etiquetas, colores personalizados, `theme_minimal()`).
4. Histograma de una variable cuantitativa (`Edad`), variando el ancho de clase (`binwidth`) y el número de clases (`bins`).

Fuente: instrucción del usuario, 2026-09-03 (contenido pegado directamente en la conversación, sin PDF de respaldo). Los gráficos generados (`grafico_01_pupusas_pro.png`, `grafico_02_pasatiempos_pro.png`, `grafico_03_edad_pro.png`) están guardados en `Semana 2/`.

## Guía de repaso y fórmulas para el Control 1

- `Guía S2 - Medidas de tendencia central.pdf`: 10 ejercicios de repaso (datos simples, datos agrupados, medias ponderadas/recompuestas, medianas con datos añadidos, efecto de curvas sobre media/mediana/moda). Sin soluciones impresas.
- `Fórmulas_Control 1.pdf`: hoja de fórmulas de media, mediana y moda, idéntica a las de la presentación de clase.
- El Programa (p. 4) indica que el Control 1 (semana 3, 10%) evalúa el contenido de semanas 1 y 2.
- Uso confirmado por el usuario (2026-09-05): la guía de repaso se resuelve solo para su estudio personal, no se entrega a nadie. El curso prohíbe el uso de IA en tareas y controles (Programa, políticas de IA); esto es material de apoyo para repasar, no una evaluación a entregar.

## Entregables

- [[Entregables/Semana 02/Guía de estudio - Semana 02.html|Guía de estudio - Semana 02]] — teoría de media, mediana y moda (datos simples y agrupados), 5 diagramas SVG pedagógicos interactivos (Balanza de momentos Σ(xi-x̄)=0, Tríptico de Asimetría y Sesgo, Posición Central de la Mediana y Robustez, Ojiva del Examen ESEN e Histograma Vectorial de Libros Leídos), ejemplos, práctica y control autocorregible, más la guía de repaso del Control 1 resuelta paso a paso.
- `docs/semana-02/index.html` — versión publicada en la web del curso con paridad total.
- `Ayudantia01.R` — script inicial (solo carga de datos). Ubicación: carpeta padre del vault.
- `Ayudantia02.R` — script completo de la ayudantía (preguntas 1–4). Ubicación: carpeta padre del vault.

## Fuentes

- [[03 Fuentes/Inventario de fuentes iniciales#Media, mediana y moda - Semana 2.pdf]]
- [[03 Fuentes/Inventario de fuentes iniciales#Guía S2 - Medidas de tendencia central.pdf]]
- [[03 Fuentes/Inventario de fuentes iniciales#Fórmulas_Control 1.pdf]]
- [[03 Fuentes/Inventario de fuentes iniciales#Ayudantia01.R]]
- [[03 Fuentes/Inventario de fuentes iniciales#Ayudantia02.R]]
- [[03 Fuentes/Inventario de fuentes iniciales#EncuestaCentroComercial_2025.csv]]
