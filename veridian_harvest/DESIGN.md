# Design System Specification: High-Performance Cultivation

## 1. Overview & Creative North Star

### Creative North Star: "The Botanical Laboratory"
This design system moves beyond basic data visualization to create an atmosphere of **Clinical Precision meets Organic Growth**. While the reference image suggests a functional dashboard, we are elevating this experience into a high-end, editorial-grade interface. The "Botanical Laboratory" aesthetic balances the rigorous data requirements of cannabis cultivation with the premium, natural essence of the product.

### Breaking the Template
To avoid a generic "SaaS" look, this system utilizes:
*   **Intentional Asymmetry:** Strategic use of negative space to guide the eye toward critical KPIs (Power, Humidity, Soil Health).
*   **Editorial Scaling:** High-contrast typography that treats data points as headlines, giving them the authority of a scientific journal.
*   **Tonal Depth:** Replacing rigid borders with sophisticated layering of green-tinted neutrals to create a sense of environmental immersion.

---

## 2. Colors & Surface Philosophy

### Color Palette
The palette is rooted in deep chlorophyll greens and earthy tertiary tones, ensuring the interface feels connected to the greenhouse floor.

*   **Primary (`#0d631b` / `primary`):** Used for critical growth status and primary actions. 
*   **Primary Container (`#2e7d32`):** The core brand anchor, used for headers and key KPI backgrounds.
*   **Secondary (`#4e635a` / `secondary`):** A soft sage for environmental data and supporting metrics.
*   **Tertiary (`#704d40` / `tertiary`):** An earthy brown used sparingly for physical substrate data (soil, roots).

### The "No-Line" Rule
**Borders are strictly prohibited for sectioning.** To separate different functional zones (e.g., Weather Trends vs. Yield Statistics), designers must use background color shifts.
*   Place `surface_container_lowest` cards on a `surface` background.
*   Use `surface_container_low` for sidebar navigation to create a natural, vertical break without a 1px line.

### Surface Hierarchy & Nesting
Treat the dashboard as a physical stack of glass and organic paper.
*   **Base:** `background` (#f8faf8)
*   **Structural Sections:** `surface_container_low`
*   **Interactive Cards:** `surface_container_lowest` (#ffffff)
*   **Floating Modals/Overlays:** Use `surface_bright` with a **Glassmorphism effect** (Backdrop blur: 12px, Opacity: 80%).

### Signature Textures
Avoid flat primary buttons. Use a subtle linear gradient from `primary` to `primary_container` (top-to-bottom) to give UI elements a slight "domed" tactile feel, reminiscent of premium lab equipment.

---

## 3. Typography

The typography strategy leverages **Manrope** for authoritative headlines and **Inter** for high-readability data density.

*   **Display (Manrope):** Large-scale growth percentages or yield totals. Use `display-lg` to make a statement about the facility's success.
*   **Headline (Manrope):** For section titles (e.g., "Atmospheric Controls"). The geometric nature of Manrope adds a "tech-forward" agricultural feel.
*   **Title (Inter):** For card headers and KPI labels. Inter’s tall x-height ensures clarity in data-dense grids.
*   **Body & Label (Inter):** Used for technical specifications and sensor metadata. 

**Editorial Tip:** Use `label-sm` with 0.05em letter-spacing for "Overline" text above headlines to create a sophisticated, curated layout.

---

## 4. Elevation & Depth

### The Layering Principle
Forget drop shadows for every card. Use **Tonal Layering**. A card using `surface_container_lowest` (#ffffff) sitting on `surface_container` (#eceeec) provides enough contrast to be perceived as "elevated" without visual clutter.

### Ambient Shadows
Where floating depth is required (e.g., a "Quick Action" FAB or a hovered sensor card), use **Ambient Shadows**:
*   **Shadow Color:** A 6% opacity tint of `on_surface` (#191c1b).
*   **Blur:** 24px - 40px for a soft, natural fall-off.
*   **Spread:** -4px to keep the shadow tucked under the element, preventing a "muddy" layout.

### The "Ghost Border" Fallback
If high-contrast backgrounds are adjacent, use a **Ghost Border**: `outline_variant` at 15% opacity. This provides a structural whisper without the "boxed-in" feel of standard dashboards.

---

## 5. Components

### KPI Blocks (The "Growth Metric")
*   **Structure:** No borders. A `surface_container_lowest` card with a `xl` (0.75rem) corner radius.
*   **Visuals:** Use circular gauges for humidity/water. The gauge "track" should be `surface_variant`, and the "progress" should be `primary`.
*   **Data Density:** Place the `label-md` unit (e.g., "PPM" or "°C") in `on_surface_variant` directly next to the value.

### Buttons & Inputs
*   **Primary Button:** `xl` (0.75rem) radius. Background: `primary`. Text: `on_primary`. 
*   **Input Fields:** Use `surface_container_low` for the field fill. No border. On focus, transition the background to `surface_container_lowest` and add a 1px "Ghost Border" of `primary`.

### Data Visualization (The "Cultivation Chart")
*   **Line Charts:** Use a 2px stroke for lines. Fill the area beneath the line with a gradient from `primary` (10% opacity) to transparent.
*   **Dots:** Only show data points on hover to maintain a clean, "High-End" aesthetic.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use `tertiary` (Earthy Brown) for alerts related to soil or substrate to provide a semantic color shift from the "atmospheric" greens.
*   **Do** prioritize whitespace. In a data-dense environment, the "luxury" is the room to breathe between metrics.
*   **Do** use `xl` (0.75rem) rounded corners for main dashboard cards to soften the technical feel.

### Don't:
*   **Don't** use pure black (#000000) for text. Use `on_surface` (#191c1b) to maintain a soft, organic contrast.
*   **Don't** use standard "Success Green." Always use the brand's `primary` (#0d631b) to ensure the interface feels bespoke to the cannabis industry.
*   **Don't** use dividers or lines to separate list items. Use a `surface_container_low` background on hover or subtle vertical spacing.