from distutils.core import setup
import setup_translate


setup(name = 'enigma2-plugin-systemplugins-swapmanager',
		version='1.0',
		author='www.xtrend-united.de',
		author_email='www.xtrend-united.de',
		package_dir = {'SystemPlugins.SwapManager': 'src'},
		packages=['SystemPlugins.SwapManager'],
		description = 'do swapping, like you want',
		cmdclass = setup_translate.cmdclass,
	)

