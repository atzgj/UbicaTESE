# 🗺️ UbicaTESE – Mapa Interactivo del Campus

Mapa interactivo del campus del **Tecnológico de Estudios Superiores de Ecatepec (TESE)**, orientado a que principalemte los alumnos de nuevo ingreso se familiaricen con las instalaciones.

---

## 📌 Descripción

UbicaTESE es una aplicación web que permite explorar visualmente el campus del TESE. Al hacer clic en cualquier edificio del mapa, se despliega una tarjeta con información del lugar y una fotografía del mismo.

El proyecto corre completamente en el navegador: no requiere servidor, base de datos ni instalación.

---

## ✨ Funcionalidades

- 🖱️ **Clic en edificios** → muestra nombre, descripción e imagen del lugar
- 📱 **Diseño responsivo** → funciona en celular y en escritorio
- ⌨️ **Tecla Escape / botón ×** → cierra la tarjeta de información
- 🛠️ **Modo trazado** (para desarrolladores) → agrega `?trazar` a la URL para obtener las coordenadas SVG de nuevos edificios

---

## 🗂️ Estructura del proyecto

```
UbicaTESE/
├── index.html      # Aplicación principal (mapa + lógica + estilos)
├── campus.png      # Imagen aérea del campus (fondo del mapa)
├── img/            # Fotografías de cada edificio
│   ├── hangar.jpg
│   └── ...
└── README.md       # Este archivo
```

---

## 🚀 Cómo usarlo

1. Escanea el código QR para apreciar la página (en proceso)

> No se necesita instalar nada.

---

## 🛠️ Modo desarrollador (trazado de edificios)

Para agregar un nuevo edificio al mapa:

1. Abre el archivo con `?trazar` al final de la URL:
   ```
   index.html?trazar
   ```
2. Haz clic en cada esquina del edificio sobre el mapa
3. Copia el texto generado en el campo de texto
4. Pégalo en el array `edificios` dentro del `<script>` de `index.html`

---

## 📋 Estado del proyecto

| Tarea | Estado |
|---|---|
| Estructura base del mapa SVG | ✅ Completo |
| Tarjeta de información interactiva | ✅ Completo |
| Diseño responsivo (móvil) | ✅ Completo |
| Herramienta de trazado | ✅ Completo |
| QR para escanear y visualizar el mapa | 🔄 En progreso |
| Coordenadas de todos los edificios | 🔄 En progreso |
| Fotografías de edificios | ⏳ Pendiente |
| Imagen del edificio en la tarjeta | ⏳ Pendiente |

---

## 🧰 Tecnologías

- HTML5
- CSS3
- JavaScript (vanilla, sin frameworks)
- SVG

---

## 👤 Autor

Desarrollado por **Godínez Atzimba** como proyecto individual.  
Ingeniería en Sistemas Computacionales — TESE

---

## 📄 Licencia

Este proyecto es de uso académico e institucional.