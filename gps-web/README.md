# GPS — Girls Problems Solutions

Sitio público estático + CMS visual gratuito. Incluye 6 universos, buscador real, 47 temas (3 guías de ejemplo publicadas y 44 borradores), páginas individuales, diseño responsive, SEO básico y sección Sobre nosotras.

**Importante:** las 3 guías publicadas se crearon como ejemplos editoriales para poner en funcionamiento el sitio. Revisen y aprueben los textos y sus fuentes antes de presentarlos como material definitivo. Los restantes 44 contenidos están cargados como borradores y NO se muestran como guías completas al público.

## Publicar sin instalar programas

### PASO 1 — GitHub
1. Entrá en https://github.com y creá una cuenta gratis (o ingresá a la tuya). Juli necesitará otra cuenta para editar.
2. Arriba a la derecha, clic en **+** → **New repository**.
3. Nombre: `girls-problems-solutions`. Elegí **Public** (o Private si tu plan y la configuración de hosting lo permiten). **No** actives "Add a README file". Clic en **Create repository**.
4. En la pantalla del repositorio vacío, clic en **uploading an existing file**.
5. Descomprimí el ZIP. Abrí la carpeta `gps-web` y arrastrá **todo su contenido** al recuadro de subida, incluidas las carpetas `content`, `scripts`, `public` y el archivo oculto `.pages.yml`. En Mac, `Command + Shift + .` muestra archivos ocultos. No hace falta subir `dist`, `node_modules` ni `.git` (si aparecen).
6. Esperá que terminen de subirse todos los archivos; abajo hacé clic en **Commit changes**. Verificá en el listado del repositorio que veas `.pages.yml`, `package.json`, `scripts`, `content` y `public` en la raíz. Si faltan archivos, repetí Upload files.

### PASO 2 — Cloudflare Pages
1. Ingresá en https://dash.cloudflare.com/ y creá una cuenta gratuita si todavía no tenés.
2. Desde el panel abrí **Workers & Pages** y elegí **Create application** → **Pages** → **Connect to Git** (los nombres pueden variar levemente según el panel).
3. Autorizá Cloudflare para acceder al repositorio en GitHub y elegí `girls-problems-solutions`.
4. Branch: `main`. Framework preset: **None**.
5. Build command: `npm run build`.
6. Build output directory: `dist`.
7. Root directory: dejar vacío / raíz del repositorio.
8. Clic en **Save and Deploy** o **Deploy**. Completado el build, Cloudflare mostrará una URL pública como `https://girls-problems-solutions.pages.dev` (el subdominio concreto lo asigna Cloudflare y podría ser otro).
9. Abrí la URL en una ventana privada y probá Home, Universos, Buscar, una guía y los enlaces de navegación.

**No uses “Direct Upload” como configuración definitiva:** permitiría mostrar la web, pero no actualizar automáticamente los cambios desde Pages CMS. La conexión Git es esencial.

### PASO 3 — Editor de contenido Pages CMS
1. Abrí https://app.pagescms.org e ingresá con tu cuenta de GitHub.
2. Autorizá la app de Pages CMS en GitHub. Si te solicita instalarla, seleccioná tu cuenta y autorizala **solo para el repositorio `girls-problems-solutions`**.
3. Seleccioná el repositorio. Pages CMS leerá `.pages.yml` automáticamente.
4. Entrá en **Guías y problemas**. Vas a ver 47 entradas, cada una con su título, universo, estado y selector de destacado.
5. Para editar un artículo, hacé clic en él; modificá el título, copete, cuerpo de texto, imagen, etc. Guardá los cambios.
6. Para crear una guía, elegí **New** en Guías y problemas, ingresá un título, universo y contenido. Elegí `draft` para guardar un borrador o `published` para publicarlo. La URL surge automáticamente del nombre del archivo que crea el CMS.
7. Para destacar una guía en portada, marcá **Destacar en portada**, guardá y asegurate de que el estado sea `published`.
8. Al guardar, el CMS modifica el repositorio GitHub; Cloudflare detecta el cambio, construye y publica una versión nueva. **No** tenés que volver a subir el ZIP.
9. Para despublicar, cambiá el estado a `draft` y guardá. La siguiente publicación quitará el contenido y su URL dejará de estar disponible.

Nota: el CMS NO está embebido dentro de `tusitio.pages.dev/admin`: se administra por `app.pagescms.org`. El sitio público nunca pide inicio de sesión.

### PASO 4 — Invitar a Juli
1. Desde el repositorio en GitHub: **Settings** → **Collaborators and teams** o **Collaborators** → **Add people**.
2. Buscá el nombre de usuario de GitHub de Juli, enviale la invitación y pedile que la acepte.
3. La administradora del CMS debe habilitar el acceso de la cuenta a Pages CMS siguiendo el flujo de autorización/colaboradores que presente el producto. Juli entra en `app.pagescms.org` con su propia cuenta, sin compartir contraseñas.
4. Cada una puede editar contenidos. Eviten editar el **mismo artículo simultáneamente**; los cambios se guardan en GitHub.

### PASO 5 — Personalizar
- En Pages CMS > **Textos generales**, cargá las URLs reales de Instagram y TikTok y el email público. Los íconos/enlaces sociales no se muestran hasta que haya URLs reales, para evitar links ficticios.
- Los títulos de categorías y la estética se editan en código; los problemas, guías, imágenes y textos generales indicados en el CMS se editan visualmente.
- Imágenes: subilas desde el editor, que las guarda en `public/media` y publica en `/media/...`. Usá imágenes originales o con licencia adecuada.
- Video: pegá una URL real de video de YouTube. Los videos se muestran en modo privacidad mejorada. Otros proveedores de video se pueden vincular en el texto.
- Descargables: cargá una URL HTTPS pública en el campo de descarga. También podés subir un PDF al repositorio o al administrador de medios y enlazar su ruta pública.

## Vista previa en tu Mac (opcional)
No necesitás instalar nada para publicar; GitHub + Cloudflare realizan la compilación. Para previsualizar localmente:
1. Instalá Node.js LTS de https://nodejs.org/.
2. Abrí **Terminal** (Aplicaciones > Utilidades > Terminal).
3. Escribí `cd ` (con un espacio al final), arrastrá la carpeta `gps-web` a Terminal y presioná Enter.
4. Ejecutá `npm run build` y luego `npm run preview`.
5. Abrí `http://localhost:4173` en tu navegador.
6. Para cerrar, presioná `Control + C` en Terminal.

## Estructura
- `content/problems/*.md`: una guía o tema por archivo, con metadatos.
- `content/site.json`: enlaces y presentación general.
- `.pages.yml`: definición de campos del CMS.
- `scripts/build.mjs`: generador de páginas estáticas. No requiere dependencias externas.
- `scripts/preview.mjs`: servidor local opcional.
- `public/assets/style.css`: identidad visual y responsive.
- `public/assets/app.js`: buscador, menú y compartir.
- `public/media`: imágenes y documentos aportados desde el CMS.
- `dist`: carpeta generada por la compilación; no requiere editarse manualmente.

## Actualizaciones, seguridad y costos
- Guardá todo en GitHub: eso conserva el historial de versiones. En la pestaña **Commits** podés revisar cambios previos.
- No alteres manualmente la URL de un artículo ya compartido cambiando el nombre de su archivo; generarías una URL nueva.
- Cloudflare Pages tiene plan gratuito con límites (a octubre de 2026: 500 builds/mes, 20.000 archivos por sitio, 25 MiB máximo por archivo). Revisá las condiciones vigentes antes de superar el plan: https://developers.cloudflare.com/pages/platform/limits/.
- Pages CMS anuncia uso gratuito: https://pagescms.org/. GitHub tiene un plan gratuito y el repositorio puede ser público.
- El sitio no utiliza cookies analíticas ni registra visitas por su cuenta. Si activás Cloudflare Web Analytics, verificá su política y configuración de privacidad.
- Un dominio propio es opcional y generalmente requiere pagar el registro anual. Configuralo desde el proyecto Cloudflare Pages → **Custom domains** siguiendo las instrucciones DNS que aparezcan.
- Los cambios no son instantáneos: aparecen en la web cuando finaliza la compilación automática.

## Alcances y decisiones de diseño
- Se reconstruyeron títulos y lista de problemas de la home de la web original en Wix, pero no se descargaron imágenes originales ni se pudieron confirmar fuentes y códigos de color exactos. Los dibujos de portada son originales hechos con CSS.
- No se reproducen los placeholders externos de Wix (dirección ficticia, copyright de una plantilla ni redes que no estén verificadas).
- Los borradores figuran en cada universo como temas futuros, **sin enlaces a guías inexistentes**.
- Buscador: búsqueda por palabras, tildes insensibles y filtro por categoría sobre guías *publicadas*.
- Funcionalidad de compartir: API nativa cuando existe y copia al portapapeles en contexto seguro (HTTPS).
- No hay login, pagos, formularios de datos personales ni backend en la web pública.
