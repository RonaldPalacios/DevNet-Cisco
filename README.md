🌐 Cisco DevNet Toolkit: Automatización, APIs y NetDevOps<p align="center"><img src="https://img.shields.io/badge/DevNet-Automation-blue?style=for-the-badge&logo=cisco" alt="Cisco DevNet Badge"/><img src="https://img.shields.io/badge/Python-Automation-yellowgreen?style=for-the-badge&logo=python" alt="Python Badge"/><img src="https://img.shields.io/badge/Ansible-NetDevOps-red?style=for-the-badge&logo=ansible" alt="Ansible Badge"/></p></br>📜 Descripción del ProyectoEste repositorio es una colección esencial de código de ejemplo, scripts de automatización, y laboratorios prácticos enfocados en la programabilidad de redes y el ecosistema Cisco DevNet.El objetivo es facilitar a ingenieros de redes y desarrolladores la adopción de la metodología NetDevOps para operar, gestionar y optimizar la infraestructura de Cisco a escala.</br>
</br>
📌Tabla de Contenidos Enfoque Principal </br> Estructura del RepositorioTecnologías ClaveComenzando (Getting Started)Requisitos PreviosInstalaciónCasos de UsoContribucionesLicencia</br>
</br>
💡Enfoque Principal </br> El código se organiza para cubrir los siguientes pilares de la programabilidad: </br>:gear: Automatización de Redes (NetDevOps): Uso de Python (con librerías como Netmiko, Paramiko, NAPALM, pyATS) y Ansible para tareas rutinarias de configuración, recopilación de datos y pruebas en dispositivos Cisco (IOS-XE, NX-OS, etc.).</br> :gear: APIs y SDN: Ejemplos de consumo de APIs REST con plataformas líderes como Cisco DNA Center, Meraki, Webex y Cisco ACI.Gestión de Infraestructura: Scripts para la orquestación y despliegue usando herramientas como Terraform o NSO (Network Service Orchestrator).DevOps y Contenedores: Integración básica con Docker para asegurar entornos de ejecución consistentes. </br>
</br>
📂Estructura del Repositorio </br> El contenido está organizado por la tecnología principal o la plataforma de Cisco:</br>
├── ansible/                ✔️   # Playbooks y roles de Ansible para configuración.
├── python/</br>
│   ├── netmiko-examples/   ✔️   # Ejemplos de SSH/Telnet con Netmiko.</br>
│   ├── dnac-scripts/       ✔️   # Scripts que usan la API de Cisco DNA Center.</br>
│   └── meraki-api-tools/   ✔️   # Herramientas para interactuar con la API de Meraki.</br>
├── postman-collections/    ✔️   # Colecciones para probar APIs (DNA Center, Meraki, etc.).</br>
└── terraform-labs/         ✔️   # Ejemplos de infraestructura como código (IaC).</br>
</br>
🛠️ Tecnologías y Plataformas Clave </br> Tipo de Herramientas/Plataformas Descripción Lenguaje PrincipalPython 3.xBase de la automatización y desarrollo de scripts.ConfiguraciónAnsible, TerraformGestión de configuración y despliegue de infraestructura como código.DispositivosIOS-XE, NX-OS, Meraki, ACIEntornos de red y nube más comunes.ControladorasCisco DNA Center, NSOPlataformas de automatización centralizada.Protocolos/APIsREST/RESTCONF, NETCONF, gRPCInteracción programática con dispositivos y controladoras.</br>
</br>
🧪 Casos de Uso
Ejecuta y adapta estos ejemplos a tus necesidades. Aquí tienes algunos puntos de partida para explorar:

python/netmiko-examples/config_backup.py: Script para generar un backup masivo de la configuración de n dispositivos IOS-XE.
ansible/ios_vlan_deployment.yml: Playbook de Ansible que implementa una nueva VLAN en un grupo de switches.
dnac-scripts/get_device_health.py: Consulta la API de Cisco DNA Center para obtener el estado de salud de todos los dispositivos gestionados.</br>
</br>

💬 Contribuciones
¡Tu colaboración es valiosa para la comunidad! Si tienes un script DevNet genial, una corrección o una mejora, por favor, ¡contribuye!
Haz un fork del repositorio.
Crea una nueva branch para tu feature (git checkout -b feature/nuevo-script-meraki).
Asegúrate de que tu código sigue las buenas prácticas.
Abre un Pull Request detallando tus cambios.</br>
</br>
📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.</br>
<p align="center"><img src="https://img.shields.io/badge/DevNet-Automation-blue?style=for-the-badge&logo=cisco" alt="Cisco DevNet Badge"/><img src="https://img.shields.io/badge/Python-Automation-yellowgreen?style=for-the-badge&logo=python" alt="Python Badge"/><img src="https://img.shields.io/badge/Ansible-NetDevOps-red?style=for-the-badge&logo=ansible" alt="Ansible Badge"/></p>
