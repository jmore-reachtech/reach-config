def __set_defaults_reach_yocto():
    set_default('DISTRO', 'reach')

def __after_init_reach_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']
    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-freescale',
                        'meta-openembedded/meta-oe',
                        'meta-qt5',
                        'meta-reach',
                    ]])

    # FSL EULA
    eulas.accept['meta-freescale/EULA'] = 'ACCEPT_FSL_EULA = "1"'

run_set_defaults(__set_defaults_reach_yocto)
run_after_init(__after_init_reach_yocto)
