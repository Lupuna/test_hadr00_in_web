from django.conf import settings
import subprocess


def hadr_zero_zero_exemple(**data):
    command = f"source {settings.GEANT_SETUP_SCRIPT} && {settings.GEANT_HADR00_EXEMPLE}"
    process = subprocess.Popen(
        command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        executable="/bin/bash"
    )
    output, errors = process.communicate(settings.GEANT_COMMANDS_TEMPLATE.format(**data))
    return output
