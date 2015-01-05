def __set_defaults_reach_yocto():
    import os
    import sys

    valid_distros = ['reach', 'reach-x11']
    valid_machines = ['g2c-43-24', 'g2c-43-24-kyocera',
                      'g2c-7-16', 'g2c-7-24', 'g2c-lite',
                      'g2c-mfg', 'g2h-solo-1', 'g2h-solo-2',
                      'g2h-solo-3', 'g2h-solo-4', 'g2s-101-24']

    try:
        distro = os.environ['DISTRO']
    except KeyError:
        distro = None

    try:
        machine = os.environ['MACHINE']
    except KeyError:
        machine = None

    if not distro or distro not in valid_distros:
        sys.stderr.write("ERROR: You must set 'DISTRO' before setting up the environment.\n")
        sys.stderr.write("       Possible values are %s\n" % valid_distros)
        sys.exit(1)

    if not machine or machine not in valid_machines:
        sys.stderr.write("ERROR: You must set 'MACHINE' before setting up the environment.\n")
        sys.stderr.write("       Possible values are %s\n" % valid_machines)
        sys.exit(1)

    set_default('DISTRO', os.environ['DISTRO'])
    set_default('MACHINE', os.environ['MACHINE'])

def __after_init_reach_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']
    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                     'meta-fsl-arm',
                     'meta-openembedded/meta-oe',
                     'meta-openembedded/meta-ruby',
                     'meta-openembedded/meta-python',
                     'meta-reach',
                     'meta-qt5'
                    ]])

    # FSL EULA
    eulas.accept['meta-fsl-arm/EULA'] = 'ACCEPT_FSL_EULA = "1"'

run_set_defaults(__set_defaults_reach_yocto)
run_after_init(__after_init_reach_yocto)
