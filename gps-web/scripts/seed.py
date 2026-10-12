import os,re,unicodedata
from pathlib import Path
root=Path(__file__).resolve().parents[1]/'content/problems'
cats={
'finanzas':['Empezar a manejar mi plata','Empezar a ahorrar e invertir','Bancos y cuentas','Tarjetas de crédito','Billeteras, descuentos y pagos','Dólares y consumos internacionales','Tengo un problema como consumidora','Me estafaron'],
'laboral':['Conseguir mi primer trabajo','Preparar una entrevista','Entender mi relación laboral','Entender mi sueldo','Conocer mis derechos','Poner límites en el trabajo','Cuando algo sale mal: despido, discriminación, acoso'],
'burocratica':['Monotributo desde cero','Cómo facturar','Documentos de adulta','Perdí documentos','Renovar documentos','Comprar o vender un auto','Herencias y sucesiones','Organismos y reclamos'],
'independiente':['¿Estoy lista para mudarme?','Alquilar por primera vez','Entender mi alquiler','¿Qué necesito para mudarme?','¿Cómo funciona mi casa?','Servicios y contratos','Comprar comida para una','Comprar una propiedad'],
'saludable':['Entender mi sistema de salud','Ir al médico sola','Guardias, hospitales y emergencia','Mi salud ginecológica','Salud sexual y reproductiva','Cuidar mi salud mental','Mis controles de salud','Cuidar a otra persona'],
'social':['Mi primer relación seria','Sexo, consentimiento y límites','Vínculos tóxicos','Cuando un vínculo se termina','Familia y límites','Amigas y vínculos','Citas y apps','Volver a casa segura']}
def slug(s):
 s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
 return re.sub('(^-|-$)','',re.sub('[^a-z0-9]+','-',s))
articles={
'Conseguir mi primer trabajo':('Tu primer laburo no tiene por qué ser un misterio. Por dónde empezar, dónde buscar y cómo organizarte sin mandar 300 CV a ciegas.', '''## Primero: ¿qué estás buscando realmente?

Antes de abrir veinte pestañas, anotá tres cosas: qué tareas te gustaría hacer, cuántas horas podés trabajar y qué modalidad necesitás. No hace falta tener decidido tu futuro entero: necesitás una primera dirección.

## Armá tu kit de búsqueda

1. Prepará un CV corto, claro y adaptado al tipo de puesto.
2. Revisá que tus datos de contacto sean correctos.
3. Si el trabajo lo amerita, armá un portfolio con trabajos académicos, voluntariados o proyectos personales.
4. Tené a mano una breve presentación: quién sos, qué sabés hacer y qué buscás aprender.

> **Tip GPS:** No haber tenido empleo formal no significa que no tengas experiencia. Organizar actividades en tu facultad, manejar redes de un emprendimiento familiar o participar de proyectos también muestra habilidades. Contá exactamente qué hiciste, sin inventar cargos.

## ¿Dónde buscar?

Podés explorar [LinkedIn Empleos](https://www.linkedin.com/jobs/), [Bumeran](https://www.bumeran.com.ar/) y las páginas de carreras de las organizaciones que te interesan. Verificá siempre que la postulación sea auténtica.

## ¿Y las pasantías?

Son experiencias formativas vinculadas con tus estudios y tienen condiciones específicas. Consultá primero la bolsa de empleo o el área de pasantías de tu universidad y revisá las condiciones por escrito antes de aceptar.

## Organizate sin agotarte

Llevá una planilla con puesto, empresa, enlace, fecha de postulación y estado. Personalizá el CV según las tareas importantes de cada búsqueda y reservá un momento de la semana para hacer seguimiento.

## Preguntas frecuentes

### ¿Mando el mismo CV a todos lados?

Podés partir de una versión base, pero conviene ordenar las habilidades y experiencias relevantes para cada puesto.

### ¿Tengo que poner foto?

En general no es indispensable. Priorizá información profesional y revisá las instrucciones concretas del aviso.

### ¿Qué hago si me piden plata para conseguir el empleo?

Desconfiá de pagos anticipados o pedidos de información financiera sensible. Verificá la identidad del empleador por canales oficiales.
'''),
'Tarjetas de crédito':('Amiga, el límite no es plata gratis. Una guía para entender el resumen, las fechas y qué pasa cuando pagás menos del total.', '''## Primero lo primero: ¿qué estás usando?

Una tarjeta de crédito te permite financiar consumos que después tenés que pagar según las condiciones del banco o entidad emisora. No es un ingreso extra.

## Las cuatro cosas que tenés que ubicar

1. **Fecha de cierre:** determina qué consumos entran en ese resumen.
2. **Vencimiento:** fecha límite de pago indicada en el resumen.
3. **Pago total:** importe para cancelar el saldo facturado según las condiciones del resumen.
4. **Pago mínimo:** evita ciertos incumplimientos inmediatos, pero deja deuda que normalmente genera intereses.

> **Tip GPS:** Antes de financiar un consumo, compará el costo financiero total y no solamente el valor de la cuota.

## ¿Cómo leer tu resumen?

Revisá consumos, cuotas pendientes, intereses, cargos, impuestos y el monto total. Si detectás un movimiento que no reconocés, contactá a la entidad emisora por sus canales oficiales cuanto antes.

## Recursos útiles

El [Banco Central de la República Argentina](https://www.bcra.gob.ar/) publica información de educación financiera y derechos de usuarias de servicios financieros.

## Preguntas frecuentes

### ¿Pagar el mínimo es lo mismo que pagar todo?

No. Generalmente el saldo que queda sin pagar genera intereses.

### ¿Puedo desconocer un consumo?

Existen procedimientos de reclamo ante la entidad. Verificá los plazos y requisitos vigentes y conservá la documentación.
'''),
'¿Estoy lista para mudarme?':('Mudarte puede ser un sueño; descubrir cuánto cuesta, no tanto. Te ayudamos a ordenar los números y las preguntas antes de decidir.', '''## Hacé números antes de hacer cajas

Calculá el costo mensual completo: vivienda, expensas, servicios, transporte, comida, conectividad y gastos habituales. Sumá un margen para imprevistos.

## Costos iniciales que no conviene olvidar

- Gastos de mudanza y traslado.
- Depósitos o garantías que correspondan según el contrato y la normativa vigente.
- Artículos básicos para equipar la casa.
- Conexiones e instalaciones necesarias.

## Preguntas para una visita

1. ¿Qué servicios están conectados y a nombre de quién?
2. ¿Qué gastos corresponden a la vivienda y cuáles a la inquilina?
3. ¿Hay filtraciones, problemas eléctricos o de presión de agua?
4. ¿Qué condiciones de ajuste y rescisión establece el contrato?

> **Tip GPS:** Pedí toda la información importante por escrito. Compará el texto contractual con las reglas actuales aplicables antes de firmar.

## ¿Y si todavía no te alcanza?

No significa que fracasaste. Tener una fecha objetivo y un fondo para la mudanza puede ayudarte a tomar una mejor decisión.

## Preguntas frecuentes

### ¿Tengo que firmar en el momento?

No te apresures. Pedí tiempo para leer el contrato y, si tenés dudas, consultá con un profesional o un organismo competente.
''')}
for cat,titles in cats.items():
 for title in titles:
  desc,body=articles.get(title,('',''))
  published=bool(body)
  fm=f'''---\ntitle: {title!r}\ncategory: {cat}\nstatus: {'published' if published else 'draft'}\nfeatured: {'true' if published else 'false'}\ndescription: {desc!r}\ncover: ''\nvideo: ''\ndownloadable: ''\nupdated: '2026-10-09'\n---\n\n'''
  (root/(slug(title)+'.md')).write_text(fm+(body if published else '# Pendiente de redacción\n\nEste problema está cargado en el CMS como borrador. Redactar y revisar antes de publicar.\n'),encoding='utf8')
print('Archivos creados:',sum(1 for _ in root.glob('*.md')))
