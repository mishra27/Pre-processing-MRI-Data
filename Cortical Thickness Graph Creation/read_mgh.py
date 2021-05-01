import nibabel as nb   


def read_mgh(filename):
    img = nb.load(filename)
    data = img.get_fdata()
    return data

th = read_mgh("rh.thickness.mgh")
thickness = []
for i in range(len(th)):
    t = []
    t.append(th[i][0][0])
    thickness.append(t)

print(thickness)
