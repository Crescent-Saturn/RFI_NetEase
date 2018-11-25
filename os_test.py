import os


def cp_file(files):
    os.system(f'move {files} E:\\')


def transform(files):
    src = os.path.splitext(files)[0]
    try:
        os.system(f'ffmpeg -i {files} {src}.m4a')
    except Exception as e:
        raise
    else:
        os.system(f'del {files}')
    finally:
        print(os.system('dir'))


os.chdir('E:\\Downloads')

dst = [x for x in os.listdir('.') if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.mp3']


for x in dst:
    # os.system(f'copy {x} ffmpeg\\bin\\')
    cp_file(x)

os.chdir('E:\\')

for y in dst:
    transform(y)
