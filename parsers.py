import jmake
from pathlib import Path

jmake.setupenv()

workspace = jmake.Workspace('parsers')

paths = Path('.').glob('tree-sitter-*')
for p in paths:
    project = jmake.Project(str(p), jmake.Target.SHARED_LIBRARY)
    src = str(p / 'src')
    files = jmake.glob(src, '**/*.c') + jmake.glob(src, '**/*.h')
    project.add(files)
    project.include(jmake.fullpath(src))
    workspace.add(project)

jmake.generate(workspace)


