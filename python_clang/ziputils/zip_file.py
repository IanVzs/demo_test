import os
import sys
import zipfile
PLATFORM = sys.PLATFORM
if PLATFORM == "linux":
    home = os.environ.get("HOME")
    PATH_EXTRACT_HERE = os.path.join(home, ".local", "share")
elif PLATFORM == "win32":
    username = os.environ.get("USERNAME")
    PATH_EXTRACT_HERE = os.path.join("C:\\", "Users", username, "AppData", "Local", "Programs")
else:
    print("Please creat by manually. I think you can do this!")

ROOT_NAME = "test"
LNK_FILE_NAME = os.path.join("", "a")
ICON_FILE_NAME = ''

def extractall(path_zip):
    if zipfile.is_zipfile(path_zip):
        zfile = zipfile.ZipFile(path_zip, 'r')
        for name in zfile.namelist():
            print(name)
            if not os.path.exists(os.path.join(PATH_EXTRACT_HERE, name)):
                zfile.extract(name, PATH_EXTRACT_HERE)
            else:
                print("fuck you! 别瞎删!")
        # zfile.extractall(PATH_EXTRACT_HERE)
    else:
        print(f"{path_zip} not is zip file")

def create_shortcut():
    if PLATFORM == "linux":
        pass
    elif PLATFORM == "win32":
        creat_win()
    else:
        print("Please creat shortcut by manually. I think you can do this!")

def creat_win():
    import pythoncom
    from win32com.shell import shell
    # from win32com.shell import shellcon
    pythoncom.CoInitialize()
    try:
        if os.environ.get("HOME"):
            path_desktop = os.path.join(os.environ.get("HOME"), "Desktop")
        elif os.environ.get("USERNAME"):
            path_desktop = os.path.join( "C:\\", "Users", os.environ.get("USERNAME"), "Desktop")
        else:
            print("Plese change your fuck PC!!!")
        path_working = os.path.join(PATH_EXTRACT_HERE, ROOT_NAME)
        filename = os.path.join(path_working, LNK_FILE_NAME)
        # iconname = os.path.join(path_working, ICON_FILE_NAME)
        lnkname = os.path.join( path_desktop, f"{ROOT_NAME}.lnk")

        shortcut = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink, None,
            pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
        shortcut.SetPath(filename)

        shortcut.SetWorkingDirectory(path_working) # 设置快捷方式的起始位置, 不然会出现找不到辅助文件的情况
        # shortcut.SetIconLocation(iconname, 0)  # 可有可无，没有就默认使用文件本身的图标
        if os.path.splitext(lnkname)[-1] != '.lnk':
            lnkname += ".lnk"
        shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)

        return True
    except Exception as e:
        print(e.args)
        return False

if __name__ == "__main__":
    PATH_ZIPFILE= os.path.join(".", "test.zip")
    print(PATH_ZIPFILE)
    extractall(PATH_ZIPFILE)
    create_shortcut()
    # creat_win()
