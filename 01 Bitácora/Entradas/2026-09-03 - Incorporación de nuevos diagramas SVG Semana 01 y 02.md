---
fecha: 2026-09-03
tipo: mejora de material
semana: 1, 2
estado: completado
---

# 2026-09-03 — Incorporación de nuevos diagramas SVG Semana 01 y 02

## Solicitud

El usuario solicitó añadir todos los diagramas SVG pedagógicos propuestos para completar la cobertura visual de los contenidos oficiales de clase.

## Hecho

- **Semana 01 (Guía interactiva y entregable):**
  - Se agregó el diagrama de **Fuentes de Recolección de Datos** (Censo, Encuesta, Experimento y Cuasi-experimento) según pp. 16–17 de la presentación.
  - Se incorporó la **Escalera de las 4 Escalas de Medición de Stevens** (Nominal, Ordinal, Intervalo, Razón) con operaciones estadísticas permitidas y ejemplos según pp. 13–15.
  - Se añadió la **Matriz de Estructura Temporal** (Corte transversal, Serie de tiempo, Panel) según p. 18.
  - Se incorporó el diagrama de **Tallo y Hojas (*Stem-and-Leaf*)**, demostrando su propiedad dual de conservar los valores numéricos individuales a la vez que reproduce el histograma de frecuencias sin pérdida de información según pp. 44–45.
  - Se añadieron estilos CSS para micro-interacciones hover fluidas (`.svg-interactive .svg-group`) con elevación y sombras dinámicas.
- **Semana 02 (Índice del curso):**
  - Se amplió la sección de la Semana 02 con tarjetas para los tres ejercicios de la ayudantía (Pupusas, Pasatiempos, Edad).
  - Se incorporó el diagrama SVG de la **Pirámide de Capas de `ggplot2`** (*Grammar of Graphics*), conectando la base de datos `read_csv()` con `aes()`, `geom_*()`, `scale_*()` y `theme()`.
- Se verificó la paridad total entre `docs/semana-01/index.html` y `Entregables/Semana 01/Guía de estudio - Semana 01.html`.

## Verificación

- `verificar_guia.py` ejecutado exitosamente sin discrepancias.
- Todas las estructuras SVG validadas como XML estricto.
