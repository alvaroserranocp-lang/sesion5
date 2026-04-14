import os
import re

dirs = [
    {
        "id": "panel_de_control",
        "path": "panel_de_control_general/code.html",
        "nav_text": "Panel de Control"
    },
    {
        "id": "sala_de_clones",
        "path": "sala_de_clones/code.html",
        "nav_text": "Sala de Clones"
    },
    {
        "id": "sala_de_produccion",
        "path": "sala_de_producci_n/code.html",
        "nav_text": "Sala de Producción"
    },
    {
        "id": "almacen_bodega",
        "path": "sala_de_almac_n/code.html",
        "nav_text": "Almacén/Bodega"
    }
]

# Get the base HTML from the first file
base_html = open(dirs[0]["path"], "r", encoding="utf-8").read()

# Extract the header/head
head_match = re.search(r"(<head>.*?</head>)", base_html, re.DOTALL)
head = head_match.group(1) if head_match else ""

# Extract the script/style from all of them if needed... actually they all share the same tailwind config mostly.
# We will just inject some custom CSS for hiding/showing pages
custom_css = """
<style>
    .page-view { display: none; }
    .page-view.active { display: block; }
    /* active nav item styles */
    .nav-item.active {
        background-color: rgb(244 244 245 / var(--tw-bg-opacity, 1)); /* bg-zinc-100 */
        color: rgb(6 78 59 / var(--tw-text-opacity, 1)); /* text-emerald-900 */
        border-right-width: 4px;
        border-color: rgb(4 120 87 / var(--tw-border-opacity, 1)); /* border-emerald-700 */
        font-weight: 700;
    }
    .dark .nav-item.active {
        background-color: rgb(24 24 27 / var(--tw-bg-opacity, 1)); /* dark:bg-zinc-900 */
        color: rgb(52 211 153 / var(--tw-text-opacity, 1)); /* dark:text-emerald-400 */
    }
</style>
"""
head = head.replace("</head>", custom_css + "\n</head>")

# Extract the aside from base
aside_match = re.search(r"(<aside.*?</aside>)", base_html, re.DOTALL)
aside = aside_match.group(1) if aside_match else ""

# Modify aside links to have id attributes or onclick
def replace_nav(m):
    text = m.group(0)
    return text

aside = re.sub(r'<a[^>]*>.*?</a>', lambda m: m.group(0), aside, flags=re.DOTALL)

# Let's reconstruct aside from scratch since they have slight variations in classes across files, but structurally similar
aside = """
<aside class="hidden md:flex flex-col h-screen w-64 fixed left-0 top-0 bg-zinc-50 dark:bg-zinc-950 py-8 px-4 transition-all duration-200 ease-in-out z-50">
<div class="mb-10 px-2">
<h1 class="font-headline font-black text-emerald-900 dark:text-emerald-50 text-xl tracking-tight">Laboratorio Botánico</h1>
<p class="font-headline uppercase tracking-wider text-[10px] text-zinc-500 mt-1">Instalación Alpha</p>
</div>
<nav class="flex-1 space-y-2">
<a href="#panel_de_control" class="nav-item flex items-center gap-3 px-3 py-3 rounded-xl transition-all duration-200 ease-in-out text-zinc-600 dark:text-zinc-400 hover:text-emerald-700 dark:hover:text-emerald-300">
<span class="material-symbols-outlined" data-icon="dashboard">dashboard</span>
<span class="font-headline uppercase tracking-wider text-xs">Panel de Control</span>
</a>
<a href="#sala_de_clones" class="nav-item flex items-center gap-3 px-3 py-3 rounded-xl transition-all duration-200 ease-in-out text-zinc-600 dark:text-zinc-400 hover:text-emerald-700 dark:hover:text-emerald-300">
<span class="material-symbols-outlined" data-icon="potted_plant">potted_plant</span>
<span class="font-headline uppercase tracking-wider text-xs">Sala de Clones</span>
</a>
<a href="#sala_de_produccion" class="nav-item flex items-center gap-3 px-3 py-3 rounded-xl transition-all duration-200 ease-in-out text-zinc-600 dark:text-zinc-400 hover:text-emerald-700 dark:hover:text-emerald-300">
<span class="material-symbols-outlined" data-icon="agriculture">agriculture</span>
<span class="font-headline uppercase tracking-wider text-xs">Sala de Producción</span>
</a>
<a href="#almacen_bodega" class="nav-item flex items-center gap-3 px-3 py-3 rounded-xl transition-all duration-200 ease-in-out text-zinc-600 dark:text-zinc-400 hover:text-emerald-700 dark:hover:text-emerald-300">
<span class="material-symbols-outlined" data-icon="inventory_2">inventory_2</span>
<span class="font-headline uppercase tracking-wider text-xs">Almacén/Bodega</span>
</a>
</nav>
<div class="mt-auto space-y-2 pt-8 flex flex-col">
<button class="w-full text-white py-3 px-4 rounded-xl font-headline font-bold text-xs uppercase tracking-wider mb-4 active:scale-95 duration-150 transition-all shadow-md" style="background: linear-gradient(180deg, #0d631b 0%, #2e7d32 100%);">Acciones Rápidas</button>
<a class="flex items-center gap-3 px-3 py-2 text-zinc-500 hover:text-emerald-600 transition-colors" href="#">
<span class="material-symbols-outlined" data-icon="help">help</span>
<span class="font-headline uppercase tracking-wider text-xs">Soporte</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-zinc-500 hover:text-emerald-600 transition-colors" href="#">
<span class="material-symbols-outlined" data-icon="history">history</span>
<span class="font-headline uppercase tracking-wider text-xs">Registros</span>
</a>
</div>
</aside>
"""

# Now build the main container
main_content = '<main class="md:ml-64 min-h-screen flex flex-col pt-0">\n'

for item in dirs:
    html = open(item["path"], "r", encoding="utf-8").read()
    # Extract inner content of main (or header, content, footer)
    main_match = re.search(r'<main[^>]*>(.*?)<\/main>', html, re.DOTALL)
    if main_match:
        inner_main = main_match.group(1)
        # wrap in div
        main_content += f'<div id="{item["id"]}" class="page-view">\n{inner_main}\n</div>\n'
    
main_content += '</main>\n'


js_script = """
<script>
    function navigateTo(id) {
        // Hide all page views
        document.querySelectorAll('.page-view').forEach(el => {
            el.classList.remove('active');
        });
        // Show target page view
        const target = document.getElementById(id);
        if (target) {
            target.classList.add('active');
        }
        
        // Update nav items
        document.querySelectorAll('.nav-item').forEach(btn => {
            btn.classList.remove('active', 'border-r-4', 'border-emerald-700', 'font-bold', 'text-emerald-900', 'dark:text-emerald-400', 'bg-zinc-100', 'dark:bg-zinc-900');
            if (btn.getAttribute('href') === '#' + id) {
                btn.classList.add('active', 'border-r-4', 'border-emerald-700', 'font-bold', 'text-emerald-900', 'dark:text-emerald-400', 'bg-zinc-100', 'dark:bg-zinc-900');
            }
        });
        
        window.scrollTo(0, 0);
    }

    // Event listener for nav links
    document.querySelectorAll('.nav-item').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const id = this.getAttribute('href').substring(1);
            window.location.hash = id;
            navigateTo(id);
        });
    });

    // Handle hash on load
    window.addEventListener('DOMContentLoaded', () => {
        let hash = window.location.hash.substring(1);
        if (!hash) {
            hash = 'panel_de_control';
            window.location.hash = hash;
        }
        navigateTo(hash);
    });
    
    window.addEventListener('hashchange', () => {
        const hash = window.location.hash.substring(1);
        if (hash) {
            navigateTo(hash);
        }
    });

</script>
"""

# Extract body attributes from base
body_match = re.search(r'<body([^>]*)>', base_html)
body_attrs = body_match.group(1) if body_match else 'class="bg-background text-on-surface"'

final_html = f"""<!DOCTYPE html>
<html class="light" lang="es">
{head}
<body {body_attrs}>
{aside}
{main_content}
{js_script}
</body>
</html>
"""

os.makedirs('app', exist_ok=True)
with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print("Built app/index.html successfully.")
