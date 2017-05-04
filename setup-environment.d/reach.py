def __set_defaults_reach_yocto():
    import os
    import sys

    valid_distros = ['reach', 'reach-x11']
    valid_machines = ['g2c-43-24', 'g2c-43-24-kyocera',
                      'g2c-7-16', 'g2c-7-24', 'g2c-lite',
                      'g2c-mfg', 'g2h-solo-3', 'g2h-solo-3-r',
                      'g2h-solo-3f', 'g2h-solo-4', 'g2h-solo-4f',
                      'g2h-solo-13', 'g2h-solo-13f', 'g2h-solo-14',
                      'g2h-solo-14f', 'g2h-solo-11f', 'g2h-solo-11f-r',
                      'g2h-solo-12f', 'g2h-solo-6']

    local_conf_exists = os.path.isfile(os.path.join(build_dir,
                                                    'conf',
                                                    'local.conf'))

    def required_var_error(varname, valid_vals):
        sys.stderr.write("ERROR: You must set '%s' before setting up the environment.\n" %
                         (varname,))
        sys.stderr.write("       Possible values are %s\n" % valid_vals)
        sys.exit(1)

    def maybe_set_default(varname, valid_vals):
        try:
            val = os.environ[varname]
        except KeyError:
            val = None

        if val:
            if val in valid_vals:
                set_default(varname, val)
            else:
                required_var_error(varname, valid_vals)
        elif not local_conf_exists:
            required_var_error(varname, valid_vals)

    maybe_set_default('DISTRO', valid_distros)
    maybe_set_default('MACHINE', valid_machines)


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
