import cx_Freeze

executaveis = [
                cx_Freeze.Executable(scrip='main.py', icon = 'assets/icon.ico')]
cx_Freeze.setup(
    name = 'Iron Man',
    options = {
        'build.exe':{
            'packages':['pyagme'],
            'include_files':['assets']
        }
    }, executables = executaveis
)
