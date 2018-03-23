from cx_Freeze import setup, Executable

includes = ["atexit"] 

buildOptions = dict(
    create_shared_zip=True,
    append_script_to_exe=True,
    includes=includes
)

executables = [
    Executable(
        script='Temperature Converter.py',
        targetName='Python Temperature Converter.exe',
        base="Win32GUI" # THIS ONE IS IMPORTANT FOR GUI APPLICATION
    )
]

setup(
    name="Python Temperature Converter",
    version="1.0",
    description="",
    options=dict(build_exe=buildOptions),
    executables=executables
)
