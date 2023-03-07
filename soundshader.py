import os

sound_range = (10, 10, 150, 1600)
range_curves = ('{0,1},{10,1}','{0,1},{10,1}','{0,1},{10,1.1},{150,0.8}','{0,1},{10,0},{150,0.8},{1600,0.25}')

def listdirs():
    dirlist = next(os.walk('.'))[1]
    for i,j in enumerate(dirlist):
        if j == '.git':
            dirlist.pop(i)
    return dirlist

def sortdircontent(dirlist):
    for i in dirlist:
        subfiles = []
        tempsubdirlist = next(os.walk('./' + str(i)))[1]
        for j,k in enumerate(tempsubdirlist):
            subfiles.append([k])
            tempfilelist = os.listdir('./' + str(i) + '/' + str(k))
            subfiles[j].append(tempfilelist)
        yield subfiles

def toCfgSoundShaders(dirlist,subf):
    global addonname, sound_range, range_curves
    with open('config.cpp', 'w') as f:
        f.write('class CfgSoundShaders\n{\n\t')
        for i,j in enumerate(dirlist):
            for k,l in enumerate(subf[i]):
                f.write(f'class {j}_{subf[i][k][0]}_soundshader\n\t{{\n\t\tsamples[]=\n\t\t{{\n')
                for s_id, s_name in enumerate(subf[i][k][1]):
                    lastfile = len(subf[i][k][1])
                    f.write(f'\t\t\t{{"{addonname}\sound\weapons\{j}\{subf[i][k][0]}\{subf[i][k][1][s_id]}", 1}}')
                    if(subf[i][k][1][-1] != subf[i][k][1][s_id]):
                        f.write(f',')
                    f.write('\n')
                f.write(f'\t\t}};\n\t\tvolume=1.3;\n\t\trange={sound_range[k]};\n\t\trangecurve[]={{{range_curves[k]}}};\n\t}};\n\t')
        f.write('\n};')
                


addonname = str(input("Your addon name="))
ungen = []
dirlist = listdirs()
for i in sortdircontent(dirlist):
    ungen.append(i)
toCfgSoundShaders(dirlist,ungen)