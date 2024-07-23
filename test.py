import os


import packages


def test():
    # Настройка драйвера Nvidia для Wayland
    with open("/etc/modprobe.d/nvidia.conf", "w") as file:
        file.write("options nvidia-drm modeset=1\n")

    # Настройка LightDM для работы с Wayland
    lightdm_conf = "/etc/lightdm/lightdm.conf"
    with open(lightdm_conf, "r") as file:
        lines = file.readlines()

    with open(lightdm_conf, "w") as file:
        for line in lines:
            if line.strip().startswith("#greeter-session="):
                file.write("greeter-session=lightdm-gtk-greeter\n")
            elif line.strip().startswith("#user-session="):
                file.write("user-session=hyprland\n")
            else:
                file.write(line)

    # Настройка полкита для Wayland
    with open("/etc/pam.d/lightdm", "a") as file:
        file.write("auth optional pam_gnome_keyring.so\n")
        file.write("session optional pam_gnome_keyring.so auto_start\n")


def test():
    install_list =  packages.PACMAN["BASE"] + \
                    packages.PACMAN["ENVIRONMENTS"] + \
                    packages.PACMAN["ENVIRONMENTS_ADDITION"] + \
                    packages.PACMAN["WINDOWS_MANAGER_COMPONENTS"] + \
                    packages.PACMAN["NVIDIA_DRIVER"] 

    os.system("sudo pacman -S --noconfirm " + ' '.join(install_list))